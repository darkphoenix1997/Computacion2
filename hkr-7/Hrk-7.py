
# coding: utf-8

# In[ ]:

from  Stack import Stack


def calculadora_polaca(elementos):
    """ Dada una lista de elementos que representan las componentes de
        una expresión en notacion polaca inversa, evalúa dicha expresión.
        Si la expresion está mal formada, levanta ValueError. """
    resultado = None
    p = Stack()
    for elemento in elementos:

        print "DEBUG:", elemento
        # Intenta convertirlo a número
        try:
            numero = float(elemento)
            p.push(numero)
            print "DEBUG: push ", numero
            continue



        # Si no se puede convertir a número, debería ser un operando
        except ValueError:
            # Si no es un operando válido, levanta ValueError
            if elemento not in "+-*/ %" or len(elemento) != 1:
                raise ValueError("Operando inválido")
            # Si es un operando válido, intenta desapilar y operar
            try:
                a1 = p.pop()
                print p.peek()
                print "DEBUG: desapila ",a1
                a2 = p.pop()
                print "DEBUG: desapila ",a2
            # Si hubo problemas al desapilar
            except ValueError:
                print "DEBUG: error pila faltan operandos"
                raise ValueError("Faltan operandos")

            if elemento == "+":
                resultado = a2 + a1
            elif elemento == "-":
                resultado = a2 - a1
            elif elemento == "*":
                resultado = a2 * a1
            elif elemento == "/":
                resultado = a2 / a1
            elif elemento == " %":
                resultado = a2 % a1
            print "DEBUG: push ", resultado

            p.push(resultado)
        # Al final, el resultado debe ser lo único en la Pila


    res = p.pop()
    if p.isEmpty():
        return res
    else:
        print "DEBUG: error pila sobran operandos"
        raise ValueError("Sobran operandos")

def main():
    expresion = raw_input("Ingrese la expresion a evaluar: ")
    elementos = expresion.split()
    print elementos
    print calculadora_polaca(elementos)


