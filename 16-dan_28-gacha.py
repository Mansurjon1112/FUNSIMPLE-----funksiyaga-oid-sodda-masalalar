import math 
#12
'''
def SortInc(a,b,c):
    if a>b:
        a,b=b,a
    if a>c:
        a,c=c,a
    if b>c:
        b,c=c,b
    return (a,b,c)
#def sortinc(sonlar):
#    a=list(s)
#    return a.sort()
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
#s=[5,6,-9]
print(SortInc(a,b,c))
#print(sortinc(s))
'''
#16
'''
def ishora_aniqla(son):
    if son<0:
        return -1
    elif son==0:
        return 0
    else:
        return 1
print(ishora_aniqla(5))    
print(ishora_aniqla(-7))    
print(ishora_aniqla(0))    
'''
#17
'''
def kv_ildiz(a,b,c):
    d=b*b-4*a*c
    if d>0:
        return 2
    elif d==0:
        return 1
    else:
        return 0
a=5
b=54
c=3
print(f'Kvadrat tenglamaning ildizlari\n soni:{kv_ildiz(a,b,c)}') 
'''
#18
'''
def doira_yuzi(r):
    pi=3.1415   
    return pi*r*r
print(doira_yuzi(1))
print(doira_yuzi(2))
print(doira_yuzi(9))
'''
#19
'''
def halqa_yuzi(r1,r2):
    pi=3.1415   
    return abs(pi*(r1*r1-r2*r2))
print(halqa_yuzi(9,5))
print(halqa_yuzi(2,1))
print(halqa_yuzi(10,8))
'''
#20
'''
def TriangleP(a,b):
    c=(a*a+b*b)**0.5
    p=a+b+c
    return p
print(TriangleP(3, 4))
print(TriangleP(5, 12))
'''
#21
'''
def SumRange(A, B):
    s=0
    if A>B:
        return 0
    else:
        for i in range(A,B+1,1):
            s=s+i
    return s
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))

print(SumRange(a,b))
print(SumRange(b,c))
'''
#22
'''
def calc(a,b,amal):
    if amal == 1:
        return a-b
    elif amal == 2:
        return a*b
    elif amal == 3:
        return a/b
    else: 
        return a+b
print(calc(5,6,1))    
print(calc(5,6,2))    
print(calc(5,6,3))    
print(calc(5,6,4))    
'''
#23
'''
def Quarter(x,y):
   if x>0 and y>0 :
       return 1
   elif x<0 and y>0 :
       return 2
   elif x<0 and y<0:
       return 3
   else:
       return 4
print(Quarter(5, 7))    
print(Quarter(-5, 7))    
print(Quarter(5, -7))    
print(Quarter(-5, -7))
'''
#24
'''
def Even(K):
    if K%2==0:
        return "True"
    else:
        return "False"
print(Even(8))
print(Even(5))
print(Even(4))
'''
#25
'''
def isSquare(k):
    m=k**0.5
    #if math.floor(m)**2 == k:
    if int(m)**2 ==k:
        return "True"
    else:
        return "False" 
print(isSquare(16))
print(isSquare(15))
'''
#26
'''
def IsPower5(K):
    while K>1:
        K=K/5
    if K==1:
        return "True"
    else:
        return "False"
print(IsPower5(620))
print(IsPower5(125))        
print(IsPower5(120))
print(IsPower5(20))
'''
#27
#Gulbahor Raxmonova, [15.07.21 22:06]
'''
def  IsPowerN(K, N):
    while K>1:
        K=K/N
    if K == 1:
        return "True"
    else:
        return "False"
print(IsPowerN(8, 2))
print(IsPowerN(9, 3))
print(IsPowerN(19, 2))
'''
#28
def IsPrime(N):
    ''' Kiritilgan sonning 
    tub son ekanligini tekshirish'''
    i = 2 #bo'luvchi
    while (i<=N) and (N % i != 0) :
        i+=1
    if i==N:
        return True
    else:
        return False
sanoq = 0
for i in range(5):
    a=int(input('Son kiriting: '))
    if IsPrime(a):
        sanoq+=1
print(f'Kiritilgan sonlarning {sanoq} tasi tub')
