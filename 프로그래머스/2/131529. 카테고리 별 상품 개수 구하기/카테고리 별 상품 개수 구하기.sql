SELECT LEFT(PRODUCT_CODE,2) AS CATEGORY,COUNT(LEFT(PRODUCT_CODE,2)) AS PRODUCT FROM PRODUCT
GROUP BY LEFT(PRODUCT_CODE,2);