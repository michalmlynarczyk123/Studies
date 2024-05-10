USE AdventureWorks2014

SELECT * FROM Production.Product;

-- USE master

-- BAZA.SCHEMAT.TABELA

SELECT * FROM AdventureWorks2014.Production.Product;

SELECT ProductID, Name, ProductNumber, MakeFlag, Color FROM Production.Product;

SELECT ProductID, Name, Color FROM Production.Product ORDER BY Name;

SELECT ProductID, Name, Color FROM Production.Product ORDER BY Color ASC, Name ASC;

SELECT ProductID, Name, Color FROM Production.Product ORDER BY Color DESC, Name;

SELECT * FROM Production.Product WHERE Color = 'Black';

SELECT  * FROM Production.ProductSubcategory WHERE ProductCategoryID = 1;

SELECT  * FROM Production.ProductSubcategory WHERE ModifiedDate = '2008-04-30';

SELECT * FROM Production.ProductSubcategory WHERE ProductSubcategoryID < 10;
SELECT * FROM Production.ProductSubcategory WHERE ProductSubcategoryID <= 10;

SELECT * FROM Production.ProductSubcategory WHERE Name != 'Mountain Bikes';
SELECT * FROM Production.ProductSubcategory WHERE Name <> 'Mountain Bikes'; /* To samo co to na górze */

SELECT * FROM Production.ProductSubcategory WHERE Name = 'Mountain Bikes';

SELECT * FROM Production.ProductSubcategory WHERE Name LIKE 'Mountain Bikes';
SELECT * FROM Production.ProductSubcategory WHERE Name LIKE '%Bikes';

SELECT * FROM Production.ProductSubcategory WHERE Name LIKE 'C%';

SELECT * FROM Production.Product WHERE Name LIKE 'Flat Washer %';
SELECT * FROM Production.Product WHERE Name LIKE 'Flat Washer _'; /* pojedynczy znak */

SELECT * FROM Production.Product WHERE Name LIKE 'Classic Vest, _';
SELECT * FROM Production.Product WHERE Name LIKE 'Classic Vest, [LM]'; /* szukamy bez rozmiaru S */
SELECT * FROM Production.Product WHERE Name LIKE 'Classic Vest, [K-Z]'; /* szukamy po zakresie */
SELECT * FROM Production.Product WHERE Name LIKE 'Classic Vest, [P-Z]'; /* szukamy po zakresie */

/* AND OR */

-- () -> AND -> OR kolejność wykonywania query
SELECT Color, Name, ProductSubcategoryID FROM Production.Product
WHERE (Color = 'Red' OR Color = 'Black') AND ProductSubcategoryID = 1
ORDER BY Color;

SELECT Color, Name, ProductSubcategoryID FROM Production.Product
WHERE Color = 'Red' AND Color = 'Black'; /* nie przeleci */

SELECT Color, Name, ProductSubcategoryID FROM Production.Product WHERE NOT Color = 'Red';

SELECT Color, Name, ProductSubcategoryID FROM Production.Product
WHERE Color = 'Red' OR Color = 'Black' OR Color = 'Silver';

SELECT Color, Name, ProductSubcategoryID FROM Production.Product
WHERE Color IN ('Red', 'Black', 'Silver'); /* to samo co na górze ale lepsze, bo z importu, hehehe */

SELECT Color, Name, ProductSubcategoryID FROM Production.Product
WHERE Color NOT IN ('Red', 'Black', 'Silver'); /* to samo co na górze ale wyłączając te kolory */

SELECT Color, Name, ProductSubcategoryID FROM Production.Product
WHERE (ProductSubcategoryID = 2 AND Color <> 'Red') OR (ProductSubcategoryID = 1 AND Color <> 'Black');

SELECT Color, Name, ProductSubcategoryID FROM Production.Product
WHERE (ProductSubcategoryID = 2 AND Color <> 'Red') OR (ProductSubcategoryID = 1 AND Color <> 'Black')
ORDER BY ProductSubcategoryID, Color;

SELECT * FROM Production.ProductSubcategory
WHERE ProductSubcategoryID >= 10 AND ProductSubcategoryID < 20;

SELECT * FROM Production.ProductSubcategory
WHERE ProductSubcategoryID BETWEEN 10 AND 19; /* to samo co na górze */

SELECT * FROM Sales.SalesOrderHeader
WHERE OrderDate >= '2011-08-01' AND OrderDate <= '2011-08-30'

SELECT * FROM Sales.SalesOrderHeader
WHERE OrderDate BETWEEN '20110801' AND '20110830';  /* to samo co na górze */

SELECT Color, Name, ProductSubcategoryID FROM Production.Product
-- WHERE Color IS NOT null;
WHERE Color IS null;

SELECT ISNULL(Color, 'Brak Koloru'), Name, ProductSubcategoryID FROM Production.Product;

SELECT DISTINCT Color FROM Production.Product
SELECT DISTINCT ISNULL(Color, 'BRAK') FROM Production.Product
SELECT DISTINCT Color, Name FROM Production.Product

SELECT Color AS 'kolor produktu', Name AS 'nazwa produktu' From Production.Product;

SELECT TOP 5 PERCENT Color AS kolor, Name AS nazwa FROM Production.Product
ORDER BY Color DESC;

SELECT * FROM Person.Person;

SELECT FirstName, LastName, FirstName + ' ' + LastName AS [Pełne imię] FROM Person.Person;

SELECT
    FirstName,
    LEFT(FirstName, 1) AS inicjał,
    LEFT(FirstName, 3) AS first_three,
    SUBSTRING(FirstName, 1, 2),
    SUBSTRING(FirstName, 3, 5),
    SUBSTRING(FirstName, 4, 5)
FROM Person.Person

SET language 'Polish'
SELECT
    SellStartDate,
    YEAR(SellStartDate),
    DATENAME(mm, SellStartDate) AS miesiąc,
    DATENAME(dw, SellStartDate) AS [dzień tygodnia],
    DAY(SellStartDate),
    DATEDIFF(yy, SellStartDate, GETDATE()) AS [ile lat]
FROM Production.Product

SELECT
    Name,
    UPPER(Name),
    Weight,
    ROUND(Weight, 0),
    ROUND(Weight, 1)
FROM Production.Product
WHERE Weight IS NOT NULL