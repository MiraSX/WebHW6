SELECT sb.name
FROM rates r
JOIN students s ON s.id = r.student_id
JOIN subjects sb ON sb.id = r.subject_id
JOIN teachers t ON t.id = sb.teacher_id
WHERE t.id = 1 AND s.id = 2
GROUP BY sb.name
