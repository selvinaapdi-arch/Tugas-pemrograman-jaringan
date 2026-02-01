import socket
import select
import sys

def run_chat_client():
    server_ip = "127.0.0.1"   # Ganti jika server di komputer lain
    server_port = 9000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    client_socket.setblocking(False)

    print("=== Terhubung ke Chat Server ===")
    print("Ketik pesan dan tekan ENTER (ketik 'exit' untuk keluar)\n")

    while True:
        # Pantau input keyboard dan socket server
        sockets_list = [sys.stdin, client_socket]
        read_sockets, _, _ = select.select(sockets_list, [], [])

        for sock in read_sockets:
            # Jika ada pesan dari server
            if sock == client_socket:
                try:
                    message = client_socket.recv(1024)
                    if not message:
                        print("Server terputus.")
                        return
                    print(message.decode(), end="")
                except:
                    continue

            # Jika user mengetik pesan
            else:
                message = sys.stdin.readline()
                if message.strip().lower() == "exit":
                    print("Keluar dari chat...")
                    client_socket.close()
                    return

                client_socket.send(message.encode())

if __name__ == "__main__":
    run_chat_client()
