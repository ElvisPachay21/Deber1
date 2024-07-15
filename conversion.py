def millas_a_kilometros(millas):
    # Una milla equivale a 1.609344 kilómetros
    kilometros = millas * 1.609344
    return kilometros

millas = float(input("Ingrese la cantidad de millas a convertir: "))

resultado = millas_a_kilometros(millas)

print(f"{millas} millas equivalen a {resultado} kilómetros")