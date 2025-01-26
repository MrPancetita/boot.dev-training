SELECT *,
  IIF(was_successful = TRUE, 'No action required', 'Perform an audit') AS audit
  FROM transactions;