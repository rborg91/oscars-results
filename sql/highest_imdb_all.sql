SELECT oscars.Film, imdb.Rating
FROM best_pictures as oscars
LEFT JOIN imdb
	ON oscars.IMDBid = imdb.IMDBid
ORDER BY imdb.Rating DESC
LIMIT 1
