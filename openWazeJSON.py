#Importar la libreria que maneja los JSONs en Python
import json

#Abrir el archivo y guardarlo en una variable como un diccionario
with open('TGeoRSS.json','r') as f:
	tGeoRSS_dict = json.load(f)

#Defino en la variable User el usuario al que voy a extraerle la data
User = 0

#Puedo guardar en variables la data
startTime = tGeoRSS_dict['startTime'] #String
endTime = tGeoRSS_dict['endTime'] #String
userID = tGeoRSS_dict['users'][0]['id'] #String 
speed = tGeoRSS_dict['users'][0]['speed'] #Float
x = tGeoRSS_dict['users'][0]['location']['x'] #Float
y = tGeoRSS_dict['users'][0]['location']['y'] #Float

#Tambien puedes hacer una lista con esos valores:
vector = (startTime, endTime, userID, speed, x, y)
print(vector)
#NOTA: tambien puedes hacer una matriz de numpy o dataframe con Pandas...

#Y si quieres directamente imprimirlos sin guardarlos en variables, puedes hacerlo así

print('StartTime: %s' % tGeoRSS_dict['startTime'])
print('EndTime: %s' % tGeoRSS_dict['endTime'])
print('User: %d' % User)
print('ID: %s' % tGeoRSS_dict['users'][0]['id'])
print('Speed: %f' % tGeoRSS_dict['users'][0]['speed'])
print('Location: x = %f' % tGeoRSS_dict['users'][0]['location']['x'])
print('Location: y = %f' % tGeoRSS_dict['users'][0]['location']['y'])


