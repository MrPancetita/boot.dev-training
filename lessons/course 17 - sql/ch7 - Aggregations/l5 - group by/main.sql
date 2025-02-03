SELECT user_id, sum(amount) AS balance
FROM transactions
GROUP BY user_id;