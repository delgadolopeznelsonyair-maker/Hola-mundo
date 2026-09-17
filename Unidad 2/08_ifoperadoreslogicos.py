edad=19
tiene_credencial=True
tiene_adeudo=True

if edad >= 18:
    es_mayor_de_edad = True
else: 
    es_mayor = False
documento_valido = tiene_credencial
if not tiene_adeudo:
    sin_adeudo = True
else:
    sin_adeudo = False
if es_mayor_de_edad and documento_valido and sin_adeudo:
    autorizado = True
else:
    autorizado = False
print(autorizado)