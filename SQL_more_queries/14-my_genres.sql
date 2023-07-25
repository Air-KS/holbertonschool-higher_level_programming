-- MySQL server
-- List join Dexter
SELECT name FROM tv_shows
LEFT JOIN (tv_shows_genres, tv_genres)
ON (show_id = tv_shows.id AND genre_id = tv_genres.id)
WHERE title = "Dexter" 
ORDER BY name;
