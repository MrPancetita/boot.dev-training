SELECT country_code, round(avg(age)) as average_age
FROM users
GROUP BY country_code;
