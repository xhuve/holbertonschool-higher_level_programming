-- show genre id

SELECT tv_shows.title AS title, tv_genres.name 
FROM tv_genres
	LEFT JOIN tv_show_genres
	ON tv_show_genres.genre_id = tv_genres.id
		LEFT JOIN tv_shows
		ON tv_shows.id = tv_show_genres.show_id
		ORDER BY title
		GROUP BY title;