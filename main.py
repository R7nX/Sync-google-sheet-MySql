 
from Google import Create_Service
import mysql.connector


CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

google_sheets_id = '1mqYkqyC_Eigm6MEjnBzSWehZgtCnZVLTRs16wEKp2LA'

response = service.spreadsheets().values().get(
    spreadsheetId=google_sheets_id,
    majorDimension='ROWS',
    range='A1:C3'
).execute()

rows = response['values'][0:]

mydb = mysql.connector.connect(

    host="113.172.178.64",
    port = "3306",
    user="root",
    password="Lmao!123",
    database = "test"

)


cursor = mydb.cursor()
a = 0

print(type(rows[0]))

for i in rows: 
    cursor.execute("INSERT INTO test.died VALUES(%s, %s, %s)", i)
    mydb.commit()

print('Data inserted!!!')
