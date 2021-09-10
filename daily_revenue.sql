-- DAILY REVENUE
SELECT eight.date, eight.eightp as from_8, eighty.eightyp as from_80
FROM
	(SELECT DATE(my_datetime) as date, sum(price) as eightyp
	FROM buy
	where price = 80
	GROUP BY date
	ORDER BY date) as eighty
JOIN
	(SELECT DATE(my_datetime) as date, sum(price) as eightp
	FROM buy
	where price = 8
	GROUP BY date
	ORDER BY date) as eight
ON eighty.date = eight.date;
