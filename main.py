import gspread
import constants


credentials = Constants.API_KEY_SERVICE


gc = gspread.service_account(credentials)

# Open a sheet from a spreadsheet in one go
wks = gc.open("Twitter Twatter Tracker").sheet1

# Update a range of cells using the top left corner address
wks.update('A1', [[1, 2], [3, 4]])


