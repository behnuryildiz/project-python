#! /bin/bash
CREATE DATABASE IF NOT EXISTS customer_data;
USE customer_data;

CREATE TABLE owners (
    owner_id int NOT NULL AUTO_INCREMENT,
    first_name varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    PRIMARY KEY (owner_id)
); 

CREATE TABLE pets (
    pet_id int NOT NULL AUTO_INCREMENT,
    fk_owned_by int,
    pet_name varchar(255) NOT NULL,
    species varchar(255) NOT NULL,
    PRIMARY KEY (pet_id),
    FOREIGN KEY (fk_owned_by) REFERENCES owners(owner_id)
); 
