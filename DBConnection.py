import pandas as pd
import pyodbc

# getting connecttion
conn = pyodbc.connect(r'DSN=drf;UID=sa;PWD=sa_1234$')
QRY = ("select * from vw_aspirantdetails ")
data = pd.io.sql.read_sql(QRY, con=conn)
