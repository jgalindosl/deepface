from django.http import HttpResponse
from deepface import DeepFace

def verificar():
    result = DeepFace.verify("C:/laragon/www/asistencia/fotos/4-617.jpg","C:/laragon/www/asistencia/fotos/4-617.jpg")
    
    return HttpResponse(result['verified'])
    