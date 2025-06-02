SELECT
     imdb.Year
    ,oscar.Film
    ,imdb.Genres
    ,imdb.Rating
    ,imdb.Runtime
    ,imdb.Countries
FROM best_pictures AS oscar
LEFT JOIN imdb
ON oscar.IMDBid = imdb.IMDBid
WHERE oscar.Winner = 1;
