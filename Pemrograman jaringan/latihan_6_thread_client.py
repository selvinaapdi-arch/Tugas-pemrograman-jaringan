import socket
import threading

# Fungsi untuk menerima pesan dari server
def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if not message:
                print("[!] Koneksi ke server terputus.")
                break
            print("\n" + message)
        except:
            print("[!] Terjadi error saat menerima pesan.")
            break

# Fungsi utama client
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # GANTI jika server beda komputer
    client.connect(('localhost', 5555))
    print("=== Terhubung ke Chat Server ===")

    # Thread untuk menerima pesan
    thread_recv = threading.Thread(target=receive_messages, args=(client,))
    thread_recv.daemon = True
    thread_recv.start()

    # Loop kirim pesan
    while True:
        try:
            msg = input()
            if msg.lower() == 'bye':
                client.send(msg.encode('utf-8'))
                break
            client.send(msg.encode('utf-8'))
        except:
            break

    client.close()
    print("=== Client Ditutup ===")

if __name__ == "__main__":
    start_client()
