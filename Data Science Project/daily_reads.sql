-- DAILY READS

SELECT first_and_returning.date, first_and_returning.country, count(distinct(first_and_returning.user_id)) as user_id
FROM (SELECT DATE(my_datetime) as date, country, user_id FROM read_first
      UNION ALL
      SELECT DATE(my_datetime) as date, country, user_id FROM read_returning) as first_and_returning
GROUP BY first_and_returning.date, first_and_returning.country
ORDER BY first_and_returning.date;