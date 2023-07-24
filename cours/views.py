from django.shortcuts import render
from .models import Cours

#*****creation de la vue*******



def acceuilView(request, template_name="cours/pages/index.html"):
    #****** contex permet d'envoyer le code python vers html*****
    #****** declaration de notre context *****
    contex = {}
    bonjour = "Bonjour Ghost, vous allez bien ?"
    #affectation de la clé et valeur dans contex
    #         key      valeur
    c1 = Cours("Java", "Mr johnny")
    c2 = Cours("php", "Mr jean")
    c3 = Cours("django", "Mr josue")
    c4 = Cours("Csharp", "Mr josias")
    c5 = Cours("ai", "Mr john")
    c6 = Cours("Javascript", "Mr yve")
    c7 = Cours("kotlin", "Mr pirre")
    c8 = Cours("html", "Mr gloire")
    list_cours = [c1, c2, c3, c4, c5, c6, c7, c8]

    contex['name'] = bonjour
    contex['cours'] = list_cours

    return render(request, template_name, contex)

def aboutView(request, template_name="cours/pages/about.html"):
    return render(request, template_name)



