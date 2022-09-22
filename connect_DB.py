import sqlite3
import pandas as pd

def get_db_connection():
    conn = sqlite3.connect('Patients.db')
    conn.row_factory = sqlite3.Row
    return conn

conn = get_db_connection()
patientListSql = conn.execute('SELECT * FROM patient_table').fetchall()
patientListSql

##save data to dataframe
df = pd.DataFrame(patientListSql)
df

##rename columns
df.columns = ['mrn', 'firstname', 'lastname', 'dob', 'sex', 'zipcode', 'contactinformation', 'insuranceprovider']
df
