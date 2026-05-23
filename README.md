## PV-Potenzial Schweiz (BINA Case Study)

Dieses Repository enthält die Anwendung und Datenvorbereitung für ein interaktives Analysetool zur Bestimmung des Photovoltaik-Potenzials und der wirtschaftlichen Attraktivität von Hausanlagen in der Schweiz. Das Projekt wurde im Rahmen einer Case Study für das Modul BINA entwickelt.

## Webseite PV-Rechner
Die App ist live auf Streamlit Cloud verfügbar:  
**[[binapvpotenzial.streamlit.app](https://binapvpotenzial.streamlit.app/)]**

---

## Anleitung Notebook in Google Colab öffnen
1. Öffne **[https://colab.research.google.com](https://colab.research.google.com)**
2. Klicke auf "Github"
<img width="679" height="526" alt="Bildschirmfoto 2026-05-23 um 20 28 47" src="https://github.com/user-attachments/assets/2b556ad1-0f10-4eff-b3c0-b901ea00b600" />

3. Füge in das Suchfeld den URL hinzu: **[https://github.com/JBTPower/BINA_PV_Anlagen](https://github.com/JBTPower/BINA_PV_Anlagen)**

<img width="675" height="524" alt="Bildschirmfoto 2026-05-23 um 20 32 10" src="https://github.com/user-attachments/assets/c999ade8-8c5a-4e38-88c2-21563bc7ba72" />

5. Wähle das entsprechende Notebook aus.

---

## Projektstruktur & Dateitabelle

Das Repository gliedert sich in folgende Kernkomponenten:

Datei / OrdnerBeschreibungData/Ordner mit den Roh- und vorbereiteten Geodaten (PVOUT.tif, Tarife als CSV, Gemeinde-Grenzdaten als Geopackage).01_PVOUT_Preparation.ipynbJupyter Notebook (Google Colab) zur Vorbereitung, Filterung und Transformation der Rasterdaten für das Solarpotenzial.02_Stromdaten_Preparation.ipynbJupyter Notebook zur Bereinigung, Filterung (Fokus auf Kategorie H4) und Zuordnung der Schweizer Stromtarifdaten.03_PV_Potenzial_Vergleich.ipynbJupyter Notebook für statistische Analysen, Validierungen und Vergleiche der berechneten Potenziale.2026_BINA_PV_Potenzial_Präsentation_Gru...Die Präsentationsfolien der Gruppe zum Projekt (z. B. als PDF oder PowerPoint).2026_BINA_PV_Potenzial_Video_Gruppe_7_...Das begleitende Projekt- oder Vorstellungsvideo der Gruppe 7.README.mdDokumentation des Repositories mit Installationshinweisen und Projektbeschreibungen.main_BINA.pyDas Hauptskript der interaktiven Streamlit-Webanwendung (GUI, Geocoding-Logik und Datenvisualisierung).requirements.txtListe der benötigten Python-Bibliotheken zur Ausführung der Anwendung (z. B. streamlit, geopandas, rasterio)..DS_StoreOptionale Systemdatei: Automatisch von macOS erstellte Datei (kann ignoriert oder über .gitignore ausgeschlossen werden).

---

## Technische Umsetzung & Datenquellen

### Datenquellen
* **Solarertrag (PVOUT):** Global Solar Atlas / Geo-optimierte Rasterdaten für die Schweiz.
* **Stromtarife:** Offizielle Schweizer Stromtarif-Rohdaten für das Standard-Produkt (Fokus auf Haushaltstyp H4).
* **Gemeindegrenzen:** `swissBOUNDARIES3D` des Bundesamtes für Landestopografie (swisstopo).

### Verwendete Technologien
* **Frontend/GUI:** Streamlit (Python) mit benutzerdefiniertem CSS-Styling für KPI-Karten.
* **Geodatenverarbeitung:** `geopandas` für räumliche Joins (`sjoin`), `rasterio` zur Beprobung von TIF-Rasterdaten und `shapely` zur Punktgenerierung.
* **Geocoding:** Integration der offiziellen Swisstopo Search API (`api3.geo.admin.ch`) mit Fallback auf `geopy` (Nominatim).

---
