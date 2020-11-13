# deepface
reconocimiento facial. 
importar deepface: pip install deepface
instalar django: python -m pip install Django

#da error al correrlo con django. 
#para probarlo solo con python: 
from deepface import DeepFace

def verificar(img1_path, img2_path):
    
    result  = DeepFace.verify(img1_path, img2_path)
    print(result["verified"])

verificar("53803_2020-11-12_16-06-14.png","dpi3216834980506.jpg")
