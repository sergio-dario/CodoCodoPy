import sqlite3

def crear_tabla_si_no_existe():
    # Conexión a la base de datos
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    
    # Crear tabla si no existe
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS inventario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT NOT NULL,
                cantidad INTEGER NOT NULL CHECK(cantidad >= 0),
                precio REAL NOT NULL CHECK(precio >= 0),
                categoria TEXT NOT NULL
            )
        ''')
    conexion.commit()
    conexion.close()

def registrar_producto():
    # asegura que la tabla exista
    crear_tabla_si_no_existe()

    try:
        # Conexión a la base de datos
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        
        # Pido los datos del producto que se descea registrar
        nombre = input("Nombre: ").strip()
        descripcion = input("Descripción: ").strip()
        
        # Valida cantidad
        while True:
            try:
                cantidad = int(input("Cantidad: "))
                if cantidad > 0:
                    break
                print("La cantidad debe ser un número mayor que 0.")
            except ValueError:
                print("Ingrese un número válido para la cantidad.")
        
        # Valida precio
        while True:
            try:
                precio = float(input("Precio: "))
                if precio > 0:
                    break
                print("El precio debe ser un número mayor que 0.")
            except ValueError:
                print("Ingrese un número válido para el precio.")
        
        # Pide categoría
        categoria = input("Categoría: ").strip()
        
        # Insertar el producto en la base de datos
        cursor.execute(''' 
            INSERT INTO inventario (nombre, descripcion, cantidad, precio, categoria) 
            VALUES (?, ?, ?, ?, ?)
        ''', (nombre, descripcion, cantidad, precio, categoria))
        
        # Confirmar los cambios
        conexion.commit()
        print(f"Producto '{nombre}' registrado con éxito.")
    
    except sqlite3.Error as e:
        print(f"Error al registrar el producto: {e}")
    
    finally:
        # Cierrar la conexión
        if conexion:
            conexion.close()

# Función para mostrar productos
def mostrar_todos_los_productos():
    crear_tabla_si_no_existe()

    try:
        # Conexión a la base de datos
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        
        # Consultar todos los productos
        cursor.execute("SELECT * FROM inventario")
        productos = cursor.fetchall()
        
        if productos:
            print("\nInventario de productos:")
            print("-" * 60)
            print(f"{'ID':<5} {'Nombre':<15} {'Cantidad':<10} {'Precio':<10} {'Categoría':<15}")
            print("-" * 60)
            for producto in productos:
                print(f"{producto[0]:<5} {producto[1]:<15} {producto[3]:<10} ${producto[4]:<10.2f} {producto[5]:<15}")
            print("-" * 60)
        else:
            print("No hay productos registrados en el inventario.")
    
    except sqlite3.Error as e:
        print(f"Error al mostrar los productos: {e}")
    
    finally:
        # Cerrar la conexión
        if conexion:
            conexion.close()

# Función para eliminar producto
def eliminar_producto_por_id():
    crear_tabla_si_no_existe()

    try:
        # Conexión a la base de datos
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        
        # Pide el ID del producto a eliminar
        while True:
            try:
                producto_id = int(input("ID del producto a eliminar: "))
                break
            except ValueError:
                print("Por favor, ingresa un número válido para el ID.")
        
        # Verificar si el producto existe
        cursor.execute("SELECT * FROM inventario WHERE id = ?", (producto_id,))
        producto = cursor.fetchone()
        
        if producto:
            # Elimina el producto
            cursor.execute("DELETE FROM inventario WHERE id = ?", (producto_id,))
            conexion.commit()
            print(f"El producto con ID {producto_id} ha sido eliminado con éxito.")
        else:
            print(f"No se encontró ningún producto con el ID {producto_id}.")
    
    except sqlite3.Error as e:
        print(f"Error al eliminar el producto: {e}")
    
    finally:
        # Cerrar la conexión
        if conexion:
            conexion.close()

# Función para buscar producto por ID
def buscar_producto_por_id():
    crear_tabla_si_no_existe()

    try:
        # Conexión a la base de datos
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        
        # Pide el ID del producto a buscar
        while True:
            try:
                producto_id = int(input("Ingresa el ID del producto a buscar: "))
                break
            except ValueError:
                print("Por favor, ingresa un número válido para el ID.")
        
        # Buscar el producto en la base de datos
        cursor.execute("SELECT * FROM inventario WHERE id = ?", (producto_id,))
        producto = cursor.fetchone()
        
        if producto:
            # Muestra los detalles del producto
            print("\nProducto encontrado:")
            print(f"ID: {producto[0]}")
            print(f"Nombre: {producto[1]}")
            print(f"Descripción: {producto[2]}")
            print(f"Cantidad: {producto[3]}")
            print(f"Precio: ${producto[4]:.2f}")
            print(f"Categoría: {producto[5]}\n")
        else:
            print(f"No se encontró ningún producto con el ID {producto_id}.")
    
    except sqlite3.Error as e:
        print(f"Error al buscar el producto: {e}")
    
    finally:
        # Cerrar la conexión
        if conexion:
            conexion.close()

# Función para actualizar la cantidad de un producto
def actualizar_cantidad_producto():
    crear_tabla_si_no_existe()

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    
    producto_id = int(input("ID del producto: "))
    nueva_cantidad = int(input("Nueva cantidad: "))
    
    cursor.execute("UPDATE inventario SET cantidad = ? WHERE id = ?", 
                   (nueva_cantidad, producto_id))
    conexion.commit()
    conexion.close()
    print("Cantidad actualizada correctamente.")

# Función para generar reporte de bajo stock
def reporte_bajo_stock():
    crear_tabla_si_no_existe()

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    limite_stock = input("Ingrese el límite de stock: ")

    cursor.execute("SELECT * FROM inventario WHERE cantidad <= ?", (limite_stock,))
    resultados = cursor.fetchall()
    
    for producto in resultados:
        print(f"ID: {producto[0]}", 
              "Nombre:", producto[1], 
              "Cantidad:", producto[3], 
              "Precio:", producto[4], 
              "Categoría:", producto[5])
    
    conexion.close()
