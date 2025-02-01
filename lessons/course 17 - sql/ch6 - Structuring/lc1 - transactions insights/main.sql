SELECT recipient_id, amount, note FROM transactions
    WHERE was_successful = true
    ORDER BY amount DESC
    LIMIT 5;