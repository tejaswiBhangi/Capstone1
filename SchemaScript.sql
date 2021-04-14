-- CREATE SCHEMA tractortek_salestracking;
-- USE tractortek_salestracking;
DROP TABLE IF EXISTS sales_quantities;

DROP TABLE IF EXISTS price;

DROP TABLE IF EXISTS sales_period_data;

DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS employee;

CREATE TABLE Employee (
Emp_ID VARCHAR(25) NOT NULL,
Sales_Team_Lead VARCHAR(50),	
PayGrade VARCHAR(25),
Region VARCHAR(25),	
PRIMARY KEY (Emp_ID)
)ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;

alter table Employee
add IsFound varchar(25);

CREATE TABLE Products (
PROD_CODE VARCHAR(100) NOT NULL,
PROD_NAME VARCHAR(100),	
URL_link VARCHAR(2083),	
Manufacturer VARCHAR(25),		
Extended_Service_Plan VARCHAR(25),
Warranty_Price INT(8),
PRIMARY KEY (PROD_CODE)
)ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE Sales_Period_Data (	
sale_period_Index VARCHAR(10) not null,
Sale_Year Int(4),
Sale_Week Int(2),
Sales_Period Int(2),
Quarter_Number Int(2), 
PRIMARY KEY (sale_period_index)
)ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE Price (
Sales_code varchar(100) not null,
PROD_CODE VARCHAR(25) NOT NULL,		
Sale_Year Int(4),
quarter_number Int(2),
Price Float(2),
PRIMARY KEY (Sales_code),
FOREIGN KEY (PROD_CODE) REFERENCES Products(PROD_CODE)
)ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE Sales_Quantities (
Index_seq INT not null Auto_Increment, 
ITEM_CODE VARCHAR(25) NOT NULL,	
EMP_ID VARCHAR(25) NOT NULL,
sale_year VARCHAR(100),
sale_week Int(2),
quantity Int(4),
primary key (Index_seq),
FOREIGN KEY (EMP_ID) REFERENCES Employee(Emp_id)
)ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;

SELECT host from mysql.user where user = "root"