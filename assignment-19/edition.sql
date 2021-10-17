-- Customers validate
INSERT INTO Customers(ID,Name,City,Country)
VALUES(1,'Mahdis','Tehran','Iran');

INSERT INTO Customers(ID,Name,City,Country)
VALUES(2,'Sara','Paris','France');

INSERT INTO Customers(ID,Name,City,Country)
VALUES(3,'Andy','New York','America');

-- Products validate
INSERT INTO Products(ID,Name,Price,Count1)
VALUES(12,'Milk',12.500,5);

INSERT INTO Products(ID,Name,Price,Count1)
VALUES(13,'chocolate',25000,12);

INSERT INTO Products(ID,Name,Price)
VALUES(13,'Apple',5500);

-- Only show existing Products 
SELECT ID,Name,Price
FROM Products
WHERE Count1 != 0;

-- DELETE Customers who aren't Iranian
DELETE FROM Customers WHERE Country != 'Iran';

-- Update the prices
UPDATE Products
SET Price = Price + ((Price *20)/100)