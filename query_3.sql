SELECT g.name, ROUND(AVG(r.rate), 2) as max_rate
FROM rates r
LEFT JOIN subjects sb ON sb.id = r.subject_id
LEFT JOIN students s ON s.id = r.student_id
LEFT JOIN groups g ON g.id = s.group_id
WHERE sb.id = 4
GROUP BY g.name
ORDER BY max_rate DESC


