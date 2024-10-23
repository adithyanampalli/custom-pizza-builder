CREATE DATABASE PIZZA_ORDERS;

USE DATABASE PIZZA_ORDERS;
USE SCHEMA PUBLIC;

-- Table to store available pizza ingredients
CREATE TABLE PIZZA_OPTIONS (
    INGREDIENT_ID NUMBER,
    INGREDIENT_NAME STRING(50),
    INGREDIENT_TYPE STRING(20) -- Topping, Crust, or Size
);

-- Insert sample data
INSERT INTO PIZZA_OPTIONS (INGREDIENT_ID, INGREDIENT_NAME, INGREDIENT_TYPE)
VALUES
    (1, 'Pepperoni', 'Topping'),
    (2, 'Mushrooms', 'Topping'),
    (3, 'Onions', 'Topping'),
    (4, 'Cheese', 'Topping'),
    (5, 'Thin Crust', 'Crust'),
    (6, 'Thick Crust', 'Crust'),
    (7, 'Small', 'Size'),
    (8, 'Medium', 'Size'),
    (9, 'Large', 'Size');



 CREATE FILE FORMAT pizza_file_format
   TYPE = 'CSV'
   FIELD_DELIMITER = ','
   SKIP_HEADER = 1;
   

-- Table to store orders
CREATE TABLE PIZZA_ORDERS (
    ORDER_ID NUMBER AUTOINCREMENT,
    CUSTOMER_NAME STRING(100),
    INGREDIENTS STRING(500),
    SIZE STRING(10),
    CRUST STRING(20),
    ORDER_FILLED BOOLEAN DEFAULT FALSE
);
