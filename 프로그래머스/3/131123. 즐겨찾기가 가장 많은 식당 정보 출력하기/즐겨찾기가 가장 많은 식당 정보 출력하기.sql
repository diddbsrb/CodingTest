WITH RAW AS(
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES,
ROW_NUMBER() OVER(PARTITION BY FOOD_TYPE ORDER BY FAVORITES DESC) AS RANKING
FROM REST_INFO)
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES FROM RAW
WHERE RANKING=1
ORDER BY FOOD_TYPE DESC;