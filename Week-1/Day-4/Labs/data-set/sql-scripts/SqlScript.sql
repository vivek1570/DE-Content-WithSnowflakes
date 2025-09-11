CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50),
    DepartmentID INT,
    Salary DECIMAL(10,2),
    HireDate DATE,
    LastModifiedDate DATETIME
);
INSERT INTO Employee VALUES
(1,'John','Doe',10,60000,'2018-01-15','2025-01-01'),
(2,'Jane','Smith',20,75000,'2019-03-12','2025-01-05'),
(3,'Bob','Johnson',10,55000,'2020-07-22','2025-01-08'),
(4,'Alice','Williams',30,80000,'2021-02-11','2025-01-10'),
(5,'Charlie','Brown',20,72000,'2022-05-30','2025-01-11'),
(6,'Diana','Miller',10,58000,'2023-09-17','2025-01-13');

CREATE TABLE DeptSalarySummary (
    DepartmentName NVARCHAR(50),
    AvgSalary DECIMAL(10,2),
    EmpCount INT
);


CREATE TABLE CleanedOrders (
    OrderID INT,
    CustomerID NVARCHAR(20),
    CustomerName NVARCHAR(50),
    Region NVARCHAR(50),
    Qty INT,
    Year INT,
    Month INT
);
