-- MySQL server
-- List all genre from tv_shows with number
SELECT tv_genre.name AS genre,
       COUNT(*) AS number_of_shows
FROM tv_genre 
    JOIN tv_show_genres 
        ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show.name
ORDER BY number_of_shows DESC;

