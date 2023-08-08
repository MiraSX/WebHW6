SELECT sb.name, ROUND(AVG(r.rate),2) as max_rate, s.fullname
FROM rates r
LEFT JOIN subjects sb ON sb.id = r.subject_id
LEFT JOIN students s ON s.id = r.student_id 
WHERE sb.id = 4
GROUP BY s.id
ORDER BY max_rate DESC
LIMIT 1
