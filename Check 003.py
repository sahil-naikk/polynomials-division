import fractions
ply1=[]
ply2=[]
rem=[]
qut=[]


# input for the first polynomial
n1= int(input("enter the highest degree of the 1 st poly :"))
n01=n1
for i in range(0,n1+1):

    ele1=input('enter the coefficient of x^'+str(i)+" ")
    ply1.append(ele1)
    qut.append(0)
ply1.append(0)

print(" ")

#to display the first polynomial
print("the  first polynomial is :",end=" ")
for i in range (n1,-1,-1):
    f1=fractions.Fraction(ply1[i])
    if i!=n1 and f1>0:
        print("+",end=" ")
    if(f1!=0):
        temp=1
        print(str(ply1[i])+'x^'+str(i),end=" ")

print(" ")
print(" ")
print(" ")


# input for the second polynomial
n2= int(input("enter the highest degree of the 2 rd poly :"))
n02=n2
for i in range(0,n1+1):
    if i<n2+1:
        
        ele2=input('enter the coefficient of x^'+str(i)+" ")
        ply2.append(ele2)
    else:
        ply2.insert(i,0)
ply2.append(0)

print(" ")
print(" ")

#to display the second polynomial
print("the second polynomial is :",end=" ")
for i in range (n1,-1,-1):
    f1=fractions.Fraction(ply2[i])
    if i!=n2 and f1>0:
        print("+",end=" ")
    if(f1!=0):
        temp=1
        print(str(ply2[i])+'x^'+str(i),end=" ")   


n001=n1
n002=n2
dply1=ply1
dply2=ply2
ddply2=[]



def divpoly(n001,n002,dply1,dply2):
    for i in range(n001,-1,-1):
        f3=fractions.Fraction(dply1[i])
        ddply2=[]
        if f3!=0 and i-n002>-1 :
            if 1>0:
                f1=fractions.Fraction(dply1[i])
                f2=fractions.Fraction(dply2[n002])
                qu=f1/f2
                qut[i-n002]=qu
                for j in range(0,n001+1):
                    f1=fractions.Fraction(dply2[j])
                    f4=f1*qu
                    ddply2.append(f4)
                for k in range (0,i-n002):
                    ddply2.insert(0,0)
                for m in range(0,n1+1):
                    f1=fractions.Fraction(dply1[m])
                    f2=fractions.Fraction(ddply2[m])
                    dply1[m]=f1-f2
    return (qut,dply1)

qut,dply1=divpoly(n1,n2,ply1,ply2)
print(" ")
print(" ")
print(" ")

print("the quotient is :")
for i in range (n1,-1,-1):
    f1=fractions.Fraction(qut[i])
    if i!=n1 and f1>0:
        print("+",end=" ")
    if(f1!=0):
        print(str(qut[i])+'x^'+str(i),end=" ")

print(" ")
print(" ")
print(" ")
print("the remainder is :")
temp=0
for i in range (n1,-1,-1):
    f1=fractions.Fraction(dply1[i])
    if i!=n1 and f1>0:
        print("+",end=" ")
    if(f1!=0):
        temp=1
        print(str(dply1[i])+' x^'+str(i),end=" "),
if(temp!=1):
    print(0)

