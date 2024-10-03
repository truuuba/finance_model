CREATE DATABASE FM_model;

USE FM_model;

CREATE TABLE company(
    ID INT NOT NULL PRIMARY KEY,
    nazv CHAR(100) NOT NULL
);

CREATE TABLE employe(
    ID INT NOT NULL PRIMARY KEY,
    Id_c INT NOT NULL,
    fam CHAR(50) NOT NULL,
    imya CHAR(50) NOT NULL,
    otch CHAR(50),
    log_ CHAR(30) NOT NULL,
    pas_ CHAR(30) NOT NULL,
    FOREIGN KEY (Id_c) REFERENCES company (ID)
    ON UPDATE CASCADE
);

CREATE TABLE administ(
    ID INT NOT NULL PRIMARY KEY,
    Id_k INT NOT NULL,
    fam CHAR(50) NOT NULL,
    imya CHAR(50) NOT NULL,
    otch CHAR(50),
    log_ CHAR(30) NOT NULL,
    pas_ CHAR(30) NOT NULL,
    FOREIGN KEY (Id_k) REFERENCES company (ID)
    ON UPDATE CASCADE
);

CREATE TABLE project(
    ID INT NOT NULL PRIMARY KEY,
    Id_c INT NOT NULL,
    nazv CHAR(50) NOT NULL,
    mount_w CHAR(30),
    yr_w INT,
    prod INT,
    mount_pr CHAR(30),
    yr_pr INT,
    dohod DECIMAL(16, 2),
    FOREIGN KEY (Id_c) REFERENCES company (ID)
    ON UPDATE CASCADE
);

CREATE TABLE stati(
    ID INT NOT NULL PRIMARY KEY,
    Id_p INT NOT NULL,
    d_r CHAR(30),
    nazv CHAR(200),
    FOREIGN KEY (Id_p) REFERENCES project (ID)
    ON UPDATE CASCADE
);

CREATE TABLE GPR(
    ID INT NOT NULL PRIMARY KEY,
    Id_st INT NOT NULL,
    Prodolj INT,
    Zavisim CHAR(100),
    FOREIGN KEY (Id_st) REFERENCES stati (ID)
    ON UPDATE CASCADE
);

CREATE TABLE PPO(
    ID INT NOT NULL PRIMARY KEY,
    Id_st INT NOT NULL,
    Prod_pl DECIMAL(16, 2) NOT NULL,
    Stoim DECIMAL(16, 2) NOT NULL,
    Kv_cnt INT NOT NULL,
    FOREIGN KEY (Id_st) REFERENCES stati (ID)
    ON UPDATE CASCADE
);

CREATE TABLE BDR_r(
    ID INT PRIMARY KEY NOT NULL,
    Id_st INT NOT NULL,
    mnt CHAR(30),
    yr INT,
    trati DECIMAL(16, 2),
    FOREIGN KEY (Id_st) REFERENCES stati (ID)
);

CREATE TABLE BDR_d(
    ID INT PRIMARY KEY NOT NULL,
    Id_st INT NOT NULL,
    mnt CHAR(30),
    yr INT,
    dohodi DECIMAL(18, 2),
    FOREIGN KEY (Id_st) REFERENCES stati (ID)
);

INSERT INTO company (ID, nazv) VALUES (1, 'Аура');
INSERT INTO company (ID, nazv) VALUES (2, 'Иволга');

INSERT INTO administ (ID, Id_k, fam, imya, otch, log_, pas_) VALUES (1, 1, 'Иванов', 'Иван', 'Иванович', 'ivanov.ii', 'pass69#');
INSERT INTO administ (ID, Id_k, fam, imya, otch, log_, pas_) VALUES (2, 1, 'Степанов', 'Степан', 'Степанович', 'stepanov.ss', 'pass70!');
INSERT INTO administ (ID, Id_k, fam, imya, otch, log_, pas_) VALUES (3, 2, 'Валерьев', 'Валерий', 'Валерьевич', 'valeriev.vv', 'pass15#');
INSERT INTO administ (ID, Id_k, fam, imya, otch, log_, pas_) VALUES (4, 2, 'Полупанов', 'Дмитрий', 'Сергеевич', 'polupanov.ds', 'pass43?');

INSERT INTO employe (ID, Id_c, fam, imya, otch, log_, pas_) VALUES (1, 1, 'Хохлов', 'Тимофей', 'Алексеевич', 'hohlov.ta', 'pass24#');
INSERT INTO employe (ID, Id_c, fam, imya, otch, log_, pas_) VALUES (2, 2, 'Марковчина', 'Мария', 'Александровна', 'markovchina.ma', 'pass82!');

INSERT INTO project (ID, Id_c, nazv, mount_w, yr_w, prod, mount_pr, yr_pr, dohod) VALUES (1, 1, 'Test', 'Январь', 2024, 15, 'Февраль', 2025);
INSERT INTO project (ID, Id_c, nazv, mount_w, yr_w, prod, mount_pr, yr_pr, dohod) VALUES (2, 2, 'Tester', 'Январь', 2024, 15, 'Февраль', 2025);

SELECT project.nazv FROM project INNER JOIN company ON project.Id_c = company.ID WHERE company.nazv = '';

SELECT Zavisim FROM GPR WHERE ID_st = '';

SELECT mount_w FROM project WHERE ID = '';

SELECT project.ID FROM project
INNER JOIN company ON project.Id_c = company.ID
WHERE company.nazv = '' AND project.nazv = '';

UPDATE project SET prod = '' WHERE ID = ''; 

SELECT Prod_pl FROM PPO WHERE Id_st = '';

DELETE FROM '';

UPDATE BDR_r SET trati = '' WHERE ID = '';
