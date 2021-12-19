# import math

# print(math.sqrt(9))

# print(math.sin(45))

# print(math.cos(45))

# print(math.log(1000, 10))

# print(math.log(32, 2))

# print(math.log(1000))

# print(math.pi)

import datetime

# print(dir(datetime))

# print(datetime.date.today())

# datetime.datetime.now()

# data = datetime.date(2020, 7, 10)

# print(data.day)
# print(data.month)
# print(data.year)

# print(f"{data.day} do {data.month} de {data.year}")

import random

# print(random.random())

# print(random.randint(1, 10))

# print(random.randrange(0, 10, 2))

# print(random.randrange(0, 10, 3))

x = ['k', 'd', 12, '34-j', 'x']

# print(random.choice(x))

import time as tm 

# print(tm.time())

antes = tm.time()

lista = [];

for i in range(0, 100000):
  lista.append(i)
  
depois = tm.time()

print(depois - antes)
