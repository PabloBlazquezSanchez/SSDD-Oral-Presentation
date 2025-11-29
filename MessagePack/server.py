import socket
import time
import msgpack

def run_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', 6006))
    print("🟠 Servidor MessagePack listo en puerto 6006...")

    while True:
        data, addr = sock.recvfrom(1024)
        
        # Medir Deserialización
        start_time = time.perf_counter()
        
        # raw=False para que los strings sean str y no bytes
        objeto_dict = msgpack.unpackb(data, raw=False) 
        
        end_time = time.perf_counter()
        
        tiempo_micro = (end_time - start_time) * 1_000_000
        print(f"[Recibido] ID: {objeto_dict['id']} | Deserialización: {tiempo_micro:.4f} µs")

if __name__ == "__main__":
    run_server()