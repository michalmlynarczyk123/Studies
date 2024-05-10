--INNER
SELECT * FROM [user]
INNER JOIN ADRESS ON [user].user_id = ADRESS.user_id;

--LEFT
SELECT * FROM [user]
LEFT OUTER JOIN ADRESS ON [user].user_id = ADRESS.user_id;

--RIGHT
SELECT * FROM [user]
RIGHT OUTER JOIN ADRESS ON [user].user_id = ADRESS.user_id;

--FULL OUTER JOIN
SELECT * FROM [user]
FULL OUTER JOIN ADRESS ON [user].user_id = ADRESS.user_id;

--SUBQUERY
SELECT * FROM ADRESS WHERE user_id IN (
    SELECT user_id FROM [user] WHERE user_name LIKE 'J%'
    );