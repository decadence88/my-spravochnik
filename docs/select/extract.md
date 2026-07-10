# EXTRACT

```sql
EXTRACT(часть_даты FROM дата_или_время)

Части даты/времени:

YEAR    – год
MONTH   – месяц
DAY     – день
HOUR    – час
MINUTE  – минута
SECOND  – секунда

::date / ::time/ ::text - во что превратить значение по итогу

Примеры:

-- Получить год из даты
SELECT EXTRACT(YEAR FROM '2026-02-23'::date);

-- Можно использовать с CURRENT_DATE / _TIMESTAMP

SELECT EXTRACT(YEAR FROM CURRENT_DATE);
SELECT EXTRACT(HOUR FROM CURRENT_TIMESTAMP)

--Математика, сравнения, агрегаты и т.д.
SELECT EXTRACT(YEAR FROM '2026-02-23') + 1; -- 2027
```