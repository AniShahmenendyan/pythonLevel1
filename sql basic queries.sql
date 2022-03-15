CREATE DATABASE python_level1;

CREATE TABLE users
(
    id        SERIAL PRIMARY KEY,
    firstname text,
    lastname  text,
    age       int
);

INSERT INTO users (firstname, lastname, age) VALUES ('Felix', 'Kocharyan', 31);

INSERT INTO users (firstname, lastname) VALUES ('Davit', 'Melikyan');

ALTER TABLE users ADD COLUMN email text;

UPDATE users SET email = 'f@gmail.com' WHERE id = 1 OR id = 2;

UPDATE users SET email = 'd@gmail.com' WHERE id = 2;

SELECT id, firstname, lastname, age, email FROM users LIMIT 1 OFFSET 1;

ALTER TABLE users ADD CONSTRAINT constraintname UNIQUE (email);

INSERT INTO users (firstname, lastname, email) VALUES ('Davit', 'Melik', 'd1@gmail.com');

UPDATE users set age = 31 where firstname = 'Davit';

SELECT firstname, lastname, email FROM users WHERE firstname = 'Davit';

SELECT firstname, lastname, email FROM users WHERE lastname = 'Melik';

SELECT firstname, lastname, email FROM users WHERE lastname LIKE '%k%';


SELECT firstname, lastname, email FROM users WHERE (lastname = 'Melik' or lastname = 'Melikyan') and age = 31;

INSERT INTO users (firstname, lastname, email) VALUES ('Edgar', 'Budaghyan', 'e@gmail.com');

SELECT firstname, lastname, email, age FROM users WHERE age IS NULL;

SELECT firstname, lastname, email, age FROM users WHERE age IS NOT NULL;

SELECT firstname, lastname, email, age FROM users ORDER BY age DESC;

SELECT count(*) as count_of_users from users;

SELECT MIN(age) from users;

SELECT MAX(age) from users;

SELECT AVG(age) from users;

SELECT SUM(age) from users;

SELECT firstname as first_name, lastname as last_name, email, age FROM users;

SELECT u.firstname , u.lastname, u.email, u.age FROM users as u;


SELECT firstname, lastname, email, age FROM users WHERE age in (31, 32, 33, 34);

SELECT firstname, lastname, email, age FROM users WHERE age BETWEEN 31 and  34;

CREATE TABLE images
(
    user_id   int,
    image_url text not null,
    FOREIGN KEY (user_id) REFERENCES users (id)
);

INSERT INTO images (user_id, image_url) VALUES (1, 'felix.jpg');

SELECT u.firstname, u.lastname, i.image_url FROM users u LEFT JOIN images i on u.id = i.user_id
WHERE i.image_url like '%.jbg';

DELETE from images where image_url like '%.jbg';

ALTER TABLE images ADD COLUMN created_at TIMESTAMP default NOW();

INSERT INTO images (user_id, image_url) VALUES (2, 'davit.jpg');