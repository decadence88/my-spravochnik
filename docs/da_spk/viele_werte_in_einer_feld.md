# Viele Werte in einer Feld

```sql
SELECT unnest(
	string_to_array(name_von_Spalte, E'\n')
	) AS werten
FROM clients;
```