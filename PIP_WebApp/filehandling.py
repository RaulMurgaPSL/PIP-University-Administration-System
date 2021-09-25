import models
import csv
import sqlite3
from inspect import isclass
import pandas as pd
import os

# *********************************************************** CSV ****************************************************************
def db2csv():
    tables = [x for x in dir(models) if isclass(getattr(models, x)) and x[0].isupper()]

    for table in tables:
        from glob import glob; from os.path import expanduser
        conn = sqlite3.connect( # open test.db
            glob(expanduser('test.db'))[0]
        )
        cursor = conn.cursor()
        cursor.execute(f"select * from {table};")
        with open(f"db_filehandling/CSV/{table}_test.csv", "w", newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([i[0] for i in cursor.description]) # write headers
            csv_writer.writerows(cursor)

# *********************************************************** EXCEL ****************************************************************
def csv2xlsx():
    folder = 'db_filehandling/CSV/'
    files = [file for file in os.listdir(folder) if '.csv' in file]
    writer = pd.ExcelWriter('db_filehandling/XLSX/test.xlsx', engine='xlsxwriter')
    for file in files:
        table = pd.read_csv(''.join([folder, file]), encoding='latin1')
        table.to_excel(writer, sheet_name=file.split('_')[0])
    writer.save()

# *********************************************************** RUN ****************************************************************
if __name__ == '__main__':
    db2csv()
    csv2xlsx()