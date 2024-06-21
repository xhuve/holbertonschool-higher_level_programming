-- show genre id
USE hbtn_0d_tvshows;

SELECT tv_genres.name AS genre FROM tv_genres
	LEFT JOIN tv_show_genres
	ON tv_show_genres.genre_id = tv_genres.id
		LEFT JOIN tv_shows
		ON tv_shows.id = tv_show_genres.show_id
		WHERE tv_shows.title = 'Dexter'
		GROUP BY genre;