import pandas as pd
import psycopg2
from sqlalchemy import create_engine


user = 'admin'
password = 'admin'
host = 'localhost'
port = '5ooo'
db = 'titanicdb'

engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

df = pd.read_csv('donnees_nettoyees.csv')

df.to_sql('titanic', engine, if_exists='replace', index=False)
