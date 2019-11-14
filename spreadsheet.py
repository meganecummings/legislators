import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("116th_congress_190103").sheet1

pp = pprint.PrettyPrinter()

result = sheet.row_values(43)

result_cols = sheet.col_values(26)

result_cell = sheet.cell(43,13).value

pp.pprint(result_cell)

sheet.update_cell(43,13, '555-555-5555')

result_cell = sheet.cell(43,13).value


pp.pprint(result_cell)

row = ["I'm", "updating", "a", "spreadsheet", "from", "python"]

index = 3

sheet.delete_row(index)

pp.pprint(sheet.row_count)
