CREATE TABLE posts (
    id INTEGER,
    image_url TEXT,
    description TEXT,
    author_id INTEGER,
    is_sponsored BOOLEAN
);

-- TEST SUITE, DON'T TOUCH BELOW THIS LINE --

PRAGMA TABLE_INFO('posts');
