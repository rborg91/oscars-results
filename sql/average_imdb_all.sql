SELECT oscars.Winner,
	CASE
		WHEN oscars.Winner = 1 THEN 'Winner'
  	ELSE 'Nominee Only'
  END AS Winner_Category,
  ROUND(AVG(imdb.Rating), 1)
FROM best_pictures as oscars
LEFT JOIN imdb
	ON oscars.IMDBid = imdb.IMDBid
GROUP BY oscars.Winner
