#1
#import random
#
#n = random.sample(range(100), 10)
#print(n)
#
#maior = n[0]
#menor = n[0]
#
#for i in range(1, len(n)):
#    if n[i] > maior:
#        maior = n[i]
#    if n[i] < menor:
#        menor = n[i]
#
#print("Maior:", maior)
#print("Menor:", menor)


#2
#import random
#n=random.sample(range(100), 20)
#par=[]
#impar=[]
#for i in n:
#    if i%2==0:
#        par.append(i)
#    else:
#        impar.append(i)

#3
#import random
#k=0
#v1=random.sample(range(1, 101), 10)
#v2=random.sample(range(1, 101), 10)
#v3=[]
#while k < 10:
#    v3.append(v1[k])
#    v3.append(v2[k])
#    k=k+1

#4
#statement='''The Python Software Foundation and the global Python
#community welcome and encou
#rage participation by everyone Our community is based on
#mutual respect tolerance and encouragement and we are working to help each other live up
#to these principles We want our community to be more diverse whoever you are and
#whatever your backgrou
#nd we welcome you'''.split()
#lista=[]
#letras= '''p y t h o n P Y T H O N'''.split()
#for palavra in statement:
#    if palavra[0].lower() in letras:
#        lista.append(palavra)
#    if palavra[-1].lower() in letras:
#        lista.append(palavra)
#print(statement)
#print()
#print(lista)

#5
#statement='''The Python Software Foundation and the global Python
#community welcome and encou
#rage participation by everyone Our community is based on
#mutual respect tolerance and encouragement and we are working to help each other live up
#to these principles We want our community to be more diverse whoever you are and
#whatever your backgrou
#nd we welcome you'''.split()
#lista=[]
#letras= '''p y t h o n P Y T H O N'''.split()
#for palavra in statement:
#    if palavra[0].lower() in letras:
#        lista.append(palavra)
#    if palavra[-1].lower() in letras:
#        lista.append(palavra)
#print(statement)
#print()
#print(lista)
#
#quatro=[]
#for palavra in lista:
#    if len(palavra)>4:
#        quatro.append(palavra)
#print()
#print(quatro)
