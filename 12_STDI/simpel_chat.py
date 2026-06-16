import socket
import threading
import sys
def terima_pesan(port_saya):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind(('0.0.0.0', port_saya))
        server_socket.listen(1)
        print(sys.stderr, f"\n[SERVER] Mendengarkan di port {port_saya}...")
        koneksi, alamat_peer = server_socket.accept()
        print(sys.stderr, f"\n[SERVER] Terhubung dengan peer: {alamat_peer}")
        while True:
            data = koneksi.recv(1024)
            if not data:
                print(sys.stderr, "\n[SERVER] Peer memutuskan koneksi.")
                break
        print(f"\n[Peer]: {data.decode('utf-8')}")
    except Exception as e:
        print(sys.stderr, f"[SERVER] Error: {e}")
    finally:
        server_socket.close()
def kirim_pesan(ip_tujuan, port_tujuan):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(sys.stderr, f"[CLIENT] Mencoba terhubung ke {ip_tujuan}:{port_tujuan}...")
    try:
        client_socket.connect((ip_tujuan, port_tujuan))
        print(sys.stderr, "[CLIENT] Sukses terhubung!")
        print("Silakan ketik pesan dan tekan Enter (Ketik 'keluar' untuk berhenti):")
        while True:
            pesan = input()
            if pesan.lower() == 'keluar':
                break
                client_socket.sendall(pesan.encode('utf-8'))
    except Exception as e:
        print(sys.stderr, f"[CLIENT] Gagal terhubung atau mengirim pesan: {e}")
    finally:
        client_socket.close()
        
if __name__ == "__main__":
    print("=== Praktikum Modul 12 - Sub 01 ===")
    port_lokal = int(input("Masukkan PORT LOKAL untuk server Anda (contoh: 5001): "))
    thread_server = threading.Thread(target=terima_pesan, args=(port_lokal,))
    thread_server.daemon = True
    thread_server.start()
    import time
    time.sleep(1)
    print("\n--- Konfigurasi Hubungan ke Peer Lain ---")
    ip_target = input("Masukkan IP TARGET (Peer tujuan, contoh: 192.168.1.10 atau localhost): ")
    port_target = int(input("Masukkan PORT TARGET (Port server peer tujuan): "))
    kirim_pesan(ip_target, port_target)
    print("\nProgram Selesai.")
