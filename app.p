from conexion import conectar

class Cliente:
    def __init__(self, nombre, apellidos, email, historial_compras=0):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.historial_compras = historial_compras

    def guardar(self):
        conexion = conectar()
        if conexion:
            cursor = conexion.cursor()
            query = "INSERT INTO clientes (nombre, apellidos, email, historial_compras) VALUES (%s, %s, %s, %s)"
            valores = (self.nombre, self.apellidos, self.email, self.historial_compras)
            cursor.execute(query, valores)
            conexion.commit()
            cursor.close()
            conexion.close()
            return True
        return False

    @staticmethod
    def listar():
        conexion = conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM clientes")
            resultados = cursor.fetchall()
            cursor.close()
            conexion.close()
            return resultados
        return []

    @staticmethod
    def buscar_por_id(id_cliente):
        conexion = conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM clientes WHERE id = %s", (id_cliente,))
            resultado = cursor.fetchone()
            cursor.close()
            conexion.close()
            return resultado
        return None

    def actualizar(self, id_cliente):
        conexion = conectar()
        if conexion:
            cursor = conexion.cursor()
            query = "UPDATE clientes SET nombre = %s, apellidos = %s, email = %s, historial_compras = %s WHERE id = %s"
            valores = (self.nombre, self.apellidos, self.email, self.historial_compras, id_cliente)
            cursor.execute(query, valores)
            conexion.commit()
            cursor.close()
            conexion.close()
            return True
        return False

    @staticmethod
    def eliminar(id_cliente):
        conexion = conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM clientes WHERE id = %s", (id_cliente,))
            conexion.commit()
            cursor.close()
            conexion.close()
            return True
        return False
