#1º Questão
nome = input("Qual o seu nome?")
gen = input("Homem ou Mulher? (h ou m)")
if(gen == "h"):
    print(nome , "É belo")
else:
    print(nome , "É bela")

#2º Questão
num1 = input("Digite o primeiro número ")
num1 = float(num1)
num2 = input("Digite o outro número ")
num2 = float(num2)
soma = num1 + num2
print(num1, "+", num2, "=", soma)

#3º Questão
val = input("Informe o valor do produto ")
val = val.replace(",",".")
val = float(val)
qtd = input("Informe a quantidade do produto ")
qtd = int(qtd)
valtotal = val * qtd
float(valtotal)
print("O valor da compra deu R$", valtotal)

#4º Questão
val = input("Digite o preço da compra ")
val = val.replace(",",".")
val = float(val)
desc = input("Digite o percentual de desconto (Apenas números) ")
desc = int(desc)
desc = desc / 100
valdesc = val - val * desc
print("Preço final: R$" , valdesc, "com desconto de:", desc * 100, "%")

#5º Questão
sal = input("Digite o seu salario ")
sal = sal.replace(",",".")
sal = float(sal)
aumento = input("Digite o percentual de aumento (Apenas números) ")
aumento = int(aumento)
aumento = aumento / 100
saln = sal + sal * aumento
print("O novo salário é: R$", saln, "com um aumento de:", aumento * 100, "%")

#6º Questão
print(28 * 43)

#7º Questão
num1 = input("Digite o primeiro número ")
num1 = num1.replace(",",".")
num1 = float(num1)
num2 = input("Digite o segundo número ")
num2 = num2.replace(",",".")
num2 = float(num2)
num3 = input("Digite o terceiro número ")
num3 = num3.replace(",",".")
num3 = float(num3)
media = (num1 + num2 + num3) / 3
print(media)

#8º Questão
n = input("Digite o número ")
n = float(n)
s = n + 1
a = n - 1
print("Antecessor:" , a , "Número:", n , "Sucessor:", s)

#9º Questão
P1 = 1
P2 = 2
P3 = 3
P4 = 4
n1 = input("Digite o primeiro valor ")
n1 = float(n1)
n2 = input("Digite o segundo valor ")
n2 = float(n2)
n3 = input("Digite o terceiro valor ")
n3 = float(n3)
n4 = input("Digite o quarto valor ")
n4 = float(n4)
somapeso = P1 + P2 + P3 + P4
mediapond = (n1 * P1 + n2 * P2 + n3 * P3 + n4 * P4 )/ somapeso
print(mediapond)

#10º Questão
saldo = input("Digite o saldo ")
saldo = float(saldo)
reajuste = saldo * 0.025
nsaldo = saldo + reajuste
print(nsaldo)

#11º Questão
valor = input("Digite o valor da prestação ")
valor = float(valor)
tempo = input("Digite a quantidade de dias de atraso ")
tempo = int(tempo)
taxa = tempo * 5
prestação = valor + (valor *  (taxa/100) *  tempo)
print(prestação)

#12º Questão
n1 = input("Digite o primeiro número")
n1 = n1.replace(",",".")
n1 = float(n1)
n2 = input("Digite o segundo número")
n2 = n2.replace(",",".")
n2 = float(n2)
print("Soma:", n1 + n2, "\nSubtração:", n1 - n2, "\nMultiplicação:", n1 * n2, "\nDivisão:", n1 / n2, "\n]Resto da divisão:", n1 % n2 )

#13º Questão
base = input("Digite o valor da base")
base = base.replace(",",".")
base = float(base)
altura = input("Digite o valor da altura")
altura = altura.replace(",",".")
altura = float(altura)
per = base * 2 + altura * 2
area = base * altura
print("Perimetro:", per , "\narea:", area)

#14º Questão
altura = input("Digite a altura do triângulo")
altura = altura.replace(",",".")
altura = float(altura)
base = input("Digite o valor da base")
base = base.replace(",",".")
base = float(base)
area = (base * altura) / 2
print("Área do triângulo:", area)

#15º Questão
PI = 3.14
raio = input("Digite o valor do raio")
raio = raio.replace(",",".")
raio = float(raio)
per = 2 * PI * raio
area = PI * raio ** 2
print("Perímetro do círculo:", per, "\nÁrea do círculo:", area)
