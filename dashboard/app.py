
from pathlib import Path

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =====================================================
# 1. PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Bike Sharing Analytics",
    page_icon="🚲",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# 2. CUSTOM CSS - MODERN DARK THEME
# =====================================================

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: #0B1120;
        color: #E5E7EB;
    }

    [data-testid="stSidebar"] {
        background: #111827;
        border-right: 1px solid #263244;
    }

    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] label {
        color: #E5E7EB !important;
    }

    .main-title {
        font-size: 34px;
        font-weight: 800;
        color: #F8FAFC;
        letter-spacing: -1px;
        margin-bottom: 5px;
    }

    .subtitle {
        color: #94A3B8;
        font-size: 14px;
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 21px;
        font-weight: 700;
        color: #F1F5F9;
        margin-top: 15px;
        margin-bottom: 5px;
    }

    .section-description {
        font-size: 13px;
        color: #94A3B8;
        margin-bottom: 15px;
    }

    .metric-card {
        background: linear-gradient(145deg, #182438, #111B2D);
        border: 1px solid #26364D;
        border-radius: 15px;
        padding: 20px;
        min-height: 125px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.15);
    }

    .metric-label {
        color: #94A3B8;
        font-size: 13px;
        font-weight: 500;
        margin-bottom: 12px;
    }

    .metric-value {
        color: #F8FAFC;
        font-size: 27px;
        font-weight: 800;
        letter-spacing: -1px;
    }

    .metric-note {
        color: #38BDF8;
        font-size: 11px;
        margin-top: 7px;
    }

    .insight-card {
        background: #142236;
        border-left: 4px solid #38BDF8;
        border-radius: 10px;
        padding: 15px 18px;
        margin-top: 10px;
        margin-bottom: 15px;
        color: #CBD5E1;
        font-size: 13px;
        line-height: 1.7;
    }

    .footer {
        color: #64748B;
        text-align: center;
        font-size: 12px;
        padding: 25px 0 10px 0;
    }

    div[data-testid="stPlotlyChart"] {
        background: #111B2D;
        border: 1px solid #26364D;
        border-radius: 14px;
        padding: 10px;
    }

    div[data-testid="stDataFrame"] {
        border: 1px solid #26364D;
        border-radius: 10px;
    }

    .stMultiSelect div[data-baseweb="select"] {
        background-color: #1E293B;
    }

    hr {
        border-color: #26364D;
    }
</style>
""", unsafe_allow_html=True)


# =====================================================
# 3. DATA DIRECTORY
# =====================================================

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data" / "cleaned"


# =====================================================
# 4. LOAD DATA
# =====================================================

@st.cache_data
def load_data():
    day = pd.read_csv(DATA_DIR / "day_cleaned.csv")
    hour = pd.read_csv(DATA_DIR / "hour_cleaned.csv")

    day["dteday"] = pd.to_datetime(day["dteday"])
    hour["dteday"] = pd.to_datetime(hour["dteday"])

    return day, hour


try:
    day_df, hour_df = load_data()

except Exception as e:
    st.error(f"Gagal memuat dataset: {e}")
    st.info("Pastikan dataset tersedia di folder data/cleaned.")
    st.stop()


# =====================================================
# 5. DATA TRANSFORMATION
# =====================================================

season_map = {
    1: "Spring",
    2: "Summer",
    3: "Fall",
    4: "Winter"
}

weather_map = {
    1: "Clear / Partly Cloudy",
    2: "Mist / Cloudy",
    3: "Light Rain / Snow",
    4: "Heavy Rain / Snow"
}

month_map = {
    1: "January", 2: "February", 3: "March",
    4: "April", 5: "May", 6: "June",
    7: "July", 8: "August", 9: "September",
    10: "October", 11: "November",
    12: "December"
}

for df in [day_df, hour_df]:
    df["season_name"] = df["season"].map(season_map)
    df["year"] = df["yr"].map({0: "2011", 1: "2012"})
    df["month_name"] = df["mnth"].map(month_map)
    df["month_year"] = df["dteday"].dt.strftime("%b %Y")

day_df["weather_name"] = day_df["weathersit"].map(weather_map)

hour_df["day_type"] = hour_df["workingday"].map({
    0: "Non-Working Day",
    1: "Working Day"
})


# =====================================================
# 6. PLOTLY DARK THEME
# =====================================================

COLORS = {
    "blue": "#38BDF8",
    "cyan": "#22D3EE",
    "purple": "#A78BFA",
    "orange": "#FB923C",
    "green": "#34D399",
    "pink": "#F472B6"
}

CHART_TEMPLATE = "plotly_dark"


# =====================================================
# 7. SIDEBAR FILTERS
# =====================================================

with st.sidebar:

    st.markdown("## 🚲 Bike Analytics")
    st.caption("DATA EXPLORATION PLATFORM")

    st.divider()

    st.markdown("### Filter Data")

    years = st.multiselect(
        "Tahun",
        options=["2011", "2012"],
        default=["2011", "2012"]
    )

    seasons = st.multiselect(
        "Musim",
        options=["Spring", "Summer", "Fall", "Winter"],
        default=["Spring", "Summer", "Fall", "Winter"]
    )

    months = st.multiselect(
        "Bulan",
        options=list(month_map.values()),
        default=list(month_map.values())
    )

    weather_options = list(weather_map.values())

    weathers = st.multiselect(
        "Kondisi Cuaca",
        options=weather_options,
        default=weather_options
    )

    st.divider()

    st.caption("Dataset: Bike Sharing Dataset")
    st.caption("Washington D.C. | 2011–2012")


# =====================================================
# 8. FILTER DATA
# =====================================================

filtered_day = day_df[
    (day_df["year"].isin(years)) &
    (day_df["season_name"].isin(seasons)) &
    (day_df["month_name"].isin(months)) &
    (day_df["weather_name"].isin(weathers))
].copy()

filtered_hour = hour_df[
    (hour_df["year"].isin(years)) &
    (hour_df["season_name"].isin(seasons)) &
    (hour_df["month_name"].isin(months)) &
    (hour_df["weathersit"].map(weather_map).isin(weathers))
].copy()

if filtered_day.empty or filtered_hour.empty:
    st.warning("Tidak ada data untuk kombinasi filter yang dipilih.")
    st.stop()


# =====================================================
# 9. HEADER
# =====================================================

st.markdown(
    '<div class="main-title">🚲 Bike Sharing Analytics</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle"> '
    'Explore rental patterns, user behavior, weather impact, '
    'and seasonal demand | Washington D.C. 2011–2012'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# =====================================================
# 10. KPI CARDS
# =====================================================

total_rentals = filtered_day["cnt"].sum()
total_casual = filtered_day["casual"].sum()
total_registered = filtered_day["registered"].sum()
average_daily = filtered_day["cnt"].mean()

casual_percentage = (
    total_casual / total_rentals * 100
    if total_rentals else 0
)

registered_percentage = (
    total_registered / total_rentals * 100
    if total_rentals else 0
)

st.markdown("### Performance Overview")

k1, k2, k3, k4 = st.columns(4)

def metric_card(column, label, value, note):
    with column:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-note">{note}</div>
        </div>
        """, unsafe_allow_html=True)


metric_card(
    k1, "Total Rentals",
    f"{total_rentals:,.0f}",
    "Total bicycle rental transactions"
)

metric_card(
    k2, "Casual Users",
    f"{total_casual:,.0f}",
    f"{casual_percentage:.1f}% of total rentals"
)

metric_card(
    k3, "Registered Users",
    f"{total_registered:,.0f}",
    f"{registered_percentage:.1f}% of total rentals"
)

metric_card(
    k4, "Daily Average",
    f"{average_daily:,.0f}",
    "Average rentals per day"
)

st.divider()


# =====================================================
# 11. BUSINESS QUESTION 1
# MONTHLY RENTAL TREND
# =====================================================

st.markdown(
    '<div class="section-title">01 | Monthly Rental Trends</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'How does bicycle rental demand develop over time?'
    '</div>',
    unsafe_allow_html=True
)

monthly = (
    filtered_day.groupby(["year", "mnth"], as_index=False)
    .agg(average_rentals=("cnt", "mean"))
)

monthly["month_name"] = monthly["mnth"].map(month_map)

monthly["date"] = pd.to_datetime(
    monthly["year"] + "-" +
    monthly["mnth"].astype(str).str.zfill(2) + "-01"
)

monthly = monthly.sort_values("date")

fig_monthly = px.line(
    monthly,
    x="date",
    y="average_rentals",
    color="year",
    markers=True,
    template=CHART_TEMPLATE,
    color_discrete_sequence=[
        COLORS["blue"], COLORS["purple"]
    ],
    labels={
        "date": "Month",
        "average_rentals": "Average Daily Rentals",
        "year": "Year"
    }
)

fig_monthly.update_layout(
    height=390,
    hovermode="x unified",
    legend_title_text="Year",
    margin=dict(l=20, r=20, t=30, b=20)
)

st.plotly_chart(fig_monthly, use_container_width=True)

if not monthly.empty:
    highest_month = monthly.loc[
        monthly["average_rentals"].idxmax()
    ]

    st.markdown(
        f"""
        <div class="insight-card">
        <b>Key Insight</b><br>
        Pada kombinasi filter saat ini, rata-rata penyewaan harian
        tertinggi terjadi pada <b>{highest_month['month_name']}
        {highest_month['year']}</b>, dengan sekitar
        <b>{highest_month['average_rentals']:,.0f}</b>
        penyewaan per hari.
        </div>
        """,
        unsafe_allow_html=True
    )


# =====================================================
# 12. BUSINESS QUESTION 2
# HOURLY RENTAL PATTERN
# =====================================================

st.markdown(
    '<div class="section-title">02 | Hourly Rental Patterns</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'How do rental patterns differ between working and non-working days?'
    '</div>',
    unsafe_allow_html=True
)

hourly = (
    filtered_hour.groupby(
        ["hr", "day_type"], as_index=False
    )
    .agg(average_rentals=("cnt", "mean"))
)

fig_hourly = px.line(
    hourly,
    x="hr",
    y="average_rentals",
    color="day_type",
    markers=True,
    template=CHART_TEMPLATE,
    color_discrete_map={
        "Working Day": COLORS["blue"],
        "Non-Working Day": COLORS["orange"]
    },
    labels={
        "hr": "Hour of Day",
        "average_rentals": "Average Rentals",
        "day_type": "Day Type"
    }
)

fig_hourly.update_xaxes(
    tickmode="linear",
    dtick=1
)

fig_hourly.update_layout(
    height=390,
    hovermode="x unified",
    margin=dict(l=20, r=20, t=30, b=20)
)

st.plotly_chart(fig_hourly, use_container_width=True)

if not hourly.empty:
    peak_hour = hourly.loc[
        hourly["average_rentals"].idxmax()
    ]

    st.markdown(
        f"""
        <div class="insight-card">
        <b>Key Insight</b><br>
        Jam dengan rata-rata penyewaan tertinggi pada data
        yang difilter adalah pukul
        <b>{int(peak_hour['hr']):02d}:00</b>,
        dengan rata-rata
        <b>{peak_hour['average_rentals']:,.0f}</b>
        penyewaan.
        </div>
        """,
        unsafe_allow_html=True
    )


# =====================================================
# 13. BUSINESS QUESTION 3
# WEATHER IMPACT
# =====================================================

st.markdown(
    '<div class="section-title">03 | Weather Impact Analysis</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'How do weather conditions relate to bicycle rental demand?'
    '</div>',
    unsafe_allow_html=True
)

weather = (
    filtered_day.groupby("weather_name", as_index=False)
    .agg(average_rentals=("cnt", "mean"))
    .sort_values("average_rentals", ascending=True)
)

fig_weather = px.bar(
    weather,
    x="average_rentals",
    y="weather_name",
    orientation="h",
    text="average_rentals",
    template=CHART_TEMPLATE,
    color="average_rentals",
    color_continuous_scale=["#164E63", "#22D3EE"],
    labels={
        "average_rentals": "Average Daily Rentals",
        "weather_name": "Weather Condition"
    }
)

fig_weather.update_traces(
    texttemplate="%{text:,.0f}",
    textposition="outside"
)

fig_weather.update_layout(
    height=350,
    showlegend=False,
    coloraxis_showscale=False,
    margin=dict(l=20, r=60, t=30, b=20)
)

st.plotly_chart(fig_weather, use_container_width=True)

if not weather.empty:
    best_weather = weather.loc[
        weather["average_rentals"].idxmax()
    ]

    st.markdown(
        f"""
        <div class="insight-card">
        <b>Key Insight</b><br>
        Kondisi cuaca dengan rata-rata penyewaan tertinggi
        pada data yang difilter adalah
        <b>{best_weather['weather_name']}</b>,
        dengan rata-rata
        <b>{best_weather['average_rentals']:,.0f}</b>
        penyewaan per hari.
        </div>
        """,
        unsafe_allow_html=True
    )


# =====================================================
# 14. BUSINESS QUESTION 4
# SEASONAL USER COMPARISON
# =====================================================

st.markdown(
    '<div class="section-title">04 | Seasonal User Analysis</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'How do casual and registered users behave across seasons?'
    '</div>',
    unsafe_allow_html=True
)

seasonal = (
    filtered_day.groupby("season_name", as_index=False)
    .agg(
        casual=("casual", "mean"),
        registered=("registered", "mean")
    )
)

seasonal_long = seasonal.melt(
    id_vars="season_name",
    value_vars=["casual", "registered"],
    var_name="User Type",
    value_name="Average Rentals"
)

fig_season = px.bar(
    seasonal_long,
    x="season_name",
    y="Average Rentals",
    color="User Type",
    barmode="group",
    template=CHART_TEMPLATE,
    color_discrete_map={
        "casual": COLORS["orange"],
        "registered": COLORS["blue"]
    },
    category_orders={
        "season_name": ["Spring", "Summer", "Fall", "Winter"]
    },
    labels={
        "season_name": "Season"
    }
)

fig_season.update_layout(
    height=390,
    margin=dict(l=20, r=20, t=30, b=20)
)

st.plotly_chart(fig_season, use_container_width=True)

if not seasonal.empty:
    best_season = seasonal.loc[
        seasonal["registered"].idxmax()
    ]

    st.markdown(
        f"""
        <div class="insight-card">
        <b>Key Insight</b><br>
        Rata-rata penyewaan pengguna registered tertinggi
        terjadi pada musim <b>{best_season['season_name']}</b>,
        yaitu sekitar
        <b>{best_season['registered']:,.0f}</b>
        penyewaan per hari.
        </div>
        """,
        unsafe_allow_html=True
    )


# =====================================================
# 15. DATA EXPLORER
# =====================================================

st.divider()

st.markdown(
    '<div class="section-title">Data Explorer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Explore the filtered dataset used in this dashboard.'
    '</div>',
    unsafe_allow_html=True
)

tab1, tab2 = st.tabs([
    "Daily Dataset",
    "Hourly Dataset"
])

with tab1:
    st.dataframe(
        filtered_day[
            ["dteday", "season_name", "weather_name",
             "casual", "registered", "cnt"]
        ],
        use_container_width=True,
        hide_index=True
    )

with tab2:
    st.dataframe(
        filtered_hour[
            ["dteday", "hr", "day_type",
             "casual", "registered", "cnt"]
        ],
        use_container_width=True,
        hide_index=True
    )


# =====================================================
# 16. FOOTER
# =====================================================

st.markdown("""
<div class="footer">
    <b>BIKE SHARING ANALYTICS</b><br>
    Data Analysis Project | Washington D.C. | 2011–2012<br>
    Built with Python, Pandas, Plotly and Streamlit
</div>
""", unsafe_allow_html=True)
