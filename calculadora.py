#Proyecto realizado por Bogdan Kaleb García Rivera 
import os
import random
operations = {}


def menu():
  print("*"*20)
  print("Bienvenido a la calculadora")
  print("1. Suma de dos numeros")
  print("2. Resta de dos numeros")
  print("3. Multiplicacion de dos numeros")
  print("4. Division de dos numeros")
  print("5. Exponenciacion de dos numeros")
  print("6. Muestra ultimas operaciones realizadas")
  print("7. Salir")
  try:
    opc = int(input("Seleccione una opcion: "))
    if opc in range(1,8):
      return opc
    else: 
      return 8
  except ValueError as error:
    print(error)
    return 9

def seleccion(opc):
  os.system ("clear")
  if opc<7:
    if opc!=6 and opc<7:
      try:
        a = float(input("Dame el primer numero: "))
        b = float(input("Dame el segundo numero: "))  
      except ValueError as error:
        print("Opción no válida: ",error)
        return None
    if opc==1:
      x = lambda m,n:m+n
      operations.update({f"Suma{random.randint(0, 1020)}":x(a,b)})
      return x(a,b)
    if opc==2:
      x = lambda m,n:m-n
      operations.update({"fResta{random.randint(0, 1020)}":x(a,b)})  
      return x(a,b)
    if opc==3:
      x = lambda m,n:m*n
      operations.update({f"Multiplicacion{random.randint(0, 1020)}":x(a,b)})
      return x(a,b)
