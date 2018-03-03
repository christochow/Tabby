import gspread
from oauth2client.service_account import ServiceAccountCredentials
 
 
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

#Number of members and their names
numOfMembers=0
numOfMembers = int(input ("How many housemates"))
numOfMembers = numOfMembers+1

names = {}
i=2
while ( i<=numOfMembers):
    names[i]= input ('Enter name')
    i=i+1

 
# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Starterhacks").sheet1
 
# Extract and print all of the values
#sheet.update_cell(3, 1, "I just wrote to a spreadsheet using Python!")


#Update their names
i=2
while ( i<=numOfMembers):
    sheet.update_cell(1,i,names[i])
    sheet.update_cell (i,1,names[i])
    i=i+1

    
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)





    

