SELECT oscars.Film, imdb.Rating
FROM best_pictures as oscars
LEFT JOIN imdb
        ON oscars.IMDBid = imdb.IMDBid
WHERE imdb.Rating IS NOT NULL
ORDER BY imdb.Rating ASC
LIMIT 1
