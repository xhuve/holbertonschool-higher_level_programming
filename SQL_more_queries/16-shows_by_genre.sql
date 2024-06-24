-- show genre id

SELECT tv_shows.title AS title, tv_genres.name AS genre_name
FROM tv_shows
	LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
	LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
	ORDER BY tv_shows.title;