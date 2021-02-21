import gspread
import constants


credentials = constants.API_KEY_SERVICE


gc = gspread.service_account(filename='/Users/rylandgrounds/Downloads/twitter-twatter--1613940316400-060db39d0e19.json')

# Open a sheet from a spreadsheet in one go
wks = gc.open("Twitter Twatter Tracker").sheet1

# Update a range of cells using the top left corner address
wks.update('A1', [['hello', 'world'], [3, 4]])


