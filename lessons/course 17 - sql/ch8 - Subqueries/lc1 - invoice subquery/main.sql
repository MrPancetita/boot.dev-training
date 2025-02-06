SELECT * FROM users
WHERE is_admin IS false
AND id IN (
    SELECT user_id FROM transactions
    WHERE note LIKE '%invoice%' OR
    note LIKE '%tax%'
);