from ultralytics import YOLO
from enum import Enum
import RPi.GPIO as GPIO
from time import sleep

#configurando GPIO
GPIO.setmode(GPIO.BCM)

#capacitivo
capacitivo = 20
GPIO.setup(capacitivo, GPIO.IN)

# Configuración de los pines GPIO del motor para el movimiento de los ejes 
PUL_PIN_1 = 17  # Pin para el pulso 
DIR_PIN_1 = 27  # Pin para la dirección 
GPIO.setup(PUL_PIN_1, GPIO.OUT)
GPIO.setup(DIR_PIN_1, GPIO.OUT)

# Configuración de los pines GPIO del motor para la apertura de la compuerta del canasto
PUL_PIN_2 =  2
DIR_PIN_2 = 3
GPIO.setup(PUL_PIN_2, GPIO.OUT)
GPIO.setup(DIR_PIN_2, GPIO.OUT)

class ModelType(Enum):
    YOLOv8n = 'yolov8n.pt'
    YOLOv8s = 'yolov8s.pt'
    pers = 'ecosorter.pt'

class Camera(Enum):
    LAPTOP = '0'

def mover_motor_eje(pasos, direccion, velocidad):
    # Establecer la dirección
    GPIO.output(DIR_PIN_1, direccion)
    
    for paso in range(pasos):
        # Enviar un pulso al driver
        GPIO.output(PUL_PIN_1, GPIO.HIGH)
        sleep(velocidad)  # Controla la velocidad del motor
        GPIO.output(PUL_PIN_1, GPIO.LOW)        
        sleep(velocidad)

def mover_motor_canasto(pasos, direccion, velocidad):
    # Establecer la dirección
    GPIO.output(DIR_PIN_2, direccion)
    
    for paso in range(pasos):
        # Enviar un pulso al driver
        GPIO.output(PUL_PIN_2, GPIO.HIGH)
        sleep(velocidad)  # Controla la velocidad del motor
        GPIO.output(PUL_PIN_2, GPIO.LOW)        
        sleep(velocidad)


def liveObjectDetection(modelType: ModelType):
    funcionamiento = 0
    model = YOLO(modelType.value)
    
    # Usar 'stream=True' para manejar largos streams o videos
    results = model.predict(source=Camera.LAPTOP.value, stream=True, show=True)
    

    for result in results:
        # Acceder a los nombres de las clases detectadas en los resultados
        for box in result.boxes:
            class_id = int(box.cls[0])  # Obtener el ID de la clase detectada
            class_name = model.names[class_id]  # Convertir ID a nombre de la c>

            if GPIO.input(capacitivo) == 0:
                if class_name == 'botella' and funcionamiento == 0:  # Ajusta a>
                    #Bloqueo la tarea
                    funcionamiento = 1
                    print("Se ha detectado una botella!")
                    # Muevo el canasto al cesto de plástico
                    mover_motor_eje(2000, GPIO.HIGH, 0.001)  

                    # Pausa antes de cambiar de dirección
                    sleep(1)
                    
                    #Abro canasto 
                    mover_motor_canasto(120, GPIO.HIGH, 0.001)

                    sleep(1)

                    mover_motor_canasto(120, GPIO.LOW, 0.001)

                    # Mover el motor en la otra dirección
                    mover_motor_eje(2000, GPIO.LOW, 0.001) 
                    #Libero la tarea 
                    funcionamiento = 0

                elif class_name == 'envoltorio' and funcionamiento == 0:  # Otr>
                    #Bloqueo tarea
                    funcionamiento = 1
                    print("Se ha detectado un metal!")
                    # Muevo el canasto al cesto de metales
                    mover_motor_eje(2000, GPIO.LOW, 0.001)  

                    # Pausa antes de cambiar de dirección
                    sleep(1)
                    
                    #Abro canasto 
                    mover_motor_canasto(120, GPIO.HIGH, 0.001)

                    sleep(1)

                    mover_motor_canasto(120, GPIO.LOW, 0.001)

                    # Mover el motor en la otra dirección
                    mover_motor_eje(2000, GPIO.HIGH, 0.001) 
                    #Libero tarea
                    funcionamiento = 0

                else:
                    print(f"Se ha detectado un objeto: {class_name}")

if __name__ == '__main__':
    liveObjectDetection(ModelType.pers)


