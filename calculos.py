
productos = ["Alfajor", "Gaseosa", "Chicle", "Agua"]
precios = [1500, 2800, 500, 1800]

def buscar_posicion(lista, nombre):
    for i in range(len(lista)):
        if lista[i] == nombre:
            return i
    return -1


#buscar posicion del precio y subtotal


EFECTIVO = "Efectivo"
TRANSFERENCIA = "Transferencia"
 
def aplicar_descuento(monto, forma_pago):
    # 10% de descuento solo en efectivo
    if forma_pago == EFECTIVO:
        return round(monto - monto * 10 / 100, 2)
    return monto

 
def calcular_iva(monto):
    return round(monto * 21 / 100, 2)










