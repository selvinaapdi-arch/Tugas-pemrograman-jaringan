import socket

# Membuat socket client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Koneksi ke server
client.connect(('localhost', 12345))
print("=== Terhubung ke Chat Server ===")

# INTI CHAT: Loop komunikasi
while True:
    try:
        # 1. Kirim Pesan ke Server
        message = input("Client (Anda) > ")
        client.send(message.encode('utf-8'))

        # 2. Cek jika Client ingin keluar
        if message.lower() == 'bye':
            print("[!] Anda mengakhiri sesi.")
            break

        # 3. Terima Balasan dari Server (BLOCKING)
        data = client.recv(1024).decode('utf-8')

        # 4. Cek jika server menutup koneksi
        if not data or data.lower() == 'bye':
            print("[!] Server mengakhiri sesi.")
            break

        print(f"Server > {data}")

    except Exception as e:
        print(f"Error Terjadi: {e}")
        break

# Bersih-bersih koneksi
client.close()
print("=== Client Ditutup ===")
