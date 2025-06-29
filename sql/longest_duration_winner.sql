SELECT oscars.Film, CAST(imdb.Runtime AS NUMERIC) as Runtime,
	oscars.Ceremony, oscars.Year
FROM best_pictures as oscars
LEFT JOIN imdb
        ON oscars.IMDBid = imdb.IMDBid
WHERE Runtime IS NOT NULL
AND oscars.Winner = 1
ORDER BY Runtime DESC
LIMIT 1
