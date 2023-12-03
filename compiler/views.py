from django.shortcuts import render
from compiler.models import Lexico
from compiler.models import Sintactico
from compiler.analizador.semantico import errores
from .analizador.sintactico import *

#Función para reiniciar el estado
def reiniciar_estado():
    # Elimina o restablece todas las variables y estructuras de datos relevantes
    # Por ejemplo, puedes limpiar la lista de errores semánticos
    errores.clear()
    variables_inicializadas.clear()
    nombres.clear()
    errores.clear()


def index(request):
    return render(request, "index.html")

def recibir_cod_fuente(request):
    cod_fuente = request.POST.get('cod_fuente', '')  # Obtén el código fuente del formulario
    mensjLex = Lexico.analizar(cod_fuente)  # Realiza el análisis léxico
    mensjSint = Sintactico.analizar(cod_fuente)  # Realiza el análisis sintáctico

    mensjSeman = errores  # Obtiene los errores semánticos
    

    return render(request, "index.html", {"cod_fuente": cod_fuente, 'mensaje': mensjLex, 'mensaje2': mensjSint, 'mensaje3': mensjSeman})

def reiniciar_programa(request):
    # Llama a la función de reinicio de estado antes de mostrar la página
    reiniciar_estado()
    return render(request, "index.html", {"cod_fuente": "", 'mensaje': "", 'mensaje2': "", 'mensaje3': ""})