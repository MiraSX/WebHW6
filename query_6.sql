SELECT s.fullname
FROM students s 
LEFT JOIN groups g ON g.id = s.group_id
WHERE g.id = 1
