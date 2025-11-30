# MessagePack Cliente-Servidor

Implementación de un sistema cliente-servidor utilizando MessagePack para la serialización de datos de telemetría.

## Requisitos Previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)
- make (GNU Make)

## Instalación

### Crear entorno virtual e instalar dependencias

Usando el Makefile:

```bash
make install
```

Esto:

- Creará un entorno virtual en el directorio `venv`
- Actualizará pip a la última versión
- Instalará todas las dependencias desde [`requirements.txt`](requirements.txt)

## Ejecución

**Terminal 1 - Iniciar el Servidor:**

```bash
make run-server
```

El servidor se iniciará y escuchará en `localhost:6006`.

**Salida esperada:**

```plaintext
Servidor MessagePack escuchando en localhost:6006
Esperando conexiones...
```

**Terminal 2 - Iniciar el Cliente:**

```bash
make run-client
```

El cliente se conectará al servidor, enviará datos de telemetría y recibirá la respuesta.

**Salida esperada:**

```plaintext
Conectado al servidor en localhost:6006
Datos enviados: {...}
Respuesta recibida: {...}
Conexión cerrada
```

## Detener la Ejecución

Para detener el servidor o el cliente:

- Presiona `Ctrl+C` en la terminal correspondiente

## Limpiar Archivos

### Limpiar caché de Python

```bash
make clean
```

Esto eliminará el directorio `__pycache__`.

### Limpiar todo (incluyendo entorno virtual)

```bash
make distclean
```

Esto eliminará:

- Directorio `__pycache__`
- Directorio `venv` (entorno virtual completo)

**Nota:** Después de `make distclean`, necesitarás ejecutar `make install` nuevamente.

## Comandos del Makefile

| Comando | Descripción |
|---------|-------------|
| `make install` | Crea el entorno virtual e instala dependencias |
| `make run-server` | Ejecuta el servidor |
| `make run-client` | Ejecuta el cliente |
| `make clean` | Elimina archivos de caché de Python |
| `make distclean` | Elimina caché y entorno virtual |

## Estructura de Datos

El sistema utiliza mensajes de telemetría con la siguiente estructura:

```python
{
    'timestamp': <timestamp_actual>,
    'device_id': 'sensor_001',
    'temperature': 23.5,
    'humidity': 65.0,
    'pressure': 1013.25
}
```

## Verificar Estado

Para verificar que el servidor está ejecutándose:

```bash
ps aux | grep server.py
```

Para verificar que el puerto está en uso:

```bash
netstat -tulpn | grep 65432
# o
ss -tulpn | grep 65432
```

## Solución de Problemas

### Error: "make: command not found"

Instala GNU Make:

```bash
# Ubuntu/Debian
sudo apt-get install build-essential

# Fedora/RHEL
sudo dnf install make

# Arch Linux
sudo pacman -S make
```

### Error: "Connection refused"

- Asegúrate de que el servidor esté ejecutándose: `make run-server`
- Verifica que el puerto 65432 no esté en uso: `netstat -tulpn | grep 65432`
- Espera unos segundos después de iniciar el servidor antes de ejecutar el cliente

### Error: "No module named 'msgpack'"

Ejecuta la instalación:

```bash
make install
```

### Error de puerto en uso

Si el puerto 65432 ya está en uso:

1. Encuentra el proceso: `lsof -i :6006`
2. Detén el proceso: `kill -9 <PID>`
3. O modifica el puerto en [`server.py`](server.py) y [`client.py`](client.py)

### Problemas con el entorno virtual

Si tienes problemas con el entorno virtual, límpialo y reinstala:

```bash
make distclean
make install
```

## Comparación con Protocol Buffers

Para comparar con la implementación de Protocol Buffers, consulta el directorio [`ProtocolBuffers`](../ProtocolBuffers)

## Licencia

Ver archivo [`LICENSE`](../LICENSE) en el directorio raíz del proyecto.
