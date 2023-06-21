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
A=[]
X=[[0, 9, 209],
[1, 5, 98],
[1, 8, 149],
[1, 12, 137],
[1, 17, 541],
[2, 14, 141],
[3, 4, 58],
[3, 6, 154],
[3, 7, 271],
[3, 8, 339],
[4, 5, 309],
[4, 7, 53],
[4, 8, 301],
[5, 17, 113],
[6, 12, 28],
[6, 14, 136],
[7, 10, 110],
[7, 16, 618],
[8, 17, 136],
[10, 17, 544],
[14, 15, 141]]
F=0
if input()=="NONE":
    F=1
for x in X:
    A.append([x[0],x[1]])
for i in range(17+F):
    for j in range(17+F-i):
        I=i
        J=j+i+1
        if not [I,J] in A:
            X.append([I,J,0])


SCR=[]
for i in X:
    S=0
    for j in X:
        if BATTLE(i,j)==1:
            S+=j[2]
        if i==j:
            S+=j[2]
        if BATTLE(i,j)==-1:
            S-=j[2]
    SCR.append([S,i])
SCR.sort()
SCR.reverse()
POS=1
for i in SCR:
    print(str(POS) + ". "+typenames[i[1][0]]+"/"+typenames[i[1][1]] + " : " + str(i[0]))
    POS+=1
input()


for i in range(17):
    W=[]
    R=[]
    I=[]
    T=types[i]
    print()
    print(typenames[i])
    for j in range(17):
        if T[j]==2:
            W.append(j)
        if T[j]==.5:
            R.append(j)
        if T[j]==0:
            I.append(j)
    print()
    print("Weaknesses :")
    for j in W:
          print(typenames[j])
    print()
    print("Resistances :")
    for j in R:
          print(typenames[j])
    print()
    print("Immunities :")
    for j in I:
          print(typenames[j])
    print()
