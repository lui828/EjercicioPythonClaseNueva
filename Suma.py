# Escribe un programa que solicite al usuario dos números y los almacene 
# en dos variables. En otra variable, almacená el resultado de la suma 
# de esos dos números y luego mostrá ese resultado en pantalla.
# A continuación, el programa debe solicitar al usuario que ingrese un 
# tercer número, el cual se debe almacenar en una nueva variable. 
# Por último, mostrá en pantalla el resultado de la multiplicación de 
# este nuevo número por el resultado de la suma anterior.

primernumero = int(input("Escribe el primer numero: "))
segundonumero = int(input("Escribe el segundo numero: "))

suma = primernumero + segundonumero
print(suma)

tercernumero = int(input("Escribe el tercer numero: "))

multi = suma * tercernumero
print(multi)