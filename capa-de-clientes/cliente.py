from logger_base import log

class Cliente:
    def __init__(self, id_cliente=None, nombre_cliente=None, fecha_nacimiento=None, direccion=None, localidad=None, telefono=None, email=None, fecha_alta=None, grupo_clientes=None):
        self._id_cliente = id_cliente
        self._nombre_cliente = nombre_cliente
        self._fecha_nacimiento = fecha_nacimiento
        self._direccion = direccion
        self._localidad = localidad
        self._telefono = telefono
        self._email = email
        self._fecha_alta = fecha_alta
        self._grupo_clientes = grupo_clientes

    def __str__(self):
        return f'''
            - ID cliente: {self._id_cliente}
            - Nombre cliente: {self._nombre_cliente}
            - Fecha nacimiento : {self._fecha_nacimiento}
            - Direccion: {self._direccion}
            - Localidad: {self._localidad}
            - Teléfono: {self._telefono}
            - Email: {self._email}
            - Fecha alta: {self._fecha_alta}
            - Grupo_clientes: {self._grupo_clientes}
        '''

    # Getters and Setters

    # ///////////// ID CLIENTE

    @property
    def id_cliente(self):
        return self._id_cliente

    @id_cliente.setter
    def id_cliente(self, id_cliente):
        self._id_cliente = id_cliente

    # ///////////// NOMBRE CLIENTE

    @property
    def nombre_cliente(self):
        return self._nombre_cliente

    @nombre_cliente.setter
    def nombre_cliente(self, nombre_cliente):
        self._nombre_cliente = nombre_cliente

    #  //////////// FECHA NACIMIENTO

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

    # ///////////// DIRECCION

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion

    # ///////////// LOCALIDAD

    @property
    def localidad(self):
        return self._localidad

    @localidad.setter
    def localidad(self, localidad):
        self._localidad = localidad

    # ///////////// TELEFONO

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono

    # ///////////// EMAIL

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    # ///////////// FECHA ALTA

    @property
    def fecha_alta(self):
        return self._fecha_alta

    @fecha_alta.setter
    def fecha_alta(self, fecha_alta):
        self._fecha_alta = fecha_alta

    # ///////////// GRUPO CLIENTES

    @property
    def grupo_clientes(self):
        return self._grupo_clientes

    @grupo_clientes.setter
    def grupo_cliente(self, grupo_clientes):
        self._grupo_clientes = grupo_clientes



if __name__ == '__main__':
    # Simulando un INSERT
    usuario1 = Usuario( )
    log.debug(usuario1)


    # Simulando un DELETE
    usuario1 = Usuario()
    log.debug(usuario1)