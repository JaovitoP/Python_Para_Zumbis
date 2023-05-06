#a=int(input('Informe o lado A do triângulo: '))
#b=int(input('Informe o lado B do triângulo: '))
#c=int(input('Informe o lado C do triângulo: '))
#elif a == b and b == c:
#    print ('É um triângulo Equilátero!')
#elif a == b and a != c or b==c and b!=a or a==c:
#    print ('É um triângulo Isósceles!')
#else:
#    print('É um triângulo Escaleno!')

#Faça um Programa que leia três números e mostre o maior deles.
#n1=int(input('Digite um número: '))
#n2=int(input('Digite um número: '))
#n3=int(input('Digite um número: '))
#if n1>n2 and n1>n3:
#    print(f'O número {n1} é o maior!')
#elif n2>n1 and n2>n3:
#    print(f'O número {n2} é o maior!')
#else: print(f'O número {n3} é o maior!')
#if n1<n2 and n1<n3:
#    print(f'O número {n1} é o menor!')
#elif n2<n1 and n2<n3:
#    print(f'O número {n2} é o menor!')
#else:
#    print(f'O número {n3} é o menor!')

#6
#area=float(input('Digite a área que será pintada (em metros): '))
#lit_tinta= area / 3
#if lit_tinta <= 18:
#    print('Será comprada 1 lata de tinta')
#else:
#    lit_tinta=int(lit_tinta/18)

#3

#    print(f'Serão compradas {lit_tinta:.2f} latas de tinta')
#preço= lit_tinta * 80
#print(f'Preço: {preço:.2f}')

#por_hora=float(input('Digite o quanto você ganha por hora: '))
#hrs_trab=int(input('Digite o número de horas trabalhadas: '))
#sal_bruto= por_hora * hrs_trab
#ir= sal_bruto - (sal_bruto * 0.11)
#inss= sal_bruto- (sal_bruto* 0.08)
#sindi= sal_bruto - (sal_bruto * 0.05)
#sal_liq= 100- ((100-ir)+(100-inss)+(100-sindi))
#print('---------------------------')
#print (f'a. + Salário Bruto: R${sal_bruto:.2f}')
#print (f'b. - IR (11%): R${ir:.2f}')
#print (f'c. -INSS (8%): R${inss:.2f}')
#print (f'd. -Sindicato (5%): R${sindi:.2f}')
#print (f'e. =Salário Líquido: R$ {sal_liq:.2f}')
#print('---------------------------')


#peso=float(input('Digite o peso dos peixes: '))
#excesso = peso - 50
#multa = excesso * 4
#print (f'Houve um excesso de {excesso:.2f} quilos!')
#print (f'A multa será de {multa:.2f}')
    
peso=float(input('Digite o peso dos peixes: '))
excesso = peso - 50
multa = excesso * 4
if excesso == 0:
    print('Não houve excesso de quilos')
else:
    print (f'Houve um excesso de {excesso:.2f} quilos!')
    print (f'A multa será de {multa:.2f}')
