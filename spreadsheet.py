import gspread
from oauth2client.service_account import ServiceAccountCredentials
# use creds to create a client to interact with the Google Drive API
class Sheet:
    def __init__(self):
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        self.client = gspread.authorize(creds)
        sheet = self.client.open("Test").sheet1
        sheet_name = input("Enter your house's name ")
        list_of_sheets = sheet.row_values(1)
        if sheet_name not in list_of_sheets:
            new_row = [sheet_name]
            sheet.insert_row(new_row,1)
            # Find a workbook by name and open the first sheet
            # Make sure you use the right name here.
        self.sheet1 = self.client.open(sheet_name).sheet1
        self.initialize()

    def initialize(self):
# Extract and print all of the values
        list_of_hashes = self.sheet1.get_all_records()
        print(list_of_hashes)
        numOfMembers=0
        numOfMembers = int(input ("How many housemates "))
        i=0
        while ( i<numOfMembers):
            self.sheet.update_cell(1,i+2,names[i])
            self.sheet.update_cell (i+2,1,names[i])
            i=i+1
        list_of_hashes = sheet.get_all_records()
        print(list_of_hashes)
if __name__ == "__main__":
    sh = Sheet()
