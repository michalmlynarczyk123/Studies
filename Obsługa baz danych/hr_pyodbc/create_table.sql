CREATE TABLE addresses
(
    address_id  INT PRIMARY KEY IDENTITY,
    country     VARCHAR(255) NOT NULL,
    city        VARCHAR(255) NOT NULL,
    street      VARCHAR(255) NOT NULL,
    postal_code VARCHAR(25)  NOT NULL
);

CREATE TABLE employees
(
    pesel      VARCHAR(11) PRIMARY KEY NOT NULL,
    first_name VARCHAR(255)            NOT NULL,
    last_name  VARCHAR(255)            NOT NULL,
    birthday   DATE                    NOT NULL CHECK (birthday < GETDATE()),
    address_id INT FOREIGN KEY REFERENCES addresses (address_id)
);