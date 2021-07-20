import pandas as pd
from sqlalchemy import create_engine
import pymysql

excelFile = r'/Users/mark/Desktop/test_excle2database.xlsx'
df = pd.DataFrame(pd.read_excel(excelFile))

engine = create_engine('mysql+pymysql://root:mark1005@localhost:3306/ods', encoding='utf8')
df.to_sql('students', con=engine, if_exists='append', index=False)
