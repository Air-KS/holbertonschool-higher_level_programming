-- MySQL server
-- List join Dexter
SELECT tv_genres.name 
FROM tv_genres
    LEFT JOIN tv_shows_genres
        ON tv_genres.id = tv_shows_genre.genre.id
    LEFT JOIN tv_shows
        ON tv_shows_genres.show_id = tv_shows.id
WHERE tv_shows.title = "Dexter" 
ORDER BY tv_genres.name ASC ;