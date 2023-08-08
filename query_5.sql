SELECT t.fullname, sb.name
FROM subjects sb
LEFT JOIN teachers t ON t.id = sb.teacher_id
WHERE t.id = 3