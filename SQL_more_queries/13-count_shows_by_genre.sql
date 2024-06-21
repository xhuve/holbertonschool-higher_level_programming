-- show genre id
USE hbtn_0d_tvshows;

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows FROM tv_genres
    LEFT JOIN tv_show_genres
    ON tv_show_genres.show_id = tv_genres.id
    GROUP BY genre
    HAVING number_of_shows > 0
    ORDER BY number_of_shows DESC;