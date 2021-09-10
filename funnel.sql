SELECT 	read_first.date, read_first.source, read_first.country,
	read_first.reads as firstimers,
	read_returning.user_id as returners,
	subscribers.user_id as subscribers,
	customer.user_id as customers
FROM
    -- FIRST READERS
    (SELECT DATE(my_datetime) as date, Source, country,
     count(distinct(user_id)) as reads
    FROM read_first
    GROUP BY date, Source, country) as read_first
    
LEFT JOIN
    -- RETURNING READERS
    (SELECT DATE(read_first.my_datetime) as date, read_first.Source, read_first.country, count(distinct(read_returning.user_id)) as user_id
    FROM read_returning 
    JOIN read_first 
    ON read_first.user_id = read_returning.user_id
    GROUP BY DATE(read_first.my_datetime), read_first.Source, read_first.country
    ORDER BY date) as read_returning
ON DATE(read_first.date) = DATE(read_returning.date) AND read_first.source = read_returning.source AND read_first.country = read_returning.country


LEFT JOIN
    -- SUBSCRIBERS
    (SELECT DATE(read_first.my_datetime) as date, read_first.Source, read_first.country, count(*) as user_id
    FROM subscribe
    JOIN read_first
    ON read_first.user_id = subscribe.user_id
    GROUP BY DATE(read_first.my_datetime), read_first.Source, read_first.country
    ORDER BY date) as subscribers
ON DATE(read_first.date) = DATE(subscribers.date) AND read_first.source = subscribers.source AND read_first.country = subscribers.country


LEFT JOIN 
    -- CUSTOMERS
    (SELECT DATE(read_first.my_datetime)as date, read_first.Source, read_first.country, count(DISTINCT(buy.user_id)) as user_id
    FROM buy
    JOIN read_first
    ON buy.user_id = read_first.user_id
    GROUP BY DATE(read_first.my_datetime), read_first.Source, read_first.country
    ORDER BY date) as customer
ON DATE(read_first.date) = DATE(customer.date) AND read_first.source = customer.source AND read_first.country = customer.country;