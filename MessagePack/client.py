import socket
import time
import msgpack

def run_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Crear datos (Diccionario simple de Python)
    sensor = {
        "id": 101,
        "ubicacion": "Servidor_Principal_Rack_4",
        "lecturas": [24.5, 25.1, 23.8, 24.9, 25.5],
        "estado": True
    }

    print(f"--- MESSAGEPACK ---")

    # Medir Serialización
    start_time = time.perf_counter()
    payload = msgpack.packb(sensor)
    end_time = time.perf_counter()
    
    tiempo_micro = (end_time - start_time) * 1_000_000
    tamanho = len(payload)

    print(f"📦 Tamaño del Payload: {tamanho} bytes")
    print(f"⏱️  Tiempo Serialización: {tiempo_micro:.4f} µs")
    
    sock.sendto(payload, ('127.0.0.1', 6006))

if __name__ == "__main__":
    run_client()