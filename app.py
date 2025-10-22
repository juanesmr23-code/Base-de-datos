import tkinter as tk
from tkinter import messagebox, ttk
from producto import Producto
from cliente import Cliente

class TiendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tienda")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        # Configurar estilo
        self.setup_styles()
        
        # Crear notebook para pestañas
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Crear pestañas
        self.create_productos_tab()
        self.create_clientes_tab()
        self.create_informes_tab()
        
    def setup_styles(self):
        """Configurar estilos para la aplicación"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configurar colores
        style.configure('TNotebook.Tab', padding=[20, 10])
        style.configure('TButton', padding=[10, 5])
        style.configure('TLabel', font=('Arial', 10))
        style.configure('TEntry', font=('Arial', 10))
        
    def create_productos_tab(self):
        """Crear pestaña de gestión de productos"""
        # Frame principal para productos
        productos_frame = ttk.Frame(self.notebook)
        self.notebook.add(productos_frame, text="Productos")
        
        # Frame para formulario
        form_frame = ttk.LabelFrame(productos_frame, text="Agregar Producto", padding=10)
        form_frame.pack(fill='x', padx=10, pady=5)
        
        # Campos del formulario
        ttk.Label(form_frame, text="Nombre:").grid(row=0, column=0, sticky='w', pady=2)
        self.entry_nombre = ttk.Entry(form_frame, width=30)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(form_frame, text="Precio:").grid(row=1, column=0, sticky='w', pady=2)
        self.entry_precio = ttk.Entry(form_frame, width=30)
        self.entry_precio.grid(row=1, column=1, padx=5, pady=2)
        
        ttk.Label(form_frame, text="Stock:").grid(row=2, column=0, sticky='w', pady=2)
        self.entry_stock = ttk.Entry(form_frame, width=30)
        self.entry_stock.grid(row=2, column=1, padx=5, pady=2)
        
        ttk.Label(form_frame, text="Categoría:").grid(row=3, column=0, sticky='w', pady=2)
        self.entry_categoria = ttk.Entry(form_frame, width=30)
        self.entry_categoria.grid(row=3, column=1, padx=5, pady=2)
        
        # Botones
        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=10)
        
        ttk.Button(button_frame, text="Guardar Producto", 
                  command=self.guardar_producto).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Actualizar Lista", 
                  command=self.actualizar_lista_productos).pack(side='left', padx=5)
        
        # Frame para lista de productos
        lista_frame = ttk.LabelFrame(productos_frame, text="Lista de Productos", padding=10)
        lista_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Treeview para mostrar productos
        columns = ('ID', 'Nombre', 'Precio', 'Stock', 'Categoría')
        self.tree_productos = ttk.Treeview(lista_frame, columns=columns, show='headings', height=10)
        
        for col in columns:
            self.tree_productos.heading(col, text=col)
            self.tree_productos.column(col, width=120)
        
        # Scrollbar para la lista
        scrollbar_productos = ttk.Scrollbar(lista_frame, orient='vertical', command=self.tree_productos.yview)
        self.tree_productos.configure(yscrollcommand=scrollbar_productos.set)
        
        self.tree_productos.pack(side='left', fill='both', expand=True)
        scrollbar_productos.pack(side='right', fill='y')
        
        # Cargar productos iniciales
        self.actualizar_lista_productos()
        
    def create_clientes_tab(self):
        """Crear pestaña de gestión de clientes"""
        # Frame principal para clientes
        clientes_frame = ttk.Frame(self.notebook)
        self.notebook.add(clientes_frame, text="Clientes")
        
        # Frame para formulario
        form_frame = ttk.LabelFrame(clientes_frame, text="Agregar Cliente", padding=10)
        form_frame.pack(fill='x', padx=10, pady=5)
        
        # Campos del formulario
        ttk.Label(form_frame, text="Nombre:").grid(row=0, column=0, sticky='w', pady=2)
        self.entry_cliente_nombre = ttk.Entry(form_frame, width=30)
        self.entry_cliente_nombre.grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(form_frame, text="Apellidos:").grid(row=1, column=0, sticky='w', pady=2)
        self.entry_apellidos = ttk.Entry(form_frame, width=30)
        self.entry_apellidos.grid(row=1, column=1, padx=5, pady=2)
        
        ttk.Label(form_frame, text="Email:").grid(row=2, column=0, sticky='w', pady=2)
        self.entry_email = ttk.Entry(form_frame, width=30)
        self.entry_email.grid(row=2, column=1, padx=5, pady=2)
        
        ttk.Label(form_frame, text="Historial Compras:").grid(row=3, column=0, sticky='w', pady=2)
        self.entry_historial = ttk.Entry(form_frame, width=30)
        self.entry_historial.grid(row=3, column=1, padx=5, pady=2)
        self.entry_historial.insert(0, "0")  # Valor por defecto
        
        # Botones
        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=10)
        
        ttk.Button(button_frame, text="Guardar Cliente", 
                  command=self.guardar_cliente).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Actualizar Lista", 
                  command=self.actualizar_lista_clientes).pack(side='left', padx=5)
        
        # Frame para lista de clientes
        lista_frame = ttk.LabelFrame(clientes_frame, text="Lista de Clientes", padding=10)
        lista_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Treeview para mostrar clientes
        columns = ('ID', 'Nombre', 'Apellidos', 'Email', 'Historial')
        self.tree_clientes = ttk.Treeview(lista_frame, columns=columns, show='headings', height=10)
        
        for col in columns:
            self.tree_clientes.heading(col, text=col)
            self.tree_clientes.column(col, width=120)
        
        # Scrollbar para la lista
        scrollbar_clientes = ttk.Scrollbar(lista_frame, orient='vertical', command=self.tree_clientes.yview)
        self.tree_clientes.configure(yscrollcommand=scrollbar_clientes.set)
        
        self.tree_clientes.pack(side='left', fill='both', expand=True)
        scrollbar_clientes.pack(side='right', fill='y')
        
        # Cargar clientes iniciales
        self.actualizar_lista_clientes()
        
    def create_informes_tab(self):
        """Crear pestaña de informes"""
        informes_frame = ttk.Frame(self.notebook)
        self.notebook.add(informes_frame, text="Informes")
        
        # Frame para botones de informes
        button_frame = ttk.LabelFrame(informes_frame, text="Informes Disponibles", padding=20)
        button_frame.pack(fill='x', padx=20, pady=20)
        
        ttk.Button(button_frame, text="Valor Total del Inventario", 
                  command=self.valor_inventario).pack(pady=10, fill='x')
        ttk.Button(button_frame, text="Total de Clientes", 
                  command=self.total_clientes).pack(pady=10, fill='x')
        ttk.Button(button_frame, text="Productos por Categoría", 
                  command=self.productos_por_categoria).pack(pady=10, fill='x')
        ttk.Button(button_frame, text="Clientes con Mayor Historial", 
                  command=self.clientes_mayor_historial).pack(pady=10, fill='x')
        
        # Frame para mostrar resultados
        self.resultado_frame = ttk.LabelFrame(informes_frame, text="Resultados", padding=10)
        self.resultado_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        self.text_resultado = tk.Text(self.resultado_frame, height=15, wrap='word')
        scrollbar_resultado = ttk.Scrollbar(self.resultado_frame, orient='vertical', command=self.text_resultado.yview)
        self.text_resultado.configure(yscrollcommand=scrollbar_resultado.set)
        
        self.text_resultado.pack(side='left', fill='both', expand=True)
        scrollbar_resultado.pack(side='right', fill='y')
        
    def guardar_producto(self):
        """Guardar un nuevo producto"""
        try:
            nombre = self.entry_nombre.get()
            precio = float(self.entry_precio.get())
            stock = int(self.entry_stock.get())
            categoria = self.entry_categoria.get()
            
            if not nombre or not categoria:
                messagebox.showwarning("Advertencia", "Por favor completa todos los campos obligatorios")
                return
            
            producto = Producto(nombre, precio, stock, categoria)
            if producto.guardar():
                messagebox.showinfo("Éxito", "Producto guardado correctamente")
                self.limpiar_campos_producto()
                self.actualizar_lista_productos()
            else:
                messagebox.showerror("Error", "Error al guardar el producto")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos para precio y stock")
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {str(e)}")
    
    def guardar_cliente(self):
        """Guardar un nuevo cliente"""
        try:
            nombre = self.entry_cliente_nombre.get()
            apellidos = self.entry_apellidos.get()
            email = self.entry_email.get()
            historial = float(self.entry_historial.get())
            
            if not nombre or not apellidos or not email:
                messagebox.showwarning("Advertencia", "Por favor completa todos los campos obligatorios")
                return
            
            cliente = Cliente(nombre, apellidos, email, historial)
            if cliente.guardar():
                messagebox.showinfo("Éxito", "Cliente guardado correctamente")
                self.limpiar_campos_cliente()
                self.actualizar_lista_clientes()
            else:
                messagebox.showerror("Error", "Error al guardar el cliente")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa un valor numérico válido para el historial")
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {str(e)}")
    
    def limpiar_campos_producto(self):
        """Limpiar campos del formulario de productos"""
        self.entry_nombre.delete(0, 'end')
        self.entry_precio.delete(0, 'end')
        self.entry_stock.delete(0, 'end')
        self.entry_categoria.delete(0, 'end')
    
    def limpiar_campos_cliente(self):
        """Limpiar campos del formulario de clientes"""
        self.entry_cliente_nombre.delete(0, 'end')
        self.entry_apellidos.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.entry_historial.delete(0, 'end')
        self.entry_historial.insert(0, "0")
    
    def actualizar_lista_productos(self):
        """Actualizar la lista de productos"""
        # Limpiar lista actual
        for item in self.tree_productos.get_children():
            self.tree_productos.delete(item)
        
        # Obtener productos de la base de datos
        productos = Producto.listar()
        for producto in productos:
            self.tree_productos.insert('', 'end', values=producto)
    
    def actualizar_lista_clientes(self):
        """Actualizar la lista de clientes"""
        # Limpiar lista actual
        for item in self.tree_clientes.get_children():
            self.tree_clientes.delete(item)
        
        # Obtener clientes de la base de datos
        clientes = Cliente.listar()
        for cliente in clientes:
            self.tree_clientes.insert('', 'end', values=cliente)
    
    def valor_inventario(self):
        """Calcular valor total del inventario"""
        productos = Producto.listar()
        total = sum(p[2] * p[3] for p in productos)  # precio * stock
        resultado = f"VALOR TOTAL DEL INVENTARIO\n"
        resultado += f"{'='*40}\n"
        resultado += f"Total de productos: {len(productos)}\n"
        resultado += f"Valor total: ${total:,.2f}\n\n"
        
        resultado += "Detalle por producto:\n"
        resultado += "-" * 40 + "\n"
        for p in productos:
            valor_producto = p[2] * p[3]
            resultado += f"{p[1]}: {p[3]} unidades × ${p[2]:.2f} = ${valor_producto:,.2f}\n"
        
        self.mostrar_resultado(resultado)
    
    def total_clientes(self):
        """Mostrar total de clientes"""
        clientes = Cliente.listar()
        resultado = f"TOTAL DE CLIENTES\n"
        resultado += f"{'='*30}\n"
        resultado += f"Total de clientes registrados: {len(clientes)}\n\n"
        
        if clientes:
            resultado += "Lista de clientes:\n"
            resultado += "-" * 30 + "\n"
            for c in clientes:
                resultado += f"• {c[1]} {c[2]} ({c[3]})\n"
        
        self.mostrar_resultado(resultado)
    
    def productos_por_categoria(self):
        """Mostrar productos agrupados por categoría"""
        productos = Producto.listar()
        categorias = {}
        
        for p in productos:
            categoria = p[4]
            if categoria not in categorias:
                categorias[categoria] = []
            categorias[categoria].append(p)
        
        resultado = f"PRODUCTOS POR CATEGORÍA\n"
        resultado += f"{'='*40}\n\n"
        
        for categoria, prods in categorias.items():
            resultado += f"{categoria.upper()}\n"
            resultado += "-" * 20 + "\n"
            for p in prods:
                resultado += f"  • {p[1]} - ${p[2]:.2f} (Stock: {p[3]})\n"
            resultado += f"  Total en {categoria}: {len(prods)} productos\n\n"
        
        self.mostrar_resultado(resultado)
    
    def clientes_mayor_historial(self):
        """Mostrar clientes ordenados por historial de compras"""
        clientes = Cliente.listar()
        clientes_ordenados = sorted(clientes, key=lambda x: x[4], reverse=True)
        
        resultado = f"CLIENTES CON MAYOR HISTORIAL DE COMPRAS\n"
        resultado += f"{'='*50}\n\n"
        
        if clientes_ordenados:
            for i, c in enumerate(clientes_ordenados, 1):
                resultado += f"{i}. {c[1]} {c[2]}\n"
                resultado += f"   Email: {c[3]}\n"
                resultado += f"   Historial: ${c[4]:,.2f}\n\n"
        else:
            resultado += "No hay clientes registrados.\n"
        
        self.mostrar_resultado(resultado)
    
    def mostrar_resultado(self, texto):
        """Mostrar resultado en el área de texto"""
        self.text_resultado.delete(1.0, 'end')
        self.text_resultado.insert(1.0, texto)

def main():
    root = tk.Tk()
    app = TiendaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

