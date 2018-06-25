from bs4 import BeautifulSoup
import requests

#esta la url de donde sacaremos el nombre de todos los paise y luego los guardaremos
#en un array
urlpaises= "http://www.banderas-mundo.es/continente"
req = requests.get(urlpaises)
#definimos el array donde guardaran los paises
nombrepaise=[]
#con esto defnimos si esta deolviendo el 200
status_code = req.status_code
#imprimimos la url para verificar si es corecta
print(urlpaises)
if status_code == 200:
    #metemos todo el contenido del html en html
    html = BeautifulSoup(req.text, "html.parser")
    #del contenido html filtamos el td con la class tb-country
    paises=html.findAll("td", {"class": "td-country"})
    #hacemos un recorrido para sacar el texto de cada pais
    for i, npaises in enumerate(paises):
        #del codigo sacamos solo el texto
        textpaises=npaises.getText()
        #lo metemos en el arry que definimos antes (identificador,datosaintroducir)
        nombrepaise.insert(i,textpaises)
#este else es para si no hay respues de la web
else:
    print ("Status Code %d" % status_code)
#con esto lo que hacemos en recorrer el array verificar si estan los datos
for i, nombrepaises in enumerate(nombrepaise):
    print(nombrepaises)
#lo que debemos relisar es que esto este en un array y luego lo recorra para ponerlo en una url
#con esto sacamos los datos del pais y los expulsamos como un print y luego lo pegamos dentro de la
#base de datos
