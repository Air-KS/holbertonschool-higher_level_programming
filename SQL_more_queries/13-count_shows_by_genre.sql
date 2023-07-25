-- MySQL server
-- List all genre from tv_shows with number
SELECT name AS genre,
       COUNT(genre_id) AS number_of_shows
FROM tv_genre 
    JOIN tv_show_genres 
        ON id = genres.id
GROUP BY genre_id
ORDER BY number_of_shows DESC;