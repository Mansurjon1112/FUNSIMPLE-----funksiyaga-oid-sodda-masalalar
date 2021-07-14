#1 
'''
def PowerA3(son):
    return son**3

print(PowerA3(float(input('A='))))
print(PowerA3(float(input('B='))))
print(PowerA3(float(input('C='))))
print(PowerA3(int(input('D='))))
print(PowerA3(int(input('E='))))
'''
#2 
'''
def PowerA234(son):
    return son**2, son**3, son**3

print(PowerA234(float(input('A='))))
print(PowerA234(float(input('B='))))
print(PowerA234(float(input('C='))))
'''
#3
'''
def MEAN(*son):
    a=(son[0]+son[1])/2
    b=(son[0]*son[1])**0.5
    return a,b

a=int(input('A='))
b=int(input('B='))
c=int(input('C='))
d=int(input('D='))

print(MEAN(a,b))
print(MEAN(a,c))
print(MEAN(a,d))
'''
#4
'''
def Triangle (a):
    p=3*a
    s=3**0.5*a**2 / 4
    return p,s

a=int(input('1-uchburchak tomoni: '))
b=int(input('2-uchburchak tomoni: '))
c=int(input('3-uchburchak tomoni: '))

print(Triangle(a))
print(Triangle(b))
print(Triangle(c))
'''
#5
'''
def RectPS(x1,y1,x2,y2):
    a=abs(x1-x2)
    b=abs(y1-y2)
    p=2*(a+b)
    s=a*b
    return p,s

print(RectPS(5, 6, -3, -1))
print(RectPS(12, 1, 1, 8))
'''
#6
'''
def DigitCountSum(son):
    uzunligi = len(str(son))
    s=0
    for i in str(son):
        s+=int(i)
    return uzunligi,s

print(DigitCountSum(15264))        
print(DigitCountSum(1212121212))        
print(DigitCountSum(10000))   
'''
#7 
'''
def InvertDigit(son):
    s=str(son)
    return s[::-1]
print(InvertDigit(12345))
print(InvertDigit(98765))
'''
#8
'''
def AddRightDigit(son,raqam):
    return son*10+raqam
    #return str(son)+str(raqam)
print(AddRightDigit(1239, 9))
print(AddRightDigit(1243225, 0))
'''
#9
'''
def AddRightDigit(son,raqam):
    sanoq=0
    a=son
    while son>0:
        sanoq+=1
        son//=10
    return raqam * 10**sanoq + a
    #return str(raqam)+str(son)
print(AddRightDigit(1239, 9))
print(AddRightDigit(1243225, 4))
'''
#10
'''
def Swap(a,b,c,d):
    (a,b) , (d,c) =(d,c),(a,b)
    return (a,b),(c,d)
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
d=int(input('d='))

print(Swap(a,b,c,d))
print(a,b,c,d)

'''
#11
def Minmax(x,y):
    if x>y :
        return(x)
    else:
        return(y)
    
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
d=int(input('d='))

print(Minmax(a,b))
print(Minmax(c,d))
