-- 코드를 입력하세요
SELECT T1.FLAVOR
FROM FIRST_HALF AS T1
INNER JOIN JULY AS T2
ON T1.FLAVOR = T2.FLAVOR
GROUP BY T1.FLAVOR
ORDER BY SUM(T1.TOTAL_ORDER + T2.TOTAL_ORDER) DESC
LIMIT 3;