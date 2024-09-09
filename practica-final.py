

tipo_eur_a_mex = 23.70
tipo_usd_a_mex = 20.75

moneda = input("Moneda de Origen? (EUR/USD): ")

monto = float(input("Monto: "))

if moneda.lower() == "eur":
    resultado = monto * tipo_eur_a_mex
    print("El monto de EUR a MXN es: ", resultado)
elif moneda.lower() == "usd":
    resultado = monto * tipo_usd_a_mex
    print("El monto de DOL a MXN es: ", resultado)
else:
    print("No está disponible este tipo de conversión")

