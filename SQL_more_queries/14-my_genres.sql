-- MySQL server
-- List join Dexter
SELECT tv_genres.name 
FROM tv_shows
    LEFT JOIN tv_shows_genres
        ON tv_shows.id = tv_shows_genre.show_id
    LEFT JOIN tv_genre
        ON tv_shows_genre.genre_id = tv_genres.id
WHERE tv_shows.title = "Dexter" 
ORDER BY tv_genre.name;
