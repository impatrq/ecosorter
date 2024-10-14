from ultralytics import YOLO
from enum import Enum

class ModelType(Enum):
    YOLOv8n = 'yolov8n.pt'
    YOLOv8s = 'yolov8s.pt'
    pers = 'ecosorter.pt'

class Camera(Enum):
    LAPTOP = '0'

def liveObjectDetection(modelType: ModelType):
    model = YOLO(modelType.value)
    
    # Usar 'stream=True' para manejar largos streams o videos
    results = model.predict(source=Camera.LAPTOP.value, stream=True, show=True)
    
    for result in results:
        # Acceder a los nombres de las clases detectadas en los resultados
        for box in result.boxes:
            class_id = int(box.cls[0])  # Obtener el ID de la clase detectada
            class_name = model.names[class_id]  # Convertir ID a nombre de la clase
            
            if class_name == 'botella':  # Ajusta al nombre de la clase que te interese
                print("Se ha detectado una botella!")
            elif class_name == 'envoltorio':  # Otro ejemplo de condición
                print("Se ha detectado un envoltorio!")
            else:
                print(f"Se ha detectado un objeto: {class_name}")

if __name__ == '__main__':
    liveObjectDetection(ModelType.pers)