-- Sample data to make queries look rich

-- Insert sample offices
INSERT INTO offices (officeCode, city, phone, addressLine1, country, postalCode, territory) VALUES
('1', 'San Francisco', '+1 650 219 4782', '100 Market Street', 'USA', '94080', 'NA'),
('2', 'Boston', '+1 215 837 0825', '1550 Court Place', 'USA', '02107', 'NA'),
('3', 'NYC', '+1 212 555 3000', '523 East 53rd Street', 'USA', '10022', 'NA'),
('4', 'Paris', '+33 14 723 4404', '43 Rue Jouffroy D''abbans', 'France', '75017', 'EMEA'),
('5', 'Tokyo', '+81 33 224 5000', '4-1 Kioicho', 'Japan', '102-8578', 'Japan'),
('6', 'Sydney', '+61 2 9264 2451', '5-11 Wentworth Avenue', 'Australia', '2010', 'APAC'),
('7', 'London', '+44 20 7877 2041', '25 Old Broad Street', 'UK', 'EC2N 1HN', 'EMEA');

-- Insert sample employees
INSERT INTO employees (employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle) VALUES
(1002, 'Murphy', 'Diane', 'x5800', 'dmurphy@classicmodelcars.com', '1', NULL, 'President'),
(1056, 'Patterson', 'Mary', 'x4611', 'mpatterso@classicmodelcars.com', '1', 1002, 'VP Sales'),
(1076, 'Firrelli', 'Jeff', 'x9273', 'jfirrelli@classicmodelcars.com', '1', 1002, 'VP Marketing'),
(1088, 'Patterson', 'William', 'x4871', 'wpatterson@classicmodelcars.com', '6', 1056, 'Sales Manager'),
(1102, 'Bondur', 'Gerard', 'x5408', 'gbondur@classicmodelcars.com', '4', 1056, 'Sale Manager'),
(1143, 'Bow', 'Anthony', 'x5428', 'abow@classicmodelcars.com', '1', 1056, 'Sales Manager'),
(1165, 'Jennings', 'Leslie', 'x3291', 'ljennings@classicmodelcars.com', '1', 1143, 'Sales Rep'),
(1166, 'Thompson', 'Leslie', 'x4065', 'lthompson@classicmodelcars.com', '1', 1143, 'Sales Rep'),
(1188, 'Firrelli', 'Julie', 'x2173', 'jfirrelli@classicmodelcars.com', '2', 1143, 'Sales Rep'),
(1216, 'Patterson', 'Steve', 'x4334', 'spatterson@classicmodelcars.com', '2', 1143, 'Sales Rep'),
(1286, 'Tseng', 'Foon Yue', 'x2248', 'ftseng@classicmodelcars.com', '3', 1143, 'Sales Rep'),
(1323, 'Vanauf', 'George', 'x4102', 'gvanauf@classicmodelcars.com', '3', 1143, 'Sales Rep'),
(1337, 'Bondur', 'Loui', 'x6493', 'lbondur@classicmodelcars.com', '4', 1102, 'Sales Rep'),
(1370, 'Hernandez', 'Gerard', 'x2028', 'ghernande@classicmodelcars.com', '4', 1102, 'Sales Rep'),
(1401, 'Castillo', 'Pamela', 'x2759', 'pcastillo@classicmodelcars.com', '4', 1102, 'Sales Rep'),
(1501, 'Bott', 'Larry', 'x2311', 'lbott@classicmodelcars.com', '7', 1102, 'Sales Rep'),
(1504, 'Jones', 'Barry', 'x102', 'bjones@classicmodelcars.com', '7', 1102, 'Sales Rep'),
(1611, 'Fixter', 'Andy', 'x101', 'afixter@classicmodelcars.com', '6', 1088, 'Sales Rep'),
(1612, 'Marsh', 'Peter', 'x102', 'pmarsh@classicmodelcars.com', '6', 1088, 'Sales Rep'),
(1619, 'King', 'Tom', 'x103', 'tking@classicmodelcars.com', '6', 1088, 'Sales Rep'),
(1621, 'Nishi', 'Mami', 'x101', 'mnishi@classicmodelcars.com', '5', 1056, 'Sales Rep'),
(1625, 'Kato', 'Yoshimi', 'x102', 'ykato@classicmodelcars.com', '5', 1621, 'Sales Rep'),
(1702, 'Gerard', 'Martin', 'x2312', 'mgerard@classicmodelcars.com', '4', 1102, 'Sales Rep');

-- Insert sample product lines
INSERT INTO productlines (productLine, textDescription, htmlDescription, image) VALUES
('Classic Cars', 'Attention car enthusiasts: Make your wildest car ownership dreams come true. Whether you are looking for classic muscle cars, hot rods or cuties, we have the perfect model for you.', NULL, NULL),
('Motorcycles', 'Our motorcycles are state of the art replicas of classic as well as contemporary motorcycle legends.', NULL, NULL),
('Planes', 'Unique, diecast airplane and helicopter replicas suitable for collections, gifts and recreational purposes.', NULL, NULL),
('Ships', 'The perfect holiday or anniversary gift for executives, clients, friends, and family.', NULL, NULL),
('Trains', 'Model trains are a rewarding hobby for enthusiasts of all ages.', NULL, NULL),
('Trucks and Buses', 'The Truck and Bus models are realistic replicas of buses and specialized trucks produced from the early 1920s to present.', NULL, NULL),
('Vintage Cars', 'Our Vintage Car models realistically portray automobiles produced from the early 1900s through the 1940s.', NULL, NULL);

-- Insert sample products
INSERT INTO products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP) VALUES
('S10_1678', '1969 Harley Davidson Ultimate Chopper', 'Motorcycles', '1:10', 'Min Lin Diecast', 'This replica features working kickstand, front suspension, gear-shift lever, footbrake lever, drive chain, wheels and steering.', 7933, 48.81, 95.70),
('S10_1949', '1952 Alpine Renault 1300', 'Classic Cars', '1:10', 'Classic Metal Creations', 'Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; opening glove compartment; detailed chassis; detailed cabin; detailed engine', 7305, 98.58, 214.30),
('S10_2016', '1996 Moto Guzzi 1100i', 'Motorcycles', '1:10', 'Highway 66 Mini Classics', 'Official Moto Guzzi logos and insignias, saddle bags located on side of motorcycle, detailed engine, working steering, working suspension, two leather seats, luggage rack, dual exhaust pipes, small saddle bag located on handle bars, two-tone paint with chrome accents, superior die-cast detail , rotating wheels , working kick stand, diecast metal with plastic parts, mounted on included wooden base.', 6625, 68.99, 118.94),
('S10_4698', '2003 Harley-Davidson Eagle Drag Bike', 'Motorcycles', '1:10', 'Red Start Diecast', 'Model features, official Harley Davidson logos and insignias, detachable rear wheelie bar, heavy diecast metal with some plastic parts, authentic multi-color tampo-printed graphics, separate engine drive belts, free-turning front fork, rotating tires, and has an included motorcycle stand.', 5582, 91.02, 193.66),
('S10_4757', '1972 Alfa Romeo GTA', 'Classic Cars', '1:10', 'Motor City Art Classics', 'Features include: Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; opening glove compartment', 3252, 85.68, 136.00),
('S10_4962', '1962 LanciaA Delta 16V', 'Classic Cars', '1:10', 'Second Gear Diecast', 'Features include: Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; opening glove compartment; detailed chassis; detailed cabin; detailed engine', 6791, 103.42, 147.74),
('S12_1099', '1968 Ford Mustang', 'Classic Cars', '1:12', 'Autoart Studio Design', 'Hood, doors and trunk all open to reveal highly detailed interior features. Engine details can be seen by removing the hood. 7 rotating wheels and rubber tires.', 68, 95.34, 194.57),
('S12_1108', '2001 Ferrari Enzo', 'Classic Cars', '1:12', 'Second Gear Diecast', 'Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; opening glove compartment; detailed chassis; detailed cabin; detailed engine', 3619, 95.59, 207.80),
('S12_1666', '1958 Setra Bus', 'Trucks and Buses', '1:12', 'Welly Diecast Productions', 'Model features 30 windows, skylights & glare resistant glass, working steering system, original logos', 1579, 77.90, 136.67),
('S12_2823', '2002 Suzuki XREO', 'Motorcycles', '1:12', 'Unimax Art Galleries', 'Official logos and insignias, saddle bags located on side of motorcycle, detailed engine, working steering, working suspension, two leather seats, luggage rack, dual exhaust pipes, small saddle bag located on handle bars, two-tone paint with chrome accents, superior die-cast detail , rotating wheels , working kick stand, diecast metal with plastic parts, mounted on included wooden base.', 9997, 66.27, 150.62);

-- Insert sample customers
INSERT INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, city, country, creditLimit) VALUES
(103, 'Atelier graphique', 'Schmitt', 'Carine ', '40.32.2555', '54, rue Royale', 'Nantes', 'France', 21000.00),
(112, 'Signal Gift Stores', 'King', 'Jean', '7025551838', '8489 Strong St.', 'Las Vegas', 'USA', 71800.00),
(114, 'Australian Collectors, Co.', 'Ferguson', 'Peter', '03 9520 4555', '636 St Kilda Road', 'Melbourne', 'Australia', 117300.00),
(119, 'La Rochelle Gifts', 'Labrune', 'Janine ', '40.67.8555', '67, rue des Cinquante Otages', 'Nantes', 'France', 118200.00),
(121, 'Baane Mini Imports', 'Bergulfsen', 'Jonas ', '07-98 9555', 'Erling Skakkes gate 78', 'Stavanger', 'Norway', 81700.00),
(124, 'Mini Gifts Distributors Ltd.', 'Nelson', 'Susan', '4155551450', '5677 Strong St.', 'San Rafael', 'USA', 210500.00),
(125, 'Havel & Zbyszek Co', 'Piestrzeniewicz', 'Zbyszek ', '(26) 642-7555', 'ul. Filtrowa 68', 'Warszawa', 'Poland', 0.00),
(128, 'Blauer See Auto, Co.', 'Keitel', 'Roland', '+49 69 66 90 2555', 'Lyonerstr. 34', 'Frankfurt', 'Germany', 59700.00),
(129, 'Mini Wheels Co.', 'Murphy', 'Julie', '6505555787', '5557 North Pendale Street', 'San Francisco', 'USA', 64600.00),
(131, 'Land of Toys Inc.', 'Lee', 'Kwai', '2125557818', '897 Long Airport Avenue', 'NYC', 'USA', 114900.00);

-- Insert sample orders
INSERT INTO orders (orderNumber, orderDate, requiredDate, shippedDate, status, customerNumber) VALUES
(10100, '2003-01-06', '2003-01-13', '2003-01-10', 'Shipped', 103),
(10101, '2003-01-09', '2003-01-18', '2003-01-11', 'Shipped', 128),
(10102, '2003-01-10', '2003-01-18', '2003-01-14', 'Shipped', 181),
(10103, '2003-01-29', '2003-02-07', '2003-02-02', 'Shipped', 121),
(10104, '2003-01-31', '2003-02-09', '2003-02-01', 'Shipped', 141),
(10105, '2003-02-11', '2003-02-21', '2003-02-12', 'Shipped', 145),
(10106, '2003-02-17', '2003-02-24', '2003-02-21', 'Shipped', 278),
(10107, '2003-02-24', '2003-03-03', '2003-02-26', 'Shipped', 131),
(10108, '2003-03-03', '2003-03-12', '2003-03-08', 'Shipped', 385),
(10109, '2003-03-10', '2003-03-19', '2003-03-11', 'Shipped', 486),
(10110, '2003-03-18', '2003-03-24', '2003-03-20', 'Shipped', 187),
(10111, '2003-03-25', '2003-03-31', '2003-03-30', 'Shipped', 129),
(10112, '2003-03-24', '2003-04-03', '2003-03-29', 'Shipped', 144),
(10113, '2003-03-26', '2003-04-02', '2003-03-27', 'Shipped', 124),
(10114, '2003-04-01', '2003-04-07', '2003-04-02', 'Shipped', 172);

-- Your original queries will now return rich data:

-- Query 1: INNER JOIN to get employee details with office information
SELECT 
    e.firstName, 
    e.lastName, 
    e.email, 
    e.officeCode,
    o.city,
    o.country
FROM employees e
INNER JOIN offices o ON e.officeCode = o.officeCode
ORDER BY e.lastName, e.firstName;

-- Query 2: LEFT JOIN to get product details with product line information
SELECT 
    p.productName, 
    p.productVendor, 
    p.productLine,
    pl.textDescription,
    p.quantityInStock,
    p.MSRP
FROM products p
LEFT JOIN productlines pl ON p.productLine = pl.productLine
ORDER BY p.productLine, p.productName;

-- Query 3: RIGHT JOIN to get order details with customer information (first 10 orders)
SELECT 
    o.orderDate, 
    o.shippedDate, 
    o.status, 
    o.customerNumber,
    c.customerName,
    c.city,
    c.country
FROM customers c
RIGHT JOIN orders o ON c.customerNumber = o.customerNumber
ORDER BY o.orderDate
LIMIT 10;