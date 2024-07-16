import sqlalchemy as sqla
import pandas as pd


# Format berkas CSV
df = pd.read_csv("data.csv", delimiter=',')

# Format berkas XLSX atau XLS
df = pd.read_excel("data.xlsx", sheet_name='Sheet1')

# Format berkas JSON
df = pd.read_json('data.json')

# Format berkas HTML
url = "https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list"
df = pd.read_html(url)[0]

# Format berkas XML
df = pd.read_xml("https://www.w3schools.com/xml/books.xml")

# Akses data dari SQL database
# read_sql_table()untuk membaca SQL database table dan mempresentasikannya ke dalam bentuk pandas DataFrame.
db = sqla.create_engine("sqlite:///mydata.sqlite")
pd.read_sql_table("table_name", db)

# read_sql_query()untuk membaca SQL query dan mempresentasikannya ke dalam bentuk pandas DataFrame.
db = sqla.create_engine("sqlite:///mydata.sqlite")
pd.read_sql_query("SELECT * FROM table_name", db)

# read_sql()untuk membaca SQL query atau table dan mempresentasikannya ke dalam bentuk pandas DataFrame.
db = sqla.create_engine("sqlite:///mydata.sqlite")
pd.read_sql("SELECT * FROM table_name", db)
