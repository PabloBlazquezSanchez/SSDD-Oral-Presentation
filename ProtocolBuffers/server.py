import socket
import time
import telemetry_pb2 # El archivo generado

def run_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', 5005))
    print("🔵 Servidor Protobuf listo en puerto 5005...")

    while True:
        data, addr = sock.recvfrom(1024) # Buffer de 1024 bytes
        
        # Medir tiempo de Deserialización
        start_time = time.perf_counter()
        
        objeto_proto = telemetry_pb2.DatosSensor()
        objeto_proto.ParseFromString(data) # Parseo estricto
        
        end_time = time.perf_counter()
        
        tiempo_micro = (end_time - start_time) * 1_000_000
        print(f"[Recibido] ID: {objeto_proto.id_dispositivo} | Deserialización: {tiempo_micro:.4f} µs")

if __name__ == "__main__":
    run_server()