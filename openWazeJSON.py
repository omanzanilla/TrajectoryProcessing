''' 
This code will open a json file obtained from waze, with the location and speed data of the users.
Orestes Manzanilla
24-01-2018 
'''
# One easy (though impractical) way to obtain the JSON files is the following:
# 
# 1) Open the "live map" in Google Chrome browser.
# 2) Adjust the zoom to the area of interest.
# 3) Press F12 to see information about the webpage.
# 4) Go to the tab "Network", and wait for the TGeoRSS* files to be loaded. Each few seconds arrives a new one. These have JSON format and a complex structure (not a table).
# 5) Right clic on one of the files and open in new tab.
# 6) Copy the contents of the JSON variable and paste it into a JSON viewer (I used http://jsonviewer.stack.hu/)
# 7) Go to the tab "Viewer" after pasting the variable.


import json

#Open the json file and save it as a python dictionary
with open('TGeoRSS.json','r') as f:
	tGeoRSS_dict = json.load(f)

#Specify the user for which the data will be read
User = 0

#Puedo guardar en variables la data
startTime = tGeoRSS_dict['startTime'] #String
endTime = tGeoRSS_dict['endTime'] #String
userID = tGeoRSS_dict['users'][User]['id'] #String 
speed = tGeoRSS_dict['users'][User]['speed'] #Float
x = tGeoRSS_dict['users'][User]['location']['x'] #Float
y = tGeoRSS_dict['users'][User]['location']['y'] #Float
