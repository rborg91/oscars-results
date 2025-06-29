SELECT oscars.Winner,
        CASE
                WHEN oscars.Winner = 1 THEN 'Winner'
        ELSE 'Nominee Only'
  END AS Winner_Category,
ROUND(AVG(CAST(imdb.Runtime AS NUMERIC)), 1) as Avg_Runtime
FROM best_pictures as oscars
LEFT JOIN imdb
        ON oscars.IMDBid = imdb.IMDBid
WHERE Runtime IS NOT NULL
GROUP BY oscars.Winner
