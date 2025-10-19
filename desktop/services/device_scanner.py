import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor
from PyQt6.QtCore import QThread, pyqtSignal


class DeviceScanner(QThread):
    device_found = pyqtSignal(str, str)  # ip, status
    scan_finished = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.is_scanning = False

    def scan_port(self, ip, port=8080):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((str(ip), port))
            sock.close()
            if result == 0:
                print(f"[+] Port {port} open on {ip}")
                return str(ip)
        except Exception:
            pass
        return None

    def run(self):
        self.is_scanning = True

        print("Scanning 192.168.1.0/24 network...")
        print("Looking for devices with HTTP servers on port 8080...")

        try:
            network = ipaddress.IPv4Network("192.168.1.0/24", strict=False)
            all_hosts = list(network.hosts())

            with ThreadPoolExecutor(max_workers=50) as executor:
                future_to_ip = {executor.submit(self.scan_port, ip, 8080): ip for ip in all_hosts}

                for future in future_to_ip:
                    if not self.is_scanning:
                        break

                    result = future.result()
                    if result:
                        # Emit device immediately when found
                        self.device_found.emit(result, result)

        except Exception as e:
            print(f"Scan error: {e}")

        self.scan_finished.emit()
        self.is_scanning = False

    def stop_scanning(self):
        self.is_scanning = False