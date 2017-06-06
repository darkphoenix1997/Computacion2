
# coding: utf-8

from  Stack import Stack


def calculadora_polaca(elementos):
    resultado = None
    p = Stack()
    for elemento in elementos:

        print "DEBUG:", elemento
        
        try:
            numero = float(elemento)
            p.push(numero)
            print "DEBUG: push ", numero
            continue



        
        except ValueError:
            
            if elemento not in "+-*/ %" or len(elemento) != 1:
                raise ValueError("Operando inválido")
          
            try:
                a1 = p.pop()
                print p.peek()
                print "DEBUG: desapila ",a1
                a2 = p.pop()
                print "DEBUG: desapila ",a2
          
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


