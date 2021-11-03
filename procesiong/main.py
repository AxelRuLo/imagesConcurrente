import timeit
from imgurpython import ImgurClient
import urllib.request
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor  
id_cliente = "bfa0e227a1c5643"
secreto_cliente = "5f8c3cce299db5e26a2eb96b0b7809a82805c9ad"

cliente = ImgurClient(id_cliente, secreto_cliente)
listaURL = []

def descarga_url_img(link):
   nombre_img = link.split("/")[3]
   formato_img = nombre_img.split(".")[1]
   nombre_img = nombre_img.split(".")[0]
   url_local = "./images/{}.{}"
   urllib.request.urlretrieve(link, url_local.format(nombre_img, formato_img))

def multiProcesos():
   print('PROCESOS')
   with Pool(len(listaURL)) as p:
        p.map(descarga_url_img,listaURL)

def URLS():
   id_album = "bUaCfoz"
   imagenes = cliente.get_album_images(id_album)
   for imagen in imagenes:
       listaURL.append(imagen.link)
   
 
if __name__ == "__main__":
   URLS()
   print("Descarga {}".format(timeit.Timer(multiProcesos).timeit(number=1)))
