# Quiz

Q: In the example, should you use a WHERE or a HAVING clause to filter down classes of a particular size?

```sql
SELECT class_id, count(id) as class_size
FROM students
WHERE ...
GROUP BY class_id
HAVING ...
```

WHERE
HAVING
