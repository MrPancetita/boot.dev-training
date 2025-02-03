SELECT sender_id, sum(amount) as balance 
FROM transactions
WHERE sender_id IS NOT NULL
AND note like '%lunch%'
GROUP BY sender_id
HAVING balance > 20;