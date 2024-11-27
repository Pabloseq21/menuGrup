## Definir los productos con el precio de cada uno de estos
precios =  {    "Producto 1": 50000,  
                "Producto 2": 30000,  
                "Producto 3": 20000   }

# Solicitar cantidades que ingresen al terminal 
cantidades = {}

## para los productos en precios pedir que la cantidad ingrese en el terminal 

for producto in precios:
    cantidades[producto] = int(input(f"Ingrese la cantidad deseada de {producto}: "))

## Calcular y demostrar el total del descuento cerrando el comit y abriendo nuevas lineas de codigo
 
print("\nDetalle de la compra:")
total = 0
for producto, cantidad in cantidades.items():
    precio_unitario = precios[producto]

            ## Determinar descuento
    if cantidad >= 20:
        descuento = 0.20
    elif cantidad >= 10:
        descuento = 0.10
    elif cantidad > 5:
        descuento = 0.05
    else:
        descuento = 0.0

             ## Calcular precios
    subtotal = cantidad * precio_unitario
    descuento_total = subtotal * descuento
    precio_final = subtotal - descuento_total

    ## Acumular total y mostrar detalle del producto
    total += precio_final
    print(f"{producto}: {cantidad} unidades x ${precio_unitario:.2f} c/u")
    print(f"  Descuento aplicado: {descuento * 100:.0f}% (-${descuento_total:.2f})")
    print(f"  Precio final: ${precio_final:.2f}")

## Mostrar total de la compra
print(f"\nTotal a pagar:${total:.2f}")