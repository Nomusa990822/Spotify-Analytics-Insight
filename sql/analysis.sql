-- =========================================
-- SPOTIFY ANALYTICS SQL QUERIES
-- =========================================

-- 1. Top 10 Most Streamed Songs
SELECT track_name, artist_name, streams
FROM spotify_data
ORDER BY streams DESC
LIMIT 10;


-- 2. Average Streams: Explicit vs Clean Songs
SELECT explicit, AVG(streams) AS avg_streams
FROM spotify_data
GROUP BY explicit;


-- 3. BPM Range Analysis
SELECT 
    CASE 
        WHEN bpm < 90 THEN 'Slow (<90 BPM)'
        WHEN bpm BETWEEN 90 AND 110 THEN 'Mid-Tempo (90–110 BPM)'
        WHEN bpm BETWEEN 111 AND 130 THEN 'Optimal (111–130 BPM)'
        ELSE 'Fast (>130 BPM)'
    END AS bpm_category,
    AVG(streams) AS avg_streams
FROM spotify_data
GROUP BY bpm_category
ORDER BY avg_streams DESC;


-- 4. Genre Distribution (Top Genres)
SELECT track_genre, COUNT(*) AS total_tracks
FROM spotify_data
GROUP BY track_genre
ORDER BY total_tracks DESC;


-- 5. Correlation Insight (Valence vs Streams - grouped)
SELECT 
    ROUND(valence, 1) AS valence_group,
    AVG(streams) AS avg_streams
FROM spotify_data
GROUP BY valence_group
ORDER BY valence_group;


-- 6. Energy vs Streams
SELECT 
    ROUND(energy, 1) AS energy_group,
    AVG(streams) AS avg_streams
FROM spotify_data
GROUP BY energy_group
ORDER BY avg_streams DESC;


-- 7. Danceability vs Streams
SELECT 
    ROUND(danceability, 1) AS danceability_group,
    AVG(streams) AS avg_streams
FROM spotify_data
GROUP BY danceability_group
ORDER BY avg_streams DESC;
