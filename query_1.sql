SELECT s.fullname, ROUND(AVG(r.rate),2) as avg_rate
FROM rates r 
LEFT JOIN students s ON s.id = r.student_id
GROUP BY s.id
ORDER BY avg_rate DESC
LIMIT 5;