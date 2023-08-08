SELECT r.rate
FROM rates r 
LEFT JOIN subjects sb ON sb.id = r.subject_id
LEFT JOIN students s ON s.id = r.student_id
LEFT JOIN groups g ON g.id = s.group_id
WHERE sb.id = 2