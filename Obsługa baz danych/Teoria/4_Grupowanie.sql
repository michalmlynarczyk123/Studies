USE AdventureWorks2014

--AGREGACJA
SELECT
    COUNT(*) AS [Liczba Produktów],
    COUNT(ProductSubcategoryID) AS [Sub Kategorie Liczba],
    AVG(ListPrice) AS [Średnia Cena]
FROM Production.Product


SELECT StoreID, COUNT(CustomerID) AS klienci
FROM Sales.Customer
WHERE StoreID IS NOT NULL
GROUP BY StoreID
HAVING COUNT(CustomerID) > 1
ORDER BY klienci


SELECT s.Name, COUNT(c.CustomerID) FROM Sales.Customer c
    INNER JOIN Sales.Store s ON c.StoreID = s.BusinessEntityID
    WHERE s.Name LIKE '%Action%'
GROUP BY s.Name
HAVING COUNT(c.CustomerID) > 1


