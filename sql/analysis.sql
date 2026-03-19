-- =========================================
-- SPOTIFY ANALYTICS SQL QUERIES
-- =========================================

-- 1. Top 10 Most Streamed Songs
SELECT track_name, artist, streams
FROM spotify_data
ORDER BY  CAST(streams AS FLOAT) DESC
LIMIT 10;


-- 2. Average Streams: Explicit vs Clean Songs
SELECT explicit, AVG(CAST(streams AS FLOAT)) AS avg_streams
FROM spotify_data
GROUP BY explicit;


-- 3. BPM Range Analysis
SELECT bpm_range, 
        AVG(CAST(streams AS FLOAT)) AS avg_streams,
        COUNT(*) AS total_tracks
FROM spotify_data
GROUP BY bpm_range
ORDER BY total_tracks DESC;


-- 4. Genre Distribution (Top Genres)
SELECT primary_genre, COUNT(*) AS total_tracks
FROM spotify_data
GROUP BY primary_genre
ORDER BY total_tracks DESC;


-- 5. Correlation Insight (Valence vs Streams - grouped)
SELECT 
    ROUND(CAST(valence AS FLOAT), 1) AS valence_group,
    AVG(CAST(streams AS FLOAT)) AS avg_streams
FROM spotify_data
GROUP BY valence_group
ORDER BY valence_group;


-- 6. Energy vs Streams
SELECT 
    ROUND(CAST(energy AS FLOAT), 1) AS energy_group,
    AVG(CAST(streams AS FLOAT)) AS avg_streams
FROM spotify_data
GROUP BY energy_group
ORDER BY avg_streams DESC;


-- 7. Danceability vs Streams
SELECT 
    ROUND(CAST(danceability AS FLOAT), 1) AS dance_group,
    AVG(CAST(streams AS FLOAT)) AS avg_streams
FROM spotify_data
GROUP BY dance_group
ORDER BY avg_streams DESC;
