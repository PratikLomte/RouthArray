from sympy import *
from numpy import *
deg = int(input("Enter highest degree of s: "))
den = []

for i in range(deg+1):
    temp = int(input("Enter coefficient in descending: "))
    den.append(temp)
print(den)

if deg%2==0:
    even_coeff = den[::2]
    odd_coeff = den[1::2]

else:
    even_coeff = den[1::2]
    odd_coeff = den[::2]

pratik = len(even_coeff)
advait = len(odd_coeff)
print(even_coeff, odd_coeff)

n = len(den)-1
if n < 2:
    print('invalid input')

m = zeros(n+1) 

# Insert the first two rows
if deg%2==0: 
    for i in range(0,pratik):
        m[0,i] = even_coeff[i]

    for i in range(0,advait):
        m[1,i] = odd_coeff[i]

else:
    for i in range(0,pratik):
        m[0,i] = odd_coeff[i]

    for i in range(0,advait):
        m[1,i] = even_coeff[i]


# Calculation of rest of the entries
for i in range(2,n+1):
    for j in range(1,n):
            m[i,j-1] = ((m[i-1,0]*m[i-2,j]-m[i-2,0]*m[i-1,j])/m[i-1,0])

print(m)

for i in range(2,n+1):
    for j in range(1,n):
        where_are_NaNs = isnan(m)
        m[where_are_NaNs] = 0

print(m)