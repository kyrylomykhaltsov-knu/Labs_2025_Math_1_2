max_nominal = 121
wallet = {
    2: 4,
    1: 20,
    
    50: 1
}
suma = 0
for i in range(max_nominal + 1):
    try:
        suma += i * wallet[i]
    except KeyError:
        pass

# for key, val in wallet.items():
#     suma += key * val

print(f"у гаманці {suma} у.о.")