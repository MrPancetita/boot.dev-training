SELECT name, username FROM users
WHERE (username LIKE '%cashpal%' OR username LIKE '%support%')
AND is_admin = FALSE; 