poupança = float(input("Insira aqui o valor que deseja investir, para saber quanto rendera em um mês!!!"))
taxa = 0.013
prazo = 1
montante = round(poupança * pow((1+taxa),prazo), 3)
juros = round((montante - poupança),2)
print("O valor total após um mê sde aplicação será de: ", montante)
print("O valor total do rendimento foi de:  ", juros)