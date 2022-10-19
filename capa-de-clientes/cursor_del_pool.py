from logger_base import log
from conexion import Conexion

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug('Se ejecuta método __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug('Se ejecuta método __exit__')
        if exc_val:
            self._conexion.rollback()
            log.error(f'Ocurrió una excepcion, se produce rollback: \n {exc_val} | {exc_type} | {exc_tb} |')
        else:
            self._conexion.commit()
            log.debug('Commit de la transacción')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)


if __name__ == '__main__':
        with CursorDelPool() as cursor:
            log.debug('Dentro del bloque with')
            cursor.execute('SELECT * FROM public.clientes ORDER BY id_cliente ASC LIMIT 5')
            log.debug(cursor.fetchall())

