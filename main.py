import funciones
from colorama import init, Fore, Back, Style

# Inicializamos colorama para que funcione en todas las plataformas
init(autoreset=True)

def mostrar_menu():
    print(Fore.CYAN + "\n--- Menú de Inventario ---")
    print(Fore.GREEN + "1. Registrar producto")
    print(Fore.GREEN + "2. Mostrar todos los productos")
    print(Fore.GREEN + "3. Eliminar producto por ID")
    print(Fore.GREEN + "4. Buscar producto por ID")
    print(Fore.GREEN + "5. Actualizar cantidad de producto")
    print(Fore.GREEN + "6. Generar reporte de bajo stock")
    print(Fore.RED + "7. Salir")

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
        print(Fore.YELLOW + "¡Hasta luego!")
        return False
    else:
        print(Fore.RED + "Opción no válida. Por favor, intente nuevamente.")
    return True

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input(Fore.YELLOW + "\nSeleccione una opción: "))
            if not ejecutar_opcion(opcion):
                break
        except ValueError:
            print(Fore.RED + "Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()

