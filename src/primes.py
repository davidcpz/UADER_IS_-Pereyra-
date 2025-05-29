#!/usr/bin/python3
# Python program to display all the prime numbers within an interval
#define el limite inf y sup del intervalo
lower = 1
upper = 500

print("Prime numbers between", lower, "and", upper, "are:")
#trabaja sobre todos los numeros del intervalo, con el valor superiór includio
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       #comprueba si el numero es divisible por algun numero en el rango de 2 a "num"
       for i in range(2, num):
           #si num es divisible por "i" entonces no es primo,se termina el ciclo
           if (num % i) == 0:
               break
       else:
           #si no tiene divisor entonces es primo y lo muestra
           print(num)
