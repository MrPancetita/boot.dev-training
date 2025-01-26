SELECT *, 
  IIF ( age > 55 OR country_code = 'CA',TRUE,FALSE) AS discount_eligible
FROM users;