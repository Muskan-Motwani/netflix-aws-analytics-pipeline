-- Netflix Analytics Project — Athena SQL Queries
-- Database: netflix_db
-- Table: processed (created via AWS Glue Crawler on the S3 processed/ folder)


-- 1. Movies vs TV Shows count
SELECT type, COUNT(*) as total
FROM processed
GROUP BY type;


-- 2. Top 10 countries by number of titles
SELECT primary_country, COUNT(*) as total
FROM processed
GROUP BY primary_country
ORDER BY total DESC
LIMIT 10;


-- 3. Top 10 genres
SELECT primary_genre, COUNT(*) as total
FROM processed
GROUP BY primary_genre
ORDER BY total DESC
LIMIT 10;


-- 4. Content added by year
SELECT year_added, COUNT(*) as total
FROM processed
GROUP BY year_added
ORDER BY year_added;


-- 5. Rating distribution
SELECT rating, COUNT(*) as total
FROM processed
GROUP BY rating
ORDER BY total DESC;


-- 6. Top 10 directors
SELECT director, COUNT(*) as total
FROM processed
WHERE director != 'Not Given'
GROUP BY director
ORDER BY total DESC
LIMIT 10;


-- 7. Longest 10 movies
SELECT title, movie_duration_minutes
FROM processed
WHERE type = 'Movie'
ORDER BY movie_duration_minutes DESC
LIMIT 10;
