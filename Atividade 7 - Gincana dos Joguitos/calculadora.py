import math
def calcula(valor1,valor2,op):
    if op=="+":
        result=valor1+valor2
    if op=="X":
        result=valor1*valor2
    if op=="/":
        result==valor1//valor2
    if op=="-":
        result==valor1-valor2
    return result

num1=int(input("Insira aqui o primeiro valor"))
num2=int(input("Insira aqui o segundo valor"))
operador=str(input("Qual operção deseja realizar?(+,-,X,/)"))
while num2!=math.pi:
    resultado=calcula(num1,num2,operador)
    print("\nO resultado obtido foi de %i"%resultado)
    num1=resultado
    operador=input("\nQual a próxima operção que deseja realizar?(+,-,X,/)\nPara resetar insira a letra c")
    if operador=="c":
        num1=int(input("Insira aqui o primeiro valor"))
        num2=int(input("Insira aqui o segundo valor"))
    else:
        num2=int(input("Insira aqui o próximo valor a ser calculado"))



    
