-- Individual counts for Winner and Nominee Only
SELECT
  CASE
    WHEN Winner = 1 THEN 'Winner'
    ELSE 'Nominee Only'
  END AS Winner_Category,
  COUNT(*) AS Count
FROM best_pictures
GROUP BY Winner

UNION ALL

-- Total count
SELECT
  'Total' AS Winner_Category,
  COUNT(*) AS Count
FROM best_pictures;
