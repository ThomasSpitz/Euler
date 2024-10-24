import pylab
import matplotlib.pyplot as plt
import math

h = 0.01 #pas de la simulation
n = 1000 #nombre d'itérations
a = 3 
b= 4        #coefficients de l'équation différentielle

def equation(y,a,b):
    '''fonction qui retourne le coefficient de la tangente en fonction de y,a et b. On peut la modifier pour résoudre une autre equation différentiel du premier ordre'''
    return (a*y)+b


def Euler_aux(h,n,a,b):
    '''fonction auxiliaire créant les tableau des valeurs prises par la courbe approximative'''
    Tx=[]
    Ty=[]
    x=0
    y=1
    Tx.append(x)
    Ty.append(y)
    for i in range(n):
        x=x+h
        y=y+h*equation(y,a,b)
        Tx.append(x)
        Ty.append(y)
    if h<0:
        Tx.reverse()
        Ty.reverse()
    return Tx,Ty

def Euler(h,n,a,b):
    '''Fonction principale qui dessine la courbe'''
    X=Euler_aux(-h,n,a,b)[0]+Euler_aux(h,n,a,b)[0]
    Y=Euler_aux(-h,n,a,b)[1]+Euler_aux(h,n,a,b)[1]

    plt.plot(X,Y)
    plt.title(str("Résolution numérique de l'equa-diff y'="+str(a)+'y+'+str(b)))
    plt.show()
    
def comparatif(h,n,a,b):
    '''Trace deux courbe, une tracé grâce à l'algorithme d'Euler, l'autre avec la méthode apprise en cours'''
    X=Euler_aux(-h,n,a,b)[0]+Euler_aux(h,n,a,b)[0]
    Y=Euler_aux(-h,n,a,b)[1]+Euler_aux(h,n,a,b)[1]

    C=1+b/a
    X2=X
    Y2=[]
    for x in X2:
        Y2.append(C*math.exp(a*x)-b/a)

    plt.plot(X,Y)
    plt.plot(X2,Y2,color='red')
    plt.title(str("Résolution numérique de l'equa-diff y'="+str(a)+'y+'+str(b)))
    plt.show()

comparatif(h,n,a,b)