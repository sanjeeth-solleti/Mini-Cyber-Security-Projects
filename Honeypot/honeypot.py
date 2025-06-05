import socket
import datetime

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 2222       # Fake SSH port
LOG_FILE = "honeypot_log.txt"

def log_attempt(addr):
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] Connection from {addr[0]}:{addr[1]}\n")
        print(f"[{timestamp}] Logged connection from {addr[0]}:{addr[1]}")

def run_honeypot():
    print(f"[*] Starting honeypot on port {PORT}...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        log_attempt(addr)
        conn.send(b"Fake SSH Server: Access Denied\n")
        conn.close()

if __name__ == "__main__":
    try:
        run_honeypot()
    except KeyboardInterrupt:
        print("\n[!] Honeypot stopped.")

