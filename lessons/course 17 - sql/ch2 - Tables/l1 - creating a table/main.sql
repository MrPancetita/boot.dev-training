CREATE TABLE people(
    id INTEGER,
    tag TEXT,
    name TEXT,
    age INTEGER,
    balance INTEGER,
    is_admin BOOLEAN
);

-- TEST SUITE, DON'T TOUCH BELOW THIS LINE --

PRAGMA TABLE_INFO('people');
