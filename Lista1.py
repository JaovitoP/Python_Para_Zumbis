##Faça um programa que peça dois números inteiros e imprima a soma desses dois números
#n1=int(input('Digite o primeiro valor: '))
#n2=int(input('Digite o segundo valor: '))
#soma=n1+n2
#print(soma)

#Escreva um programa que leia um valor em metros e o exiba convertido em milímetro
#Valor_metro=int(input('Digite um valor em metros: '))
#Valor_mili=Valor_metro*1000
#print('O valor em milímetros é igual a:', Valor_mili)

#Escreva um programa que leia a quantidade de dias, horas,
#minutos e segundos do usuário. Calcule
#o total em segundos.
#dia=int(input('Digite a quantidade de dias: '))
#hor=int(input('Digite a quantidade de horas: '))
#minu=int(input('Digite a quantidade de minutos: '))
#seg=int(input('Digite a quantidade de segundos: '))
#dia_seg = dia * 86400
#hor_seg = hor * 3600      
#minu_seg = minu * 60
#soma = dia_seg + hor_seg + minu_seg + seg
#print ('A soma em segundos é igual a:', soma)

#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
#porcentagem do aumento. Exiba o valor do aumento e do novo salário
#sal=float(input('Digite o valor do salário: '))
#aume=float(input('Digite o aumento percentual: '))
#novosal = sal + (sal * (aume/100))
#quantaumen= novosal - sal
#print ('Houve um aumento de R$',quantaumen)
#print ('O novo salário é igual a:',novosal)

#Solicite o preço de uma mercador
#ia e o percentual de desconto. Exiba o valor do desconto e o
#preço a pagar.
#preço=float(input('Digite o preço da mercadoria: '))
#percen=float(input('Digite o percentual de desconto: '))
#novpreço= preço - (preço * (percen/100))
#desc= novpreço - preço
#print ('House um desconto de R$' , desc)
#print ('O valor a pagar será de R$' , novpreço)

#Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média
#esperada para a viagem
#dist=float(input('Digite a distância percorrida em metros: '))
#vmedia=float(input('Digite a velocidade média percorrida: '))
#temp= dist / vmedia
#print ('O tempo percorrido em segundos foi será de:', temp, 'segundos')

#Converta uma temperatura digitada em Celsius para Fahrenheit.
#C=float(input('Digite a temperatura em º celsius: '))
#F= (C * 1.8) + 32
#F = 9*C/5 + 32
#print (C, 'ºC convertido para Farenheit é igual a:', F, 'ºF')

#Fahrenheit para Celsius
#F=float(input('Digite a temperatura em ºFahrenheit: '))
#C = (F - 32) / 1.8
#print (F, 'ºF convertido para Fahrenheit é igual a:', C, 'ºC')

#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
#usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
#km=float(input('Quantos km foram percorridos? '))
#dia=int(input('Quantos dias foram alugados para o uso do carro? '))
#vlr= (km* 0.15) + (60.00 * dia)
#print ('O preço a pagar pelo uso do carro será de R$:', vlr)

#Escreva um programa para
#calcular a redução do tempo de vida de um fumante. Pergunte a
#quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
#perde 1
#0 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
#total de dias.
#cig=int(input('Quantos cigarros você fuma por dia? '))
#ano=int(input('Há quantos anos você fuma? '))
#min_per= (10 * (cig * (ano * 365)))
#dia_per= min_per / 1440
#dia_per= round(dia_per)
#print ('Você perdeu', dia_per ,'dias de vida!')

#Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado
#a um milhão.
print (len(str(2**1000000)))
