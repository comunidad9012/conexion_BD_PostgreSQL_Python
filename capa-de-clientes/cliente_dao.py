from cursor_del_pool import CursorDelPool
from cliente import Cliente
from logger_base import log


class ClienteDAO:
    _SELECCIONAR = 'SELECT * FROM clientes ORDER BY id_cliente ASC'
    _INSERTAR = 'INSERT INTO clientes(nombre_cliente, fecha_nacimiento, direccion, localidad, telefono, email, fecha_alta, grupo_clientes) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE clientes SET nombre_cliente=%s, fecha_nacimiento=%s, direccion=%s, localidad=$s, telefono=%s, email=%s, grupo_clientes=%s WHERE id_cliente=%s'
    _ELIMINAR = 'DELETE FROM clientes WHERE id_cliente=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2],registro[3], registro[4], registro[5],registro[6], registro[7], registro[8]) #Se pasan los valores a Clientes
                clientes.append(cliente)
            return clientes

    @classmethod
    def insertar(cls, cliente):
        with CursorDelPool() as cursor:
            valores = (cliente.nombre_cliente, cliente.fecha_nacimiento, cliente.direccion, cliente.localidad, cliente.telefono, cliente.email, cliente.fecha_alta, cliente.grupo_clientes)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Cliente insertado: {cliente}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, cliente):
        with CursorDelPool() as cursor:
            valores = (cliente.nombre_cliente, cliente.fecha_nacimiento, cliente.direccion, cliente.localidad, cliente.telefono, cliente.email, cliente.grupo_clientes, cliente.id_cliente)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Cliente actualizado: {usuario}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, cliente):
        with CursorDelPool() as cursor:
            valores = (cliente.id_cliente,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Cliente eliminado: {cliente}')
            return cursor.rowcount

if __name__ == '__main__':

    # Eliminar objetos
    # usuario1 = Usuario(id_usuario=2)
    # usuarios_eliminadas = UsuarioDAO.eliminar(usuario1)
    # log.debug(f'Cantidad de usuario/s eliminado/s: {usuarios_eliminadas}')

    # Actualizar objetos
    usuario1 = Usuario(4,'Josebeneg', '1578')
    usuarios_actualizados = UsuarioDAO.actualizar(usuario1)
    log.debug(f'Cantidad de usuario/s actualizado/s: {usuarios_actualizados}')

    # Insertar objetos
    # usuario1 = Usuario(username='alesito123', password='786545')
    # usuarios_insertadas = UsuarioDAO.insertar(usuario1)
    # log.debug(f'Cantidad de usuario/s insertado/s: {usuarios_insertadas}')

    # Seleccionar objetos
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)