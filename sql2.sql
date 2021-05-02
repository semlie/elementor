SELECT prom_visitors.site, CAST(CAST(prom_visitors.number_of_visitors AS DECIMAL(9,2)) * 100/ total_visitors.total AS int) as perc
FROM
(SELECT sv.date, sv.site, sv.number_of_visitors
FROM site_visitors sv
JOIN promotion_dates pd
ON sv.site=pd.site
WHERE sv.date BETWEEN pd.start_date AND pd.end_date) prom_visitors
JOIN
(SELECT site, SUM(number_of_visitors) AS total
	FROM site_visitors
	GROUP BY site) total_visitors
ON prom_visitors.site = total_visitors.site

