import pandas as pd
import matplotlib.pyplot as plt
import os

# Create folder
os.makedirs("sql_visuals", exist_ok=True)

# 1. Explicit vs Streams
df = pd.read_csv("sql_outputs/explicit_vs_streams.csv")
df.plot(x="explicit", y="avg_streams", kind="bar")
plt.title("SQL: Explicit vs Streams")
plt.savefig("sql_visuals/sql_explicit_vs_streams.png")
plt.clf()

# 2. Genre Distribution
df = pd.read_csv("sql_outputs/genre_distribution.csv")
df = df.sort_values(by="total_tracks", ascending=False).head(10)
df.plot(x="primary_genre", y="total_tracks", kind="bar")
plt.title("SQL: Genre Distribution (Top 10)")
plt.savefig("sql_visuals/sql_genre_distribution.png")
plt.clf()

# 3. BPM Performance
df = pd.read_csv("sql_outputs/bpm_performance.csv")
df.plot(x="bpm_range", y="avg_streams", kind="bar")
plt.title("SQL: BPM vs Streams")
plt.savefig("sql_visuals/sql_bpm_vs_streams.png")
plt.clf()

# 4. Valence vs Streams
df = pd.read_csv("sql_outputs/valence_vs_streams.csv")
df.plot(x="valence_group", y="avg_streams", kind="line")
plt.title("SQL: Valence vs Streams")
plt.savefig("sql_visuals/sql_valence_vs_streams.png")
plt.clf()

print("✅ SQL visuals created successfully!")