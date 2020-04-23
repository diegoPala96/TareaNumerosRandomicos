from random import randint
import numpy as np


print("primera forma randomicos")
a=[]
b=[]
suma=[]
for x in range(0,10):
	a.append(randint(1,6))
	b.append(randint(1,6))
	suma.append(a[x]+b[x])
	#print(a[x],"+",b[x], "= ",suma[x])




print("segunda forma randomico")
a=[]b=[]
suma=[]

for x in range(0,10):
	a.append(np.random.randint(1,6))
	b.append(np.random.randint(1,6))
	suma.append(a[x]+b[x])
	#print(a[x],"+",b[x], "= ",suma[x])







