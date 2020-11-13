#from numpy import *
import numpy as np
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

m = np.zeros((n,n))

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

print(m, "\n\n")

for i in range(2,n+1):
    for j in range(1,n):
        where_are_NaNs = np.isnan(m)
        m[where_are_NaNs] = 0

print(m)

for i in range(2,n):
    if m.all()==0:
        # print("Advait <3 Neha")
        z = i-1
        max_power = deg - i
        # print(max_power)  

        # for p in range(max_power+1):
        #     pass
        
        # print(p)
        new=[]
        max_power = int(max_power)
        # for u in range(int(max_power/2)):
        #     new.append(u*2)
        # print(new)
        # new.reverse()
        # print(new)

        for b in range(n):
            for p in range(max_power,-1,-2):
                # print(p)
                # print(m[z,b])
                new_dn = p*m[z,b]
                # print(new_dn)
                m[i,b] = new_dn
                max_power = max_power-2
                break

            # h = int(p)*int(m[z,b])
            # print(int(m[z,b]))
            # print(h)
            pass

        break
    
print(m, '\n\n\n')

for i in range(i+1,n):
    for j in range(1,n):
            m[i,j-1] = ((m[i-1,0]*m[i-2,j]-m[i-2,0]*m[i-1,j])/m[i-1,0])

print(m)