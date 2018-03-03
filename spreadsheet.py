import gspread
from oauth2client.service_account import ServiceAccountCredentials
 
 
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
 
# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Starterhacks").sheet1
 
# Extract and print all of the values
sheet.update_cell(3, 1, "I just wrote to a spreadsheet using Python!")

list_of_hashes = sheet.get_all_records()
print(list_of_hashes)



numOfMembers=0
numOfMembers = int(input ("How many housemates"))

names = {}
i=0
while ( i<numOfMembers):
    names[i]= input ('Enter name')
    i=i+1
    

