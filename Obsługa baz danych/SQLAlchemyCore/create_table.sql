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

INSERT INTO addresses (country, city, street, postal_code)
VALUES ('Poland', 'Warsaw', 'Aleje Jerozolimskie', '00-001'),
       ('Poland', 'Krakow', 'Rynek Glowny', '31-042'),
       ('Poland', 'Wroclaw', 'Rynek', '50-106'),
       ('Poland', 'Gdansk', 'Dlugi Targ', '80-831'),
       ('Poland', 'Poznan', 'Stary Rynek', '61-747'),
       ('Poland', 'Lodz', 'Piotrkowska', '90-001'),
       ('Poland', 'Szczecin', 'Plac Rodla', '70-419'),
       ('Poland', 'Bydgoszcz', 'Stary Rynek', '85-001'),
       ('Poland', 'Katowice', 'Rynek', '40-001'),
       ('Poland', 'Bialystok', 'Rynek Kosciuszki', '15-087'),
       ('Poland', 'Gdynia', 'Skwer Kosciuszki', '81-347'),
       ('Poland', 'Czestochowa', 'Aleja Najswietszej Marii Panny', '42-217'),
       ('Poland', 'Sosnowiec', 'ul. 3 Maja', '41-200'),
       ('Poland', 'Radom', 'Rynek', '26-600'),
       ('Poland', 'Kielce', 'Plac Moniuszki', '25-309'),
       ('Poland', 'Gliwice', 'Rynek', '44-100'),
       ('Poland', 'Torun', 'Rynek Staromiejski', '87-100'),
       ('Poland', 'Zabrze', 'Plac Teatralny', '41-800'),
       ('Poland', 'Olsztyn', 'Stare Miasto', '10-001'),
       ('Poland', 'Rzeszow', 'Rynek', '35-001');


-- Inserting employees with Polish names
INSERT INTO employees (pesel, first_name, last_name, birthday, address_id)
VALUES ('89040512345', 'Wojciech', 'Nowak', '1989-04-05', 1);
INSERT INTO employees (pesel, first_name, last_name, birthday, address_id)
VALUES ('80070298761', 'Anna', 'Kowalska', '1980-07-02', 2);
INSERT INTO employees (pesel, first_name, last_name, birthday, address_id)
VALUES ('92122176543', 'Piotr', 'Wójcik', '1992-12-21', 3);
INSERT INTO employees (pesel, first_name, last_name, birthday, address_id)
VALUES ('85110345213', 'Katarzyna', 'Wiśniewska', '1985-11-03', 4);
INSERT INTO employees (pesel, first_name, last_name, birthday, address_id)
VALUES ('90021578965', 'Marcin', 'Dąbrowski', '1990-02-15', 5);
INSERT INTO employees (pesel, first_name, last_name, birthday, address_id)
VALUES ('93101765432', 'Małgorzata', 'Lewandowska', '1993-10-17', 6);
INSERT INTO employees (pesel, first_name, last_name, birthday, address_id)
VALUES ('88062498765', 'Krzysztof', 'Wójcik', '1988-06-24', 7);
INSERT INTO employees (pesel, first_name, last_name, birthday, address_id)
VALUES ('91041054321', 'Barbara', 'Kamińska', '1991-04-10', 8);
INSERT INTO employees (pesel, first_name, last_name, birthday, address_id)
VALUES ('87031523456', 'Grzegorz', 'Kowalczyk', '1987-03-15', 9);
INSERT INTO employees (pesel, first_name, last_name, birthday, address_id)
VALUES ('84052087654', 'Krystyna', 'Zielińska', '1984-05-20', 10);
INSERT INTO employees (pesel, first_name, last_name, birthday, address_id)
VALUES ('95070131245', 'Tomasz', 'Szymański', '1995-07-01', 11);
INSERT INTO employees (pesel, first_name, last_name, birthday, address_id)
VALUES ('86082687654', 'Joanna', 'Woźniak', '1986-08-26', 12);
INSERT INTO employees (pesel, first_name, last_name, birthday, address_id)
VALUES ('92020212345', 'Andrzej', 'Jankowski', '1992-02-02', 13);
INSERT INTO employees (pesel, first_name, last_name, birthday, address_id)
VALUES ('89060478965', 'Zofia', 'Wójcik', '1989-06-04', 14);
INSERT INTO employees (pesel, first_name, last_name, birthday, address_id)
VALUES ('93071365432', 'Marek', 'Nowakowski', '1993-07-13', 15);
INSERT INTO employees (pesel, first_name, last_name, birthday, address_id)
VALUES ('90050254321', 'Ewa', 'Kaczmarek', '1990-05-02', 16);
INSERT INTO employees (pesel, first_name, last_name, birthday, address_id)
VALUES ('91071298765', 'Adam', 'Grabowski', '1991-07-12', 17);
INSERT INTO employees (pesel, first_name, last_name, birthday, address_id)
VALUES ('87090134567', 'Elżbieta', 'Pawlak', '1987-09-01', 18);
INSERT INTO employees (pesel, first_name, last_name, birthday, address_id)
VALUES ('94040387654', 'Jakub', 'Michalski', '1994-04-03', 19);
INSERT INTO employees (pesel, first_name, last_name, birthday, address_id)
VALUES ('92072412345', 'Natalia', 'Krupa', '1992-07-24', 20);
INSERT INTO employees (pesel, first_name, last_name, birthday)
VALUES ('92072412343', 'Marcin', 'Bułka', '1992-07-24');