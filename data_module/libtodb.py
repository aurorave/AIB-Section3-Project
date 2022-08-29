import sqlite3
import pandas as pd

conn = sqlite3.connect('s3_project.db') # db 생성 (해당 이름의 db 없을 시 생성하고 연결, 있으면 그냥 연결)


# 도서관 CSV 파일 DB 연결
dt = pd.read_csv('data/library_public.csv')
dt.to_sql('letsread', conn)