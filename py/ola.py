import sys
print( "Sistema %d " % sys.version)
a = [5,10,3]
try:
    print(a[3])
except IndexError:
    print("O Indice Inserido Nao Exite , Obrg")
