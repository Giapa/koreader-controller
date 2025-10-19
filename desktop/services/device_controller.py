import requests


class DeviceController:
    def __init__(self):
        self.selected_ip = None

    def connect_device(self, ip):
        self.selected_ip = ip
        print(f"Selected IP: {self.selected_ip}")

    def previous_page(self):
        if self.selected_ip:
            try:
                requests.get(
                    f"http://{self.selected_ip}:8080/koreader/event/GotoViewRel/-1",
                    timeout=2,
                )
                print(f"Previous page request sent to {self.selected_ip}")
                return True
            except Exception as e:
                print(f"Error sending previous request: {e}")
                return False
        return False

    def next_page(self):
        if self.selected_ip:
            try:
                requests.get(
                    f"http://{self.selected_ip}:8080/koreader/event/GotoViewRel/1",
                    timeout=2,
                )
                print(f"Next page request sent to {self.selected_ip}")
                return True
            except Exception as e:
                print(f"Error sending next request: {e}")
                return False
        return False

    def get_selected_ip(self):
        return self.selected_ip

    def disconnect_device(self):
        self.selected_ip = None
        print("Device disconnected")