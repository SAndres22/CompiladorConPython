#Importamos el modulo lexico el cual contiene el analizador
from .analizador.lexico import analizador
#Importamos el modulo sintatico el cual contiene la funcion PARSE_EXPRESSION
from .analizador.sintactico import parse_expression

class Lexico():
    @staticmethod
    def analizar(codigo):
        # Definición de la función generadora para analizar tokens
        def generar_tokens():
            # Itera sobre cada línea del código con un contador que comienza en 1
            for contador, linea in enumerate(codigo.splitlines(), start=1):
                # Produce una cadena indicando el número de línea
                yield f"Linea # {contador}"

                # Ingresa la línea al analizador léxico
                analizador.input(linea)

                # Itera sobre los tokens generados por el analizador
                for tok in analizador:
                    # Produce un diccionario con información del token
                    yield {
                        "position": str(tok.lexpos + 1),  # Número de posición en la línea
                        "value": str(tok.value),  # Valor del token
                        "type": str(tok.type),  # Tipo del token
                    }

        # Convierte los resultados de la función generadora en una lista y retorna la lista
        return list(generar_tokens())


class Sintactico():
    @staticmethod
    def analizar(codigo):
        lineas = codigo.split('\n')
        resultados = []

        for numero_de_linea, linea in enumerate(lineas, start=1):
            resultado = parse_expression(linea.strip())
            resultados.append((numero_de_linea, resultado))

        return resultados
