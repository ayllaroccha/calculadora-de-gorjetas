#Se a conta for de R$ 150,00, divida entre 5 pessoas, com gorjeta de 12%.

#Cada pessoa deverá pagar (150,00 / 5) * 1,12 = 33,6
#Formate o resultado com 2 casas decimais = 33,60

#Dica: Existem 2 maneiras de arredondar um número. Talvez seja necessário pesquisar no Google para resolver isso.💪

#Escreva seu código abaixo desta linha 👇

print("Bem vindo(a) a calculadora de gorjetas")
conta = float(input("Qual foi o valor total da conta? R$ "))
gorjeta = int(input("Qual o valor de gorjeta que você gostaria de dar? \n obs: escolha entre os números a seguir, sem o simbolo da porcentagem: 10, 12 ou 15?"))
pessoas = int(input("Quantas pessoas vão dividir a conta?"))
gorjeta_porcentagem = gorjeta / 100
valor_total_gorjeta = conta * gorjeta_porcentagem
total_conta = conta + valor_total_gorjeta
conta_por_pessoa = total_conta / pessoas
quantia_final = round(conta_por_pessoa, 2)
quantia_final = "{:.2f}".format(conta_por_pessoa)
print(f"Cada pessoa deverá pagar o valor de R$ {quantia_final}")
