-- Import the database dump of hbtn_0d_tvshows to your MySQL server: download
SELECT tvs.title, tvsg.genre_id FROM tv_shows AS tvs LEFT JOIN tv_show_genres AS tvsg ON tvs.id=tvsg.show_id ORDER BY tvs.title, tvsg.genre_id ASC;