import random
NOR=[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 2, 1, 1, 1, 0]
#   [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, A, B, C, D, E, F, G, H]
WAT=[ 1,.5, 1, 2,.5, 1, 1, 2, 1, 1,.5, 1,.5, 1, 1, 1, 1, 1, 0]
PSY=[ 1, 1,.5, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1,.5, 2, 1, 1, 0]
#   [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, A, B, C, D, E, F, G, H]
ELE=[ 1, 1, 1,.5,.5, 1, 1, 1,.5, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0]
STE=[.5, 1,.5, 1,.5,.5,.5,.5,.5, 1, 2,.5,.5, 0, 2, 1,.5, 2, 0]
#   [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, A, B, C, D, E, F, G, H]
DRA=[ 1,.5, 1,.5, 1, 2, 2,.5, 1, 1,.5, 1, 2, 1, 1, 1, 1, 1, 0]
FAI=[ 1, 1, 1, 1, 2, 0, 1, 1, 1, 1, 1,.5, 1, 2,.5,.5, 1, 1, 0]
#   [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, A, B, C, D, E, F, G, H]
GRA=[ 1,.5, 1,.5, 1, 1, 1,.5, 2, 1, 2, 2, 2, 2, 1, 1, 1,.5, 0]
FLY=[ 1, 1, 1, 2, 1, 1, 1,.5, 1, 1, 1,.5, 2, 1,.5, 1, 2, 0, 0]
#   [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, A, B, C, D, E, F, G, H]
GHO=[ 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1,.5, 1,.5, 0, 2, 1, 1, 0]
FIR=[ 1, 2, 1, 1,.5, 1,.5,.5, 1, 1,.5,.5,.5, 1, 1, 1, 2, 2, 0]
#   [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, A, B, C, D, E, F, G, H]
BUG=[ 1, 1, 1, 1, 1, 1, 1,.5, 2, 1, 2, 1, 1, 1,.5, 1, 2,.5, 0]
ICE=[ 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1,.5, 1, 2, 1, 2, 1, 0]
#   [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, A, B, C, D, E, F, G, H]
POI=[ 1, 1, 2, 1, 1, 1,.5,.5, 1, 1, 1,.5, 1,.5,.5, 1, 1, 2, 0]
FIG=[ 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1,.5, 1, 1, 1,.5,.5, 1, 0]
#   [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, A, B, C, D, E, F, G, H]
DAR=[ 1, 1, 0, 1, 1, 1, 2, 1, 1,.5, 1, 2, 1, 1, 2,.5, 1, 1, 0]
ROC=[.5, 2, 1, 1, 2, 1, 1, 2,.5, 1,.5, 1, 1,.5, 2, 1, 1, 2, 0]
#   [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, A, B, C, D, E, F, G, H]
GRO=[ 1, 2, 1, 0, 1, 1, 1, 2, 1, 1, 1, 1, 2,.5, 1, 1,.5, 1, 0]
NON=[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
types=[NOR,WAT,PSY,ELE,STE,DRA,FAI,GRA,FLY,GHO,FIR,BUG,ICE,POI,FIG,DAR,ROC,GRO,NON]
typenames=["NOR","WAT","PSY","ELE","STE","DRA","FAI","GRA","FLY","GHO","FIR","BUG","ICE","POI","FIG","DAR","ROC","GRO","NON"]
team=[]
LLL=[]
def BATTLE(G1,G2):
    stat1=[]
    stat2=[]
    for s in range(19):
        stat1.append(types[G1[0]][s]*types[G1[1]][s])
    for s in range(19):
        stat2.append(types[G2[0]][s]*types[G2[1]][s])
    if max(stat1[G2[0]],stat1[G2[1]]) < max(stat2[G1[0]],stat2[G1[1]]):
        return 1
    if max(stat1[G2[0]],stat1[G2[1]]) == max(stat2[G1[0]],stat2[G1[1]]):
        return 0
    if max(stat1[G2[0]],stat1[G2[1]]) > max(stat2[G1[0]],stat2[G1[1]]):
        return -1

X=[]
F=0
if input()=="NONE":
    F=1
for x in X:
    A.append([x[0],x[1]])
for i in range(17+F):
    for j in range(17+F-i):
        I=i
        J=j+i+1

while True:
    for ii in range(1):
        AVG=[]
        for I in range(len(X)):
            AVG.append([])
        for x in range(200):
            NM=0
            V=[]
            for i in X:
                W=[]
                L=[]
                D=[]
                s=0
                for j in X:
                    if BATTLE(i,j)==1:
                        W.append(j)
                    if BATTLE(i,j)==0:
                        D.append(j)
                    if BATTLE(i,j)==-1:
                        L.append(j)
                T=0
                for w in W:
                    s+=w[-1]*i[-1]
                    T+=w[-1]
                for d in D:
                    s+=d[-1]*i[-1]*1/2
                for l in L:
                    T-=l[-1]
                V.append(s)
                NM+=1
                #if x+ii==0:
                    #print(str(T)+" : " + str(NM))
            S=sum(V)
            l=0
            for i in X:
                i[-1]=V[0]/S
                AVG[l].append(V[0]/S)
                l+=1
                V.pop(0)
        S=0
        for i in AVG:
            S+=sum(i)/len(i)
        for i in X:
            i[-1]=sum(AVG[0])/len(AVG[0])/S
            AVG.pop(0)
    for x in X:
        if x[-1]>10**-25:
            print(x)
    input()
