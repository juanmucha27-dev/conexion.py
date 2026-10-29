"""
if __name__ == '__main__':
    x = int(input("ingrese x: "))
    y = int(input("ingrese y: "))
    z = int(input("ingrese z: "))
    n = int(input("ingrese n: "))
    resultado = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print("***El resultado es*** = ", resultado)
"""
"""
p = int(input())
records = []
for _ in range(p):
    name = input()
    score = float(input())
    records.append([name, score])
#===notas unicas y ordenadas===
scores = sorted(set(s for n, s in records))
second_lowest = scores[1]

names = sorted({n for n, s in records if s == second_lowest})
    
for name in names:
    print(name)
"""

N = int(input("ingrese la cantidad: "))
list = []

for _ in range(N):
    command = input().split()
    if command[0] == "insert":
        list.insert(int(command[1], int(command[2])))
    elif command[0] == "print":
        print(list)
    elif command[0] == "remove":
        list.remove(int(command[1]))
    elif command[0] == "reverse":
        list.reverse(int(command[1]))
    elif command[0] == "len":
        list.__len__(int(command[1]), int(command[2]))
    elif command[0] == "delete":
        list.delete(int(command[1], int(command[2])))
"""
t = int(input())

for _ in range(t):
    line = input().strip()
    if not line:
        continue
    a, b = line.split()
    
    try:
        # comprobamos cual falla para poder crear el mensaje en ingles
        val_a = int(a)
        val_b = int(b)
        print(val_a // val_b)
        
    except ZeroDivisionError:
        # el juez espera este texto exacto para //
        print("Error Code: integer division or modulo by zero")
        
    except ValueError:
        # averiguamos que token fallo
        try:
            int(a)
            bad = b
        except:
            bad = a
        print(f"Error Code: invalid literal for int() with base 10: '{bad}'")
"""
"""
from collections import namedtuple

n = int(input())
cols = input().split()

# crea la tupla con los nombres de las columnas
Student = namedtuple('Student', cols)

total = 0
for _ in range(n):
    # *input().split() mete cada columna en su nombre
    s = Student(*input().split())
    total += int(s.MARKS)

print(f"{total / n:.2f}")
"""
"""
from collections import OrderedDict

n = int(input())
ventas = OrderedDict()

for _ in range(n):
    linea = input().strip()
    # separamos por espacio: lo ultimo es el precio, lo demas es el nombre
    *nombre_partes, precio = linea.split()
    nombre = " ".join(nombre_partes)
    ventas[nombre] = ventas.get(nombre, 0) + int(precio)

for nombre, total in ventas.items():
    print(nombre, total)
"""
"""
from collections import OrderedDict

n = int(input())
conteo = OrderedDict()

for _ in range(n):
    palabra = input().strip()
    conteo[palabra] = conteo.get(palabra, 0) + 1

print(len(conteo))
print(*conteo.values())
"""
"""
n = int(input())
arr = map(int, input().split())

puntajes_unicos = sorted(set(arr), reverse=True)

print(puntajes_unicos)
"""
"""
n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

felicidad = 0
for i in arr:
    if i in A:
        felicidad += 1
    elif i in B:
        felicidad -= 1
print(felicidad)
"""
"""
x = int(input())
a = set(map(int, input().split()))

y =  int(input())
b = set(map(int, input().split()))

resultado = sorted(a^b)

for i in resultado:
    print(i)
"""
"""
import re

T = int(input())

for _ in range(T):
    S = input()

    if re.search(r'(?<!\\)(?:[*+?]|\{[0-9]+(?:,[0-9]*)?\})\+', S):
        print(False)
        continue

    try:
        re.compile(S)
        print(True)
    except re.error:
        print(False)
"""
"""
cube = lambda x: x**3

def fibonacci(n):
    # return a list of fibonacci numbers
    a, b = 0, 1
    lista = []
    for _ in range(n):
        lista.append(a)
        a, b = b, a+b
    return lista
"""
"""
x = int(input())
y = int(input())
z = int(input())
n = int(input())

resultado = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]

print(resultado) 
"""
