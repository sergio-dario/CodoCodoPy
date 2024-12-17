import funciones

def mostrar_menu():
    print("\n--- Menú de Inventario ---")
    print("1. Registrar producto")
    print("2. Mostrar todos los productos")
    print("3. Eliminar producto por ID")
    print("4. Buscar producto por ID")
    print("5. Actualizar cantidad de producto")
    print("6. Generar reporte de bajo stock")
    print("7. Salir")

def ejecutar_opcion(opcion):
    if opcion == 1:
        funciones.registrar_producto()
    elif opcion == 2:
        funciones.mostrar_todos_los_productos()
    elif opcion == 3:
        funciones.eliminar_producto_por_id()
    elif opcion == 4:
        funciones.buscar_producto_por_id()
    elif opcion == 5:
        funciones.actualizar_cantidad_producto()
    elif opcion == 6:
        funciones.reporte_bajo_stock()
    elif opcion == 7:
        print("¡Hasta luego!")
        return False
    else:
        print("Opción no válida. Por favor, intente nuevamente.")
    return True

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("\nSeleccione una opción: "))
            if not ejecutar_opcion(opcion):
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
