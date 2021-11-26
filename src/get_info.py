from datetime import datetime

myFile = open('/Users/alexyucra/Documents/relatorios/dashboard/src/json/append.txt', 'a') 
myFile.write('\nAccessed on ' + str(datetime.now()))