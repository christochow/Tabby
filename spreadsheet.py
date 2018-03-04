import gspread
from oauth2client.service_account import ServiceAccountCredentials
# use creds to create a client to interact with the Google Drive API
class Sheet:
    #initializes a Sheet object
    def __init__(self):
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        self.client = gspread.authorize(creds)
        self.numOfMembers=0;
        sheet_temp = self.client.open("Test")
        sheet1 = sheet_temp.sheet1
        sheet_name = input("Enter your house's name ")
        list_of_sheets = sheet1.row_values(1)
        if sheet_name not in list_of_sheets:
            new_row = [sheet_name]
            sheet1.insert_row(new_row,1)
            self.names = []
            self.initialize()
        else:
            self.sheet = self.client.open(sheet_name).sheet1
            self.names = self.sheet.col_values(1)
            #print(self.names)
            self.numOfMembers = int(self.sheet.cell(1,1).value)
    #initialize the spreadsheet
    def initialize(self):
        self.numOfMembers = int(input ("How many housemates "))
        self.names.append("")
        for a in range(self.numOfMembers):
            self.names.append(input("Enter name of housemate no."+str(a+1)+" "))
        i=1
        self.sheet.update_cell(1,1,self.numOfMembers)
        while (i<=self.numOfMembers):
            self.sheet.update_cell(1,i+2,self.names[i])
            self.sheet.update_cell (i+2,1,self.names[i])
            i=i+1
        list_of_hashes = self.sheet.get_all_records()
        print(list_of_hashes)
    #set a new dept between two members
    def set_Debt(self, payer, payee, amount):
        am = int(amount)
        ind = self.names.index(payer)
        p_ind = self.names.index(payee)
        self.sheet.update_cell(ind+1,p_ind+1,-am)
        self.sheet.update_cell (p_ind+1,ind+1,am)
    #add a new member to the spreadsheet
    def add_housemate(self, name):
        list = [name]
        for i in range(1,self.numOfMembers+1):
            list.append(0)
        self.names[self.numOfMembers+1] = name
        self.sheet.insert_row(list,self.numOfMembers+2)
        self.numOfMembers+=1
        self.sheet.update_cell(1,1,self.numOfMembers)
    #generate a list of string of who owes the use money
    def get_tabs(self,name):
        result = []
        ind = self.names.index(name)+1
        list = self.sheet.row_values(ind)
        for i in range(1,self.numOfMembers+1):
            member = self.names[i]
            if(member==name):
                continue
            if(len(list[i])!=0 or list[i]!='0'):
                if(int(list[i])>0):
                    result.append(member+" owes "+name+" "+ list[i])
                else:
                    result.append(name+" owes "+member+" "+ list[i][1:])
            else:
                    result.append(member+" does not owe you any money!")
        print (result)
        return result
if __name__ == "__main__":
    sh = Sheet()
    #sh.set_Debt("conrad","chris",200)
    #sh.add_housemate("rebecca")
    #sh.get_tabs("conrad")
