USE AdventureWorks2014;

SELECT *
FROM Production.Product
INNER JOIN Production.ProductSubcategory
ON Production.Product.ProductSubcategoryID = Production.Product.ProductSubcategoryID;


--INNER
SELECT
    Production.Product.Name AS Produkt,
    Production.ProductSubcategory.Name AS [Sub Kategoria],
    Production.ProductCategory.Name AS Kategoria
FROM Production.Product
    INNER JOIN Production.ProductSubcategory
        ON Production.Product.ProductSubcategoryID = Production.ProductSubcategory.ProductSubcategoryID
    INNER JOIN Production.ProductCategory
        ON Production.ProductSubcategory.ProductSubcategoryID = Production.ProductCategory.ProductCategoryID;


--INNER Z ALIASAMI ORAZ SKRÓCONA WERJSA INNERA
SELECT
    product.Name AS Produkt,
    sub.Name AS [Sub Kategoria],
    cat.Name AS Kategoria
FROM Production.Product AS product
    JOIN Production.ProductSubcategory AS sub
        ON product.ProductSubcategoryID = sub.ProductSubcategoryID
    JOIN Production.ProductCategory AS cat
        ON sub.ProductSubcategoryID = cat.ProductCategoryID
WHERE cat.Name = 'Components'
ORDER BY sub.Name DESC;

--LEFT JOIN
SELECT p.FirstName + ' ' + p.LastName AS Imię, c.CustomerID, oh.SalesOrderID
FROM Sales.Customer AS c
    JOIN  Sales.SalesOrderHeader AS oh ON c.CustomerID = oh.CustomerID
    JOIN Person.Person AS p ON c.PersonID = p.BusinessEntityID
ORDER BY c.CustomerID

--SUBQUERY
SELECT DISTINCT Name FROM Production.Product
WHERE ProductID IN (
    SELECT ProductID FROM Sales.SalesOrderDetail
                WHERE OrderQty >= 20
    )
ORDER BY Name

--to samo ale joinem
SELECT DISTINCT Name FROM Production.Product AS p
    JOIN Sales.SalesOrderDetail AS od
    ON p.ProductID = od.ProductID
WHERE od.OrderQty >= 20
ORDER BY Name