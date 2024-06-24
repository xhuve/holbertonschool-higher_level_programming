-- show genre id

SELECT tv_shows.title AS title FROM tv_genres
	LEFT JOIN tv_show_genres
	ON tv_show_genres.genre_id = tv_genres.id
		LEFT JOIN tv_shows
		ON tv_shows.id = tv_show_genres.show_id
		WHERE tv_genres.name = 'Comedy'
		ORDER BY title;