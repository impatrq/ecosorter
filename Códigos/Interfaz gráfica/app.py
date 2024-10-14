from flask import Flask, render_template, url_for
from gpiozero import DistanceSensor
import threading
from time import sleep

app = Flask(__name__)

#Sensores Ultrasónicos
medidorVid = DistanceSensor(echo= 24, trigger= 23)
medidorPlas = DistanceSensor(echo= 25, trigger= 8)
medidorMet = DistanceSensor(echo= 7, trigger= 12)
medidorRes = DistanceSensor(echo= 16, trigger= 20)

class medir:
    def vid(self):
            try:
                disvid = medidorVid.distance * 100
                sleep(0.1)
            except:
                print("error")
            print (disvid)
            disvid = (disvid / 40) * 100
            capacidadvid = 100 - disvid
            self.capacidadvid = capacidadvid
            return self.capacidadvid

    def plas(self):
        try:
            displas = medidorPlas.distance * 100
            sleep(.01)
        except:
            print("error")
        displas = (displas * 100) / 40
        capacidadplas = 100 - displas
        self.capacidadplas = capacidadplas
        return self.capacidadplas 

    def res(self):
        try:
            disres = medidorRes.distance * 100 
            sleep(.01)
        except:
            print("error")
        disres = (disres * 100) / 40
        capacidadres = 100 - disres
        self.capacidadres = capacidadres 
        return self.capacidadres 

    def met(self):
        try:
            dismet = medidorMet.distance * 100 
            sleep(.01)
        except:
            print("error")
        dismet = (dismet * 100) / 40
        capacidadmet = 100 - dismet 
        self.capacidadmet = capacidadmet
        return self.capacidadmet
    
var = 0

#Defino funcion para interfaz gráfica 
def servidor():
        
    @app.route("/")
    def index():
            return render_template("index.html")

    @app.route("/medidas")
    def medidas():
            global varVid
            global varMet
            global varPlas
            global varRes

            while True:
                    refrescar = 5
                    vid = int(class_.vid())
                    plas = int(class_.plas())
                    res = int(class_.res())
                    met = int(class_.met())
                    detPlas = 0
                    detMet = 0
                    detRes = 0
                    detVid = 0
                    if varPlas == 1:
                         detPlas = 1
                         refrescar = 15
                         varPlas = 0
                    elif varMet == 1:
                         detMet = 1
                         refrescar = 15
                         varMet = 0
                    elif varRes == 1:
                         detRes = 1
                         refrescar = 15
                         varRes = 0
                    elif varVid == 1:
                         detVid == 1
                         refrescar = 15
                         varVid = 0
                    return render_template("medidas.html",
                                            vid = vid,
                                            plas = plas,
                                            res = res,
                                            met = met,
                                            detPlas = detPlas,
                                            detMet = detMet,
                                            detRes = detRes,
                                            detVid = detVid,
                                            refrescar = refrescar)
            
#Asigno la clase            
class_ = medir()

#Creo el hilo
hilo1 = threading.Thread(target= servidor)
#Lo inicio
hilo1.start()