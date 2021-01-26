def conversor(dolar):

    halfDollar = 0
    quarter = 0
    dime = 0
    nickel = 0
    penny = 0

    dolarConvertido = int(dolar  * 100)

    verf = 0
    sobra = 0
    if dolarConvertido < 50:
        verf = 1
    
    while verf == 0:

        if dolarConvertido % 50 == 0:
            halfDollar = int(dolarConvertido / 50)
            dolarConvertido = (dolarConvertido - (50 * halfDollar)) + sobra
            verf = 1
        else:
            dolarConvertido = dolarConvertido - 1
            sobra = sobra + 1
    
    verf = 0
    sobra = 0
    if dolarConvertido < 25:
        verf = 1
    
    while verf == 0:

        if dolarConvertido % 25 == 0:
            quarter = int(dolarConvertido / 25)
            dolarConvertido = (dolarConvertido - (25 * quarter)) + sobra
            verf = 1
        else:
            dolarConvertido = dolarConvertido - 1
            sobra = sobra + 1

    verf = 0
    sobra = 0
    if dolarConvertido < 10:
        verf = 1
    
    while verf == 0:

        if dolarConvertido % 10 == 0:
            dime = int(dolarConvertido / 10)
            dolarConvertido = (dolarConvertido - (10 * dime)) + sobra
            verf = 1
        else:
            dolarConvertido = dolarConvertido - 1
            sobra = sobra + 1
    
    verf = 0
    sobra = 0
    if dolarConvertido < 5:
        verf = 1
    
    while verf == 0:

        if dolarConvertido % 5 == 0:
            nickel = int(dolarConvertido / 5)
            dolarConvertido = (dolarConvertido - (5 * nickel)) + sobra
            verf = 1
        else:
            dolarConvertido = dolarConvertido - 1
            sobra = sobra + 1

    verf = 0
    sobra = 0
    if dolarConvertido < 1:
        verf = 1
    
    while verf == 0:

        if dolarConvertido % 1 == 0:
            penny = int(dolarConvertido / 1)
            dolarConvertido = (dolarConvertido - (1 * penny)) + sobra
            verf = 1
        else:
            dolarConvertido = dolarConvertido - 1
            sobra = sobra + 1

    totalMoedas = halfDollar + quarter + dime + nickel + penny

    return print("Se você tem $" + str(dolar) + ", você vai ter " + str(totalMoedas) + " moedas: " + str(halfDollar) + " half-dollar, " 
    + str(quarter) + " quarter, " + str(dime) + " dime, " + str(nickel) + " nickel, " + str(penny) + " penny.")

dinheiro = float(input("Quantos dolares você tem: "))

conversor(dinheiro)