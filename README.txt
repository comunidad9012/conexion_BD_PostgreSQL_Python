Instalamos dentro del directorio con la consola cmd (no powershell porque puede no funcionar)

pip install virtualenv

- Luego dentro del directorio deseado donde esté nuestro codigo corremos:

virtualenv env

- Se crea la carpena "env" en el direcctorio

- posteriormente para activar el entorno virtual corremos el siguiente comando, ejecutando un archivo .bat:

env\Scripts\activate.bat #Para activar el entorno virtual en la terminal

env\Scripts\deactivate.bat #Para desactivar el entorno virtual en la terminal




#######################################################################################

Dentro del (env)

corremos:

pip install psycopg2


###############################################################################################

Import de la DB y Conectarse con Python:


Descargar Posgres y en pgAdmin crear una nueva database llamada "test_db_2" 
(Asi fue llamada por default pero en ./capa-de-clientes/conexion.py puede cambiarse el nombre de la db en _DATABASE)

En la nueva base click derecho y darle a la opcion "Restore" y en la ventana que se habre copiar la ruta del archivo .sql para hacer el import de la base de datos 

el archivo se encuentra en: /capa-de-clientes/test_db_2.sql

Clickear en "Restore"

Comprobar que la base de datos "test_db_2" tiene creada la tabla "clientes" en pgAdmin: "test_db_2/Schemas/public/tables"

### Si alta error en pgAdmin para la opcion "Restore", ir a preferencias y en path/binary path/ seleccionar el path de los binarios de PosgreSQL

Por defecto se encuentra en: "C:\Program Files\PostgreSQL\14\bin"

######################################################################################

Para correr el ABM: python \capa-de-clientes\menu_usuario.py

