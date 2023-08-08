SELECT ROUND(AVG(r.rate), 2) as max_rate
FROM rates r
ORDER BY max_rate DESC


