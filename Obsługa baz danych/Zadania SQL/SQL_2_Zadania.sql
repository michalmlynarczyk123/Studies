USE AdventureWorks2014;

--1
SELECT
    p.Name AS name,
    p.StandardCost AS prize,
    pc.Name AS category
FROM Production.Product AS p
JOIN Production.ProductCategory AS pc
ON p.ProductSubcategoryID = pc.ProductCategoryID

--2
SELECT
    p.FirstName AS [first name],
    p.LastName AS [last name],
    em.EmailAddress AS [email address],
    hr.Name AS [department name]
FROM Person.Person AS p
JOIN Person.EmailAddress AS em
ON p.BusinessEntityID = em.BusinessEntityID
JOIN HumanResources.Department AS hr
ON p.BusinessEntityID = hr.DepartmentID
ORDER BY p.FirstName

--3
SELECT
    p.FirstName AS [first name],
    p.LastName AS [last name],
    soh.TotalDue AS [total due],
    st.Name AS [teritory name]
FROM Person.Person AS p
JOIN Sales.SalesOrderHeader AS soh
ON p.BusinessEntityID = soh.CustomerID
JOIN Sales.SalesTerritory AS st
ON st.TerritoryID = soh.TerritoryID

--4
SELECT
    c.CustomerID AS [customerID],
    soh.SalesOrderID AS [orderID]
FROM Sales.Customer AS c
JOIN Sales.SalesOrderHeader AS soh
ON c.CustomerID = soh.CustomerID

--5
SELECT
    sc.CustomerID AS [customerID],
    p.FirstName AS [first name],
    p.LastName AS [last name],
    em.EmailAddress AS [email address]
FROM Person.Person AS p
JOIN Person.EmailAddress AS em
ON p.BusinessEntityID = em.BusinessEntityID
JOIN Sales.Customer AS sc
ON p.BusinessEntityID = sc.CustomerID

--6
SELECT
    sc.CustomerID AS [Customer ID],
    soh.SalesOrderID AS [Order ID],
    pa.AddressLine1 AS [Address]
FROM Sales.Customer AS sc
JOIN sales.SalesOrderHeader AS soh
ON sc.CustomerID = soh.CustomerID
JOIN Person.Address AS pa
ON sc.TerritoryID = pa.StateProvinceID

---7
SELECT
    p.FirstName +' '+ p.LastName AS [name],
    hr.Name AS [department name],
    hre.HireDate AS [Hire Date]
FROM Person.Person AS p
JOIN HumanResources.Department AS hr
ON p.BusinessEntityID = hr.DepartmentID
JOIN HumanResources.Employee AS hre
ON p.BusinessEntityID = hre.BusinessEntityID
WHERE HireDate >= '20100101'
ORDER BY p.LastName DESC, HireDate;

--8
SELECT
    p.Name AS Name,
    pv.Name AS [supplier]
FROM Production.Product AS p
JOIN Purchasing.ProductVendor AS ppv
ON p.ProductID = ppv.ProductID
JOIN Purchasing.Vendor AS pv
ON ppv.BusinessEntityID = pv.BusinessEntityID

--9
SELECT
    p.FirstName +' '+ p.LastName AS name,
    s.Name AS [delivery method]
FROM Person.Person AS p
JOIN HumanResources.Employee AS hr
ON p.BusinessEntityID = hr.BusinessEntityID
JOIN Purchasing.PurchaseOrderHeader AS poh
ON hr.BusinessEntityID = poh.EmployeeID
JOIN Purchasing.Shipmethod AS s
ON s.ShipMethodID = poh.ShipMethodID
WHERE FirstName LIKE 'E%' AND s.Name like 'OVER%';

--10
SELECT * FROM Sales.SalesOrderHeader
SELECT * FROM HumanResources.Employee
SELECT * FROM Person.Person

--11
SELECT
    product.Name AS Produkt,
    cat.Name AS Kategoria,
    v.Name AS [vendor name]
FROM Production.Product AS product
JOIN Production.ProductSubcategory AS sub
ON product.ProductSubcategoryID = sub.ProductSubcategoryID
JOIN Production.ProductCategory AS cat
ON sub.ProductSubcategoryID = cat.ProductCategoryID
 JOIN Purchasing.ProductVendor AS pv
ON pv.ProductID = product.ProductID
 JOIN Purchasing.Vendor AS v
ON v.BusinessEntityID = pv.BusinessEntityID
WHERE cat.Name = 'Clothing'

--12
SELECT
    p.FirstName +' '+ p.LastName AS name,
    soi.SalesOrderID AS [order ID],
    soi.OrderDate AS [order date]
FROM Sales.SalesOrderHeader AS soi
JOIN Person.Person AS p
ON soi.CustomerID = p.BusinessEntityID
WHERE OrderDate BETWEEN '20110101' AND '20111231'
ORDER BY OrderDate

--13
SELECT
    p.ProductID AS productID,
    p.Name AS name,
    p.ListPrice AS [list price],
    v.Name AS supplier
FROM Production.Product AS p
JOIN Purchasing.ProductVendor AS pv
ON p.ProductID = pv.ProductID
JOIN Purchasing.Vendor AS v
ON pv.BusinessEntityID = v.BusinessEntityID
WHERE p.ListPrice > 25