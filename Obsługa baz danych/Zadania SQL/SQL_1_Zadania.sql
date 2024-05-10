USE AdventureWorks2014
--1
SELECT * FROM Production.Product;
--2
SELECT ProductID, Name, ListPrice FROM Production.Product;
--3
SELECT ProductID, Name, ListPrice FROM Production.Product ORDER BY ListPrice DESC;
--4
SELECT Name, StandardCost, ListPrice FROM Production.Product WHERE ListPrice >= 500;
--5
SELECT Name, Color FROM Production.Product WHERE Color = 'Red' ORDER BY Name;
--6
SELECT FirstName, LastName, MiddleName FROM Person.Person ORDER BY LastName, FirstName;
--7
SELECT BusinessEntityID, HireDate, JobTitle FROM HumanResources.Employee
WHERE JobTitle like 'Sales Representative' ORDER BY BusinessEntityID, HireDate;
--8
SELECT Name, ListPrice FROM Production.Product WHERE ListPrice BETWEEN 500 AND 1000 ORDER BY ListPrice;
--9
SELECT Name, Color, Size FROM Production.Product WHERE Color like 'Black' AND Size like 'M';
--10
SELECT BusinessEntityID, HireDate FROM HumanResources.Employee
WHERE  HireDate >= '20100101' ORDER BY HireDate;
--11
SELECT * FROM Sales.SalesTerritory;
SELECT * FROM Sales.Customer WHERE TerritoryID  = 8 ORDER BY PersonID;
--12
SELECT * FROM Production.ProductCategory; /* 2 */
SELECT * FROM Production.ProductSubcategory WHERE ProductCategoryID = 2;
SELECT * FROM Production.Product
WHERE ProductSubcategoryID IN (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17) ORDER BY Name;
--13
SELECT * FROM HumanResources.Employee WHERE HireDate BETWEEN '20050101' AND '20061231' ORDER BY HireDate;
--14
SELECT * FROM Sales.SalesOrderDetail
SELECT * FROM Sales.Store
--15
SELECT * FROM Production.Product WHERE Name like '%bike%' ORDER BY Name ASC;