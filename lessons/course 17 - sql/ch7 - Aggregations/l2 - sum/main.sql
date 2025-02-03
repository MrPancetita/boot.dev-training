SELECT sum(amount) FROM transactions
WHERE was_successful = true AND
user_id = 9;