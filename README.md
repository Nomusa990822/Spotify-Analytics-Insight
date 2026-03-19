# Spotify Analytics Insight: What Makes a Song Popular?

## Project Overview

This project explores the key factors that drive song popularity on Spotify using real-world datasets. It analyzes how audio features such as danceability, energy, tempo (BPM), and valence influence streaming performance.

The project follows a complete data analytics workflow — from raw data to insights — combining Python, SQL, and data visualization to uncover meaningful patterns.

---

## Business Question

**What makes a song successful on Spotify?**

This project answers this by analyzing how musical attributes and metadata impact streaming performance.

---
## Analysis Questions Explored

1. What BPM range produces the most streamed songs?
2. Do explicit songs perform better than clean songs?
3. How does valence (happiness) affect streams?
4. Which genres dominate top-performing songs?
5. What audio features define high-performing tracks?

---

## Key Insights

- Songs with higher **energy and danceability** tend to achieve more streams  
- **Explicit songs** show slightly higher average streaming performance  
- Certain **BPM ranges (100–130)** dominate high-performing tracks  
- **Valence (happiness)** has a moderate positive relationship with streams  
- Popular songs are heavily concentrated in mainstream genres  

---

## What This Project Demonstrates

This project follows a layered analytics workflow:
- Data Layer → Raw and cleaned datasets
- Python Layer → Data cleaning and visualization
- SQL Layer → Analytical queries and aggregations
- Visualization Layer → Insights communicated through charts

---

## Project Structure 

```

Spotify-Analytics-Insight/
│
├── data/
│   ├── raw/
│   │   ├── spotify_alltime_top100_songs.csv
│   │   ├── spotify_wrapped_2025_top50_artists.csv
│   │   └── spotify_wrapped_2025_top50_songs.csv
│   │
│   └── processed/
│       └── cleaned_data.csv
│
├── notebooks/
│   └── spotify_analysis.ipynb
│
├── reports/
│   └── insights.md
│
├── sql/
│   └── analysis.sql
│
├── sql_outputs/
│   ├── bpm_performance.csv
│   ├── explicit_vs_streams.csv
│   ├── genre_distribution.csv
│   └── valence_vs_streams.csv
│
├── sql_visuals/
│   ├── sql_bpm_vs_streams.png
│   ├── sql_explicit_vs_streams.png
│   ├── sql_genre_distribution.png
│   └── sql_valence_vs_streams.png
│
├── src/
│   ├── data_cleaning.py
│   ├── analysis.py
│   └── sql_visuals.py
│
├── visuals/
│   ├── bpm_vs_streams.png
│   ├── explicit_vs_streams.png
│   ├── genre_distribution.png
│   └── valence_vs_streams.png
│
├── README.md
├── requirements.txt
└── .gitignore
```
---

## Installation & Setup

Clone the repository:

```
git clone
https://github.com/Nomusa990822/Spotify-Analytics-Insight.git
cd Spotify-Analytics-Insight
pip install -r requirements.txt
```
---

## How to Run

1. **Data Cleaning**
```
python src/data_cleaning.py
```
2. **Python Analysis & Visualizations**
```
python src/analysis.py
```
3. **SQL Analysis (SQLite)**
```
sqlite3 spotify.db
.mode csv
.import data/processed/cleaned_data.csv spotify_data
.read sql/analysis.sql
```
## Outputs

Clean dataset saved in ```data/processed/```
Visualizations saved in ```visuals/```

**SQL Analysis Outputs**

SQL queries were used to replicate and validate insights from Python analysis.
Outputs include:
- BPM performance analysis
- Explicit vs non-explicit comparison
- Genre distribution counts
- Valence vs streams aggregation

These results are stored in:
```
sql_outputs/
```

---

## Sample Visualizations

### BPM vs Streams
![BPM vs Streams](visuals/bpm_vs_streams.png)

_Mid-tempo songs tend to achieve higher streaming performance, suggesting an optimal BPM range for mainstream appeal._


### Explicit vs Clean Songs
![Explicit vs Streams](visuals/explicit_vs_streams.png)

_Explicit songs show slightly higher average streams, indicating a potential listener preference for unfiltered or expressive content._


### Genre Distribution
![Genre Distribution](visuals/genre_distribution.png)

_A few dominant genres account for most top-performing songs, highlighting the concentration of popularity within specific music categories._


### Valence vs Streams
![Valence vs Streams](visuals/valence_vs_streams.png)

_No strong correlation observed — both high and low valence songs can achieve high streaming performance._

---
## Key Takeaways

- Popularity is driven by a combination of features, not a single factor. 
- Mid-range BPM and higher energy levels tend to perform better  
- Explicit content may influence listener engagement  
- Emotional tone (valence) alone is not a strong predictor of success

---
## Dataset

**Spotify Wrapped 2025 Top Songs & Artists (Kaggle)**

Includes:
- Song metadata
- Audio features (BPM, energy, danceability, valence)
- Streaming performance metrics

---

## Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- SQLite

---

## Future Improvements
- Build an interactive dashboard (Power BI / Tableau)
- Develop a machine learning model for prediction

---
## Feedback & Contributions
Feedback, suggestions, and improvements are always welcome.
If you found this project useful or interesting, feel free to ⭐ the repository and share your thoughts!

---
## License 

This project is licensed under the MIT License.
