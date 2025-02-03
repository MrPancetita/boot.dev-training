SELECT user_id, max(amount) FROM transactions
WHERE was_successful = true AND
user_id = 4 AND
sender_id IS NOT NULL;