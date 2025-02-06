SELECT * FROM transactions
WHERE user_id IN (
    SELECT id FROM users
    WHERE name='David'
);