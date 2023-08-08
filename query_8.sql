SELECT sb.name, ROUND(AVG(r.rate), 2)
FROM rates r
JOIN subjects sb ON sb.id = r.subject_id
WHERE r.subject_id IN (SELECT id FROM subjects WHERE teacher_id = 3)
GROUP BY r.subject_id, sb.name 
ORDER BY sb.name;