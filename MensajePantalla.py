# Escribe un programa que solicite al usuario su edad y la guarda en una variable
# que luego solicite la cantidad de articulos comprados en una tienda 
# y la guarde en otra variable. Finalmente, mostrar en pantalla un valor
# de verdad (True o False) que indique si el usuario es mayor de
# 18 años de edad y ademas compra más de 1 artículo.

edad = int(input("Ingresar la edad: "))
articulos = int(input("Ingresar la cantidad de articulos: "))

if edad > 18:
    if articulos > 1:
        print(True)
    else:
        print(False)
else:
    print(False)