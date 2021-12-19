def mensagem(num1, num2):
  print(num1 + num2)

# mensagem(10,15)

def soma(a, b):
  return a + b

# print(soma(3, 5))

def calcula_energia_potencial_gravitacional(m, h, g = 10):
  e = g * m * h 
  return e

calcula_energia_potencial_gravitacional(30, 12, 9.8)
