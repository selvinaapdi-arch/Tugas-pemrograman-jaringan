import asyncio

async def send_and_receive():
    # Koneksi ke server
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    addr = writer.get_extra_info('sockname')
    print(f"=== Terhubung ke server sebagai {addr} ===")

    try:
        while True:
            # Input user (dibungkus agar tidak blocking event loop)
            message = await asyncio.to_thread(input, "Client > ")

            if message.lower() == 'bye':
                print("[!] Menutup koneksi...")
                break

            # Kirim pesan
            writer.write((message + "\n").encode())
            await writer.drain()

            # Terima balasan server
            data = await reader.read(100)
            if not data:
                print("[!] Server memutus koneksi.")
                break

            print("Server >", data.decode().strip())

    except Exception as e:
        print("[ERROR]", e)
    finally:
        writer.close()
        await writer.wait_closed()
        print("=== Client Ditutup ===")

if __name__ == "__main__":
    asyncio.run(send_and_receive())
