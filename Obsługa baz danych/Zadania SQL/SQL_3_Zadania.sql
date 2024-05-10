USE AdventureWorks2014;

--1
SELECT CustomerID, COUNT(*) AS CountORders
FROM Sales.SalesOrderHeader
GROUP BY CustomerID

--2
SELECT
    DISTINCT(JobTitle),
    AVG(eph.Rate)
FROM HumanResources.Employee AS re
JOIN humanresources.employeepayhistory AS eph
ON re.BusinessEntityID = eph.Rate
GROUP BY JobTitle

--3
SELECT
    p.FirstName +' '+ p.LastName AS Name,
    soh.CustomerID,
    COUNT(soh.SalesOrderID)
FROM Sales.SalesOrderHeader AS soh
JOIN Sales.Customer AS c
ON soh.CustomerID = c.CustomerID
JOIN Person.Person AS p
ON c.PersonID = p.BusinessEntityID
WHERE OrderDate BETWEEN '20130101' AND '20131231'
GROUP BY p.FirstName +' '+ p.LastName, soh.CustomerID

--4
SELECT COUNT(LineTotal) AS LineTotal, ProductID FROM Sales.SalesOrderDetail
GROUP BY ProductID

--5
SELECT
    p.LastName +' '+ p.LastName,
    AVG(SubTotal) AS AVG
FROM Sales.SalesOrderHeader AS soh
JOIN Sales.Customer AS c
ON soh.CustomerID = c.CustomerID
JOIN Person.Person AS p
ON c.PersonID = p.BusinessEntityID
GROUP BY p.LastName +' '+ p.LastName

--6
SELECT
    p.Name,
    COUNT(p.ProductID) AS CountNum
FROM Production.Product AS p
JOIN Sales.SalesOrderDetail AS sod
ON p.ProductID = sod.ProductID
GROUP BY p.Name
ORDER BY CountNum DESC

--7
SELECT
    st.Name AS Teritory,
    AVG(SubTotal) AS Total
FROM Sales.SalesOrderHeader AS soh
JOIN Sales.Customer AS c
ON c.TerritoryID = soh.TerritoryID
JOIN Sales.SalesTerritory AS st
ON soh.TerritoryID = st.TerritoryID
GROUP BY st.Name

--8