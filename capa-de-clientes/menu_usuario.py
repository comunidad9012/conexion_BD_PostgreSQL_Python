from logger_base import log
from cliente_dao import ClienteDAO
from cliente import Cliente
from datetime import datetime


opcion = None

while opcion != 5:
    print(f'''
    Opciones
    1. Listar clientes
    2. Agregar cliente
    3. Actualizar un cliente
    4. Eliminar usuario
    5. Salir
    ''')
    opcion = int(input('Ingrese una opcion (1-5): '))
    if opcion == 1: #SELECCIONAR
        clientes = ClienteDAO.seleccionar()
        for cliente in clientes:
            log.info(cliente)
    elif opcion == 2: #INSERTAR
        nombre_cliente_var = str(input('Ingrese el nombre del cliente: '))
        fecha_nacimiento_var = str(input('Ingrese la fecha de nacimiento del cliente (dd/mm/aaaa): '))
        direccion_var = str(input('Ingrese la direccion del cliente: '))
        localidad_var = str(input('Ingrese la localidad del cliente: '))
        telefono_var = str(input('Ingrese el telefono del cliente: '))
        email_var = str(input('Ingrese el email del cliente: '))
        fecha_alta_var = str(datetime.strftime(datetime.now(),'%d/%m/%Y %H:%M'))
        grupo_clientes_var = str.upper(input('Ingrese el grupo al que pertenece el cliente (1 valor): '))

        cliente = Cliente(nombre_cliente=nombre_cliente_var, fecha_nacimiento=fecha_nacimiento_var, direccion=direccion_var, localidad=localidad_var, telefono=telefono_var, email=email_var, fecha_alta=fecha_alta_var, grupo_clientes=grupo_clientes_var)
        cliente_insertado = ClienteDAO.insertar(cliente)
        log.info(f'Cliente insertado: {cliente_insertado}')
    elif opcion == 3: #ACTUALIZAR
        id_cliente_var = int(input('Ingrese el id del cliente a actualizar: '))
        nombre_cliente_var = str(input('Ingrese el nombre del cliente: '))
        fecha_nacimiento_var = str(input('Ingrese la fecha de nacimiento del cliente(dd/mm/aaaa): '))
        direccion_var = str(input('Ingrese la direccion del cliente: '))
        localidad_var = str(input('Ingrese la localidad del cliente: '))
        telefono_var = str(input('Ingrese el telefono del cliente: '))
        email_var = str(input('Ingrese el email del cliente: '))
        grupo_clientes_var = str.upper(input('Ingrese el grupo al que pertenece el cliente (1 valor): '))

        cliente = Cliente(id_cliente=id_cliente_var ,nombre_cliente=nombre_cliente_var, fecha_nacimiento=fecha_nacimiento_var, direccion=direccion_var, localidad=localidad_var, telefono=telefono_var, email=email_var, grupo_clientes=grupo_clientes_var)
        cliente_actualizado = ClienteDAO.actualizar(cliente)
        log.info(f'Cliente actualizado: {cliente_actualizado}')
    elif opcion == 4: #ELIMINAR
        id_cliente_var = int(input('Escribe el id del cliente a eliminar: '))
        cliente = Cliente(id_cliente=id_cliente_var)
        cliente_eliminado = ClienteDAO.eliminar(cliente)
        log.info(f'Cliente eliminado: {cliente_eliminado}')

    elif opcion == 5:
        log.info('bai')
    else:
        log.info('Ingrese una opcion valida del 1 al 5')