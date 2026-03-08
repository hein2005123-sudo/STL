import socket, threading, time, sys, hashlib, os

# --- YOUR PRIVATE KEY ---
MY_SECRET_KEY = "Key_Pro_2026_X" 
# ------------------------

def get_hwid():
    try:
        info = str(os.uname()[1]) + str(os.getlogin() if hasattr(os, 'getlogin') else 'user')
        return hashlib.md5(info.encode()).hexdigest()[:10].upper()
    except:
        return "F0A90BD125"

MY_DEVICE_ID = get_hwid()

print("\033[92m[*] STL PRIVATE BYPASS SYSTEM v3.5")
print(f"\033[93m[!] YOUR DEVICE ID: {MY_DEVICE_ID}")
print("\033[37m------------------------------------------")

user_input = input("\033[96m[?] ENTER ACCESS KEY: ")

if user_input != MY_SECRET_KEY:
    print("\033[91m[X] ACCESS DENIED: INVALID KEY.")
    sys.exit()

print("\033[92m[V] AUTHENTICATION SUCCESS! STARTING SERVICE...")
time.sleep(1)

def handle_connection(client_socket):
    try:
        remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        remote.connect(('1.1.1.1', 80))
        payload = "GET / HTTP/1.1\r\nHost: www.starlink.com\r\nConnection: Keep-Alive\r\n\r\n"
        remote.send(payload.encode())
        def sync(s1, s2):
            try:
                while True:
                    data = s1.recv(8192)
                    if not data: break
                    s2.send(data)
            except: pass
        threading.Thread(target=sync, args=(client_socket, remote), daemon=True).start()
        sync(remote, client_socket)
    except: pass
    finally: client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('0.0.0.0', 8080))
server.listen(100)

print("\033[92m[*] TUNNEL RUNNING ON PORT 8080")
print("\033[94m[*] SYSTEM STATUS: ACTIVE")

while True:
    client, addr = server.accept()
    threading.Thread(target=handle_connection, args=(client,), daemon=True).start()
