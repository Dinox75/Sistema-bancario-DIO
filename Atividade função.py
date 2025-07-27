def calcular_total(consumo, tipo):
    if tipo == "R":
        if consumo <= 500:
            return 0.40
        else:
            return 0.65
    elif tipo == "C":
        if consumo <= 1000:
            return 0.55
        else:
            return 0.60
    elif tipo == "I":
        if consumo <= 5000:
            return 0.5
        else:
            return 0.60

c = int(input("Entre com o consumo (kWh): "))
t = input("Entre com o tipo de consumidor (R, C ou I): ").upper()
preco = calcular_total(c, t)
total = c * preco
print(f"Total a pagar: R$ {total:.2f}")


