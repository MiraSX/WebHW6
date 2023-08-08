SELECT sb.name
FROM rates r
JOIN students s ON s.id = r.student_id
JOIN subjects sb ON sb.id = r.subject_id
WHERE r.rate not null AND s.id = 1
GROUP BY sb.name