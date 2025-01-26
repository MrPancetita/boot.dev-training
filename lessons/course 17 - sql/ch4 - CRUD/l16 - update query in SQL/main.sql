UPDATE users
  SET is_admin = TRUE
  WHERE id = 9;

-- TEST SUITE, DON'T TOUCH BELOW THIS LINE --

SELECT * FROM users;
