import socket
import time
import telemetry_pb2

def run_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Crear datos (Objeto estricto)
    sensor = telemetry_pb2.DatosSensor()
    sensor.id_dispositivo = 101
    sensor.ubicacion = "Servidor_Principal_Rack_4"
    sensor.lecturas.extend([24.5, 25.1, 23.8, 24.9, 25.5]) # 5 lecturas float
    sensor.estado_activo = True

    print(f"--- PROTOCOL BUFFERS ---")
    
    # Medir Serialización
    start_time = time.perf_counter()
    payload = sensor.SerializeToString()
    end_time = time.perf_counter()
    
    tiempo_micro = (end_time - start_time) * 1_000_000
    tamanho = len(payload)

    print(f"📦 Tamaño del Payload: {tamanho} bytes")
    print(f"⏱️  Tiempo Serialización: {tiempo_micro:.4f} µs")
    
    sock.sendto(payload, ('127.0.0.1', 5005))

if __name__ == "__main__":
    run_client()