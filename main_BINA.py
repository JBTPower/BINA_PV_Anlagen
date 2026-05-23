import streamlit as st
import pandas as pd
import gpd
import rasterio
import requests
import random  # Neu importiert für das Zufallsprinzip
from geopy.geocoders import Nominatim
from shapely.geometry import Point

# --- KONFIGURATION & STYLING ---
st.set_page_config(page_title="PV-Potenzial Schweiz", layout="wide")

st.markdown("""
<style>
.main { background-color: #f5f7f9; }
.pvd-card {
    background-color: #262730;
    padding: 20px;
    border-radius: 10px;
    color: white;
    margin-bottom: 20px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
.pvd-kpi-val { font-size: 32px; font-weight: bold; color: #ffcc00; }
.pvd-kpi-lbl { font-size: 14px; color: #bcbcbc; }
</style>
""", unsafe_allow_html=True)

# --- DATEN-LADEFUNKTIONEN ---
@st.cache_resource(show_spinner="Lade Solardaten…")
def load_solar_data():
    url = "https://raw.githubusercontent.com/nesasad/BINA_PV_Anlagen/main/Data/PVOUT.tif"
    return rasterio.open(url)

@st.cache_data(show_spinner="Lade Stromtarife…")
def load_tariffs():
    url = "https://raw.githubusercontent.com/nesasad/BINA_PV_Anlagen/main/Data/Rohdaten-Tarife-Standard-Produkt.csv"
    df = pd.read_csv(url)
    if 'kategorieName' in df.columns:
        df = df[df['kategorieName'] == 'H4']
    return df

@st.cache_resource(show_spinner="Lade Gemeindedaten…")
def load_boundaries():
    url = "https://raw.githubusercontent.com/nesasad/BINA_PV_Anlagen/main/Data/swissBOUNDARIES3D_1_5_LV95_LN02.gpkg"
    return gpd.read_file(url, layer='tlm_hoheitsgebiet')

# --- LOGIK ---
def geocode_address(address):
    try:
        url = (
            "https://api3.geo.admin.ch/rest/services/api/SearchServer"
            f"?searchText={address}&type=locations&origins=address"
        )
        res = requests.get(url).json()
        if res.get("results"):
            attrs = res["results"][0]["attrs"]
            return attrs["lat"], attrs["lon"], attrs["label"]
    except:
        pass

    try:
        geolocator = Nominatim(user_agent="pv_app")
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude, location.address
    except:
        pass

    return None, None, None

def get_pv_value(tif, lat, lon):
    try:
        for val in tif.sample([(lon, lat)]):
            return float(val[0])
    except:
        pass
    return 0.0

# --- UI ---
st.title("☀️ PV-Potenzial-Check Schweiz")
st.markdown(
    "Ermitteln Sie die Attraktivität einer Solaranlage basierend auf "
    "Wetterdaten und lokalen Stromtarifen."
)

st.markdown("## 🔍 Standortanalyse starten")
st.markdown(
    "Geben Sie Ihre Adresse ein und erhalten Sie eine Einschätzung "
    "zur Wirtschaftlichkeit einer Photovoltaikanlage an diesem Standort."
)

st.markdown("### 📍 Adresse eingeben")

address_input = st.text_input(
    "Strasse und Ort",
    placeholder="Zollstrasse 17, 8005 Zürich"
)

check_button = st.button("Analyse starten", type="primary")

# --- ANALYSE-TRIGGER ---
analysis_started = check_button and address_input.strip() != ""

if check_button and address_input.strip() == "":
    st.warning("Bitte geben Sie eine Adresse ein.")

# --- ANALYSE ---
if analysis_started:
    lat, lon, full_address = geocode_address(address_input)

    if lat:
        tif = load_solar_data
