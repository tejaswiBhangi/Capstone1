from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

import pandas as pd

engine = create_engine('mysql+pymysql://root:Avatar16@localhost:3306/tractortek_salestracking')

engine.connect()
print(engine)




df = pd.read_excel('Employee.xlsx')
print(df.values)
df_products = pd.read_excel('Products.xlsx')
df_sales_period_data = pd.read_excel('Sales_Period_Data.xlsx')
df_price = pd.read_excel('Price.xlsx')
df_sales_quantities = pd.read_excel('Sales Quantities.xlsx')

from sqlalchemy.types import String, SmallInteger

df.to_sql('Employee', con=engine, if_exists='append', index=False, dtype=
          {'EmpID': String(length=255),
           'Sales Team Lead': String(length=255),
           'PayGrade': String(length=255), 
           'Region': String(length=255),
           'IsFound' : String(length=255)})

print(df_products)

df_products.to_sql('products', con = engine, if_exists = 'append', index = False, dtype = 
                   {'PROD_CODE': String(length=255),
                    'PROD_NAME': String(length=1024),
                    'URL_Link' : String(length=1024),
                    'Manufacturer' : String(length=255),
                    'Extended_Service_Plan' : String(length=255),
                    'Warranty_Price' : SmallInteger                                                                                  
})


df_sales_period_data.to_sql('Sales_Period_Data', con = engine, if_exists = 'append', index = False, dtype = 
                   {'sale_period_Index':String(length=255),
                    'Sale_Year': SmallInteger,
					'Sale_Week': SmallInteger,
					'Sales_Period': SmallInteger,
					'Quarter_Number': SmallInteger                                                                        
})

df_price.to_sql('Price', con = engine, if_exists = 'append', index = False, dtype = 
					{'Sales_code': String(length=255),
					'PROD_CODE': String(length = 255),		
					'Sale_Year': SmallInteger,
					'quarter_number': SmallInteger,
					'Price': SmallInteger                                                                       
})

df_sales_quantities.to_sql('Sales_Quantities', con = engine, if_exists = 'append', index = False, dtype = 
					{'Index_seq': String(length = 255), 
					'ITEM_CODE': String(length = 255),	
					'EMP_ID' :String(length = 255),
					'sale_year': SmallInteger,
					'sale_Week': SmallInteger,
					'Quantity': SmallInteger,                                                                      
})


