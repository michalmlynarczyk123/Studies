USE mimlynar
SELECT DB_NAME()

--tworzenie tabeli
CREATE TABLE customers(
    id int primary key,
    first_name varchar(100) NOT NULL,
    last_name varchar(100) NOT NULL,
    wrong_name date NOT NULL
)

SELECT * FROM   customers

--usuwanie tabeli
DROP TABLE customers

--zmiana tabeli
ALTER TABLE customers

--usuwanie kolumny
DROP COLUMN wrong_name

--dodanie kolumny
ALTER TABLE customers ADD birthday date

--zmiana tabeli tamto alter nie działa, złe
EXEC sp_rename 'customers.wrong_name', 'birthday', 'column'

INSERT INTO customers(id, first_name, last_name, wrong_name) values (1, 'Andrzej', 'Chudzicki', '2000-01-01')
INSERT INTO customers(id, first_name, last_name, wrong_name) values (2, 'Michal', 'Mlynarczyk', '2001-02-02')

--wszystko z tabeli
DELETE FROM customers
--pojedyncza rzecz
DELETE FROM customers WHERE id = 1
--również usuwanie
TRUNCATE TABLE customers

--------------------------------------------------------------------------------------------------------

CREATE TABLE customers(
    id int primary key,
    pesel VARCHAR(9),
    first_name varchar(100) NOT NULL,
    last_name varchar(100) NOT NULL,
    birthday date NOT NULL
)

SELECT * FROM customers

INSERT INTO customers(id, first_name, last_name, wrong_name) values (1, 'Andrzej', 'Chudzicki', '2000-01-01')

--TWORZENIE NOWEGO SCHEMA
CREATE SCHEMA nowySchemat

CREATE TABLE nowySchemat.customers(
    id int primary key,
    pesel VARCHAR(9),
    first_name varchar(100) NOT NULL,
    last_name varchar(100) NOT NULL,
    birthday date NOT NULL
)

SELECT SCHEMA_NAME()

--------------------------------------------------------------------------------------------------------

CREATE TABLE customers(
    id int identity primary key,
    first_name varchar(100) NOT NULL,
    last_name varchar(100) NOT NULL,
    birthday date NOT NULL
)

CREATE TABLE orders(
    id int identity primary key,
    order_date date,
    customer_id int
)

SELECt * FROM customers
SELECt * FROM orders

INSERT INTO customers(first_name, last_name, wrong_name)
VALUES ('Andrzej', 'Chudzicki', '2000-01-01')

INSERT INTO orders(order_date, customer_id)
VALUES ('2024-01-01', 1)

INSERT INTO orders(order_date, customer_id)
VALUES (GETDATE(), 2)

DROP TABLE orders

CREATE TABLE orders(
    id int identity primary key,
    order_date date,
    customer_id int foreign key references customers(id)
)

--------------------------------------------------------------------------------------------------------

CREATE TABLE orders(
    id int identity primary key,
    order_date date,
    customer_id int
)

ALTER TABLE orders
ADD CONSTRAINT FK_Orders_Customers_ID FOREIGN KEY(customer_id)
REFERENCES customers(ID)

ALTER TABLE orders DROP CONSTRAINT FK_Orders_Customers_ID

ALTER TABLE orders
ADD CONSTRAINT FK_Orders_Customers_ID FOREIGN KEY(customer_id)REFERENCES customers(ID) ON DELETE CASCADE

DELETE FROM customers

SELECT * FROM customers
SELECT * FROM orders

INSERT INTO customers(first_name, last_name, birthday)
VALUES ('Andrzej', 'Chudzicki', '2000-01-01')

INSERT INTO orders(order_date, customer_id)
VALUES ('2024-01-01', 1)

DROP TABLE orders

--------------------------------------------------------------------------------------------------------

CREATE TABLE orders(
    id int identity primary key,
    order_date date DEFAULT GETDATE(),
    customer_id int FOREIGN KEY REFERENCES customers(id)
)

INSERT INTO customers(first_name, last_name, birthday)
VALUES ('Andrzej', 'Chudzicki', '2000-01-01')

INSERT INTO orders(order_date, customer_id)
VALUES ('2024-01-01', 3)

INSERT INTO orders(order_date, customer_id) VALUES (DEFAULT, 3)

--------------------------------------------------------------------------------------------------------

CREATE TABLE orders(
    id int identity primary key,
    order_date date,
    customer_id int FOREIGN KEY REFERENCES customers(id)
)

ALTER TABLE orders
ADD CONSTRAINT DF_OrderDate DEFAULT GETDATE() FOR order_date

INSERT INTO orders(order_date, customer_id) VALUES ('2021-01-01', 3), (DEFAULT, 3), ('2024-05-05', 3)

--------------------------------------------------------------------------------------------------------

CREATE TABLE employees(
    id int identity primary key,
    age int check (age BETWEEN 18 and 65)
)

CREATE TABLE students(
    id int identity primary key,
    grade char(1) check (grade in ('A', 'B', 'C', 'D', 'F'))
)

INSERT INTO employees(age) VALUES (20)
INSERT INTO employees(age) VALUES (15)

INSERT INTO students(grade) VALUES ('A')
INSERT INTO students(grade) VALUES ('Z')