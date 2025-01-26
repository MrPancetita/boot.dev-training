INSERT INTO users(name, age, country_code, username, password, is_admin)
  VALUES('Lance', 20, 'US', 'LanChr', 'bootdevisbest', FALSE);

INSERT INTO users(name, age, country_code, username, password, is_admin)
  VALUES('Tiffany', 28, 'US', 'Tifferoon', 'autoincrement', TRUE);

-- TEST SUITE, DON'T TOUCH BELOW THIS LINE --

SELECT * FROM users;