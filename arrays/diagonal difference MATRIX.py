a=[] #declaration
n= int(input())
P_D =0
S_D =0
for i in range(0,n):   #where n is the no. of lines you want
    a.append([int(j) for j in input().split()])  #for taking m space separated integers as input
for i in range (0,n):
    for j in range(0,n):
        if i==j:
            P_D +=a[i][j]

        if i+j==n-1:
            S_D +=a[i][j]
#print(P_D)
#print(S_D)
print(abs( P_D - S_D ))#mode function