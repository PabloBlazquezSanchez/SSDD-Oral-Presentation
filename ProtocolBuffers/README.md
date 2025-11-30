# Protocol Buffers Cliente-Servidor

Implementación de un sistema cliente-servidor utilizando Protocol Buffers (gRPC) para la serialización de datos de telemetría.

## Requisitos Previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)
- make (GNU Make)
- Protocol Buffers compiler

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

### Compilar archivos Protocol Buffers

Después de instalar las dependencias, compila el archivo `.proto`:

```bash
make proto
```

Esto generará los archivos:

- `telemetry_pb2.py` (mensajes Protocol Buffers)
- `telemetry_pb2_grpc.py` (servicios gRPC)

**Nota:** Este paso es **obligatorio** antes de ejecutar el servidor o cliente.

### Instalación completa (recomendado)

Para instalar dependencias y compilar los archivos proto en un solo comando:

```bash
make all
```

Esto ejecutará `make install` seguido de `make proto`.

## Ejecución

**Terminal 1 - Iniciar el Servidor:**

```bash
make run-server
```

El servidor gRPC se iniciará y escuchará en `localhost:5005`.

**Salida esperada:**

```plaintext
Servidor gRPC escuchando en [::]:50051
Esperando conexiones...
```

**Terminal 2 - Iniciar el Cliente:**

```bash
make run-client
```

El cliente se conectará al servidor, enviará datos de telemetría y recibirá la respuesta.

**Salida esperada:**

```plaintext
Conectado al servidor en localhost:50051
Datos enviados: {...}
Respuesta recibida: {...}
Conexión cerrada
```

## Detener la Ejecución

Para detener el servidor o el cliente:

- Presiona `Ctrl+C` en la terminal correspondiente

## Limpiar Archivos

### Limpiar archivos generados y caché

```bash
make clean
```

Esto eliminará:

- `telemetry_pb2.py`
- `telemetry_pb2_grpc.py`
- Directorio `__pycache__`

**Nota:** Después de `make clean`, necesitarás ejecutar `make proto` nuevamente antes de ejecutar el servidor o cliente.

### Limpiar todo (incluyendo entorno virtual)

```bash
make distclean
```

Esto eliminará:

- Archivos generados por Protocol Buffers
- Directorio `__pycache__`
- Directorio `venv` (entorno virtual completo)

**Nota:** Después de `make distclean`, necesitarás ejecutar `make all` nuevamente.

## Comandos del Makefile

| Comando | Descripción |
|---------|-------------|
| `make all` | Instala dependencias y compila archivos proto |
| `make install` | Crea el entorno virtual e instala dependencias |
| `make proto` | Compila el archivo telemetry.proto |
| `make run-server` | Ejecuta el servidor gRPC |
| `make run-client` | Ejecuta el cliente gRPC |
| `make clean` | Elimina archivos generados y caché |
| `make distclean` | Elimina todo (archivos generados, caché y venv) |

## Estructura de Archivos

### Archivo Proto ([`telemetry.proto`](telemetry.proto))

Define los mensajes y servicios gRPC:

```protobuf
syntax = "proto3";

message DatosSensor {
  int32 id_dispositivo = 1;
  string ubicacion = 2;
  repeated float lecturas = 3;
  bool estado_activo = 4;
}
```

### Archivos Generados

Después de ejecutar `make proto`, se generan:

- **`telemetry_pb2.py`**: Clases de mensajes Protocol Buffers
- **`telemetry_pb2_grpc.py`**: Clases de servicios gRPC

## Verificar Estado

Para verificar que el servidor está ejecutándose:

```bash
ps aux | grep server.py
```

Para verificar que el puerto está en uso:

```bash
netstat -tulpn | grep 5005
# o
ss -tulpn | grep 5005
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

### Error: "No module named 'telemetry_pb2'"

Compila los archivos proto:

```bash
make proto
```

### Error: "No module named 'grpc'"

Instala las dependencias:

```bash

make install
```

### Error de compilación de proto

Si `make proto` falla, verifica que las dependencias estén instaladas:

```bash
make install
```

### Error: "Connection refused"

- Asegúrate de que el servidor esté ejecutándose: `make run-server`
- Verifica que el puerto 50051 no esté en uso: `netstat -tulpn | grep 5005`
- Espera unos segundos después de iniciar el servidor antes de ejecutar el cliente

### Error de puerto en uso

Si el puerto 50051 ya está en uso:

1. Encuentra el proceso: `lsof -i :5005`
2. Detén el proceso: `kill -9 <PID>`
3. O modifica el puerto en [`server.py`](server.py) y [`client.py`](client.py)

### Problemas con el entorno virtual

Si tienes problemas con el entorno virtual, límpialo y reinstala:

```bash
make distclean
make all
```

### Archivos proto modificados

Si modificas [`telemetry.proto`](telemetry.proto), recompila:

```bash
make clean
make proto
```

## Flujo de Trabajo Completo

1. **Primera instalación:**

   ```bash
   make all
   ```

2. **Ejecutar servidor y cliente:**

   ```bash
   # Terminal 1
   make run-server
   
   # Terminal 2
   make run-client
   ```

3. **Después de modificar telemetry.proto:**

   ```bash
   make clean
   make proto
   ```

4. **Reinstalación completa:**

   ```bash
   make distclean
   make all
   ```

## Comparación con MessagePack

Para comparar con la implementación de MessagePack, consulta el directorio [`MessagePack`](../MessagePack)

## Licencia

Ver archivo [`LICENSE`](../LICENSE) en el directorio raíz del proyecto.
