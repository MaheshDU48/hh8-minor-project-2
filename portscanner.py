import socket
import threading

target = input("Enter target IP address: ")
start_port = 1
end_port = 1024

print(f"\nScanning {target}...\n")

def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    try:
        if sock.connect_ex((target, port)) == 0:
            print(f"Port {port} is OPEN")
    except socket.error:
        pass
    finally:
        sock.close()

threads = []

for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("\nScan completed.")
