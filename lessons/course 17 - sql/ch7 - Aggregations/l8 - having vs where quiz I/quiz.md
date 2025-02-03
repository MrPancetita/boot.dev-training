# Quiz

Q: In the example, should you use a WHERE or a HAVING clause to filter down to a specific class_id?

```sql
SELECT class_id, count(id) as class_size
FROM students
WHERE ...
GROUP BY class_id
HAVING ...
```

WHERE
HAVING

