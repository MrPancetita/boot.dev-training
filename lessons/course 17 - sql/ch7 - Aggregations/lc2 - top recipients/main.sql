SELECT recipient_id, count(*) AS transactions_received
FROM transactions
WHERE was_successful = true
AND recipient_id IS NOT NULL
GROUP BY recipient_id
ORDER BY transactions_received DESC
LIMIT 2;