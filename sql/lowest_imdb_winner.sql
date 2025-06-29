SELECT oscars.Film, imdb.Rating, oscars.Ceremony, oscars.Year
FROM best_pictures as oscars
LEFT JOIN imdb
        ON oscars.IMDBid = imdb.IMDBid
WHERE oscars.Winner = 1
ORDER BY imdb.Rating ASC
LIMIT 1
