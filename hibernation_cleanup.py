import ctypes
from PyQt5.QtWidgets import QMessageBox

def run_as_admin(command):
    try:
        result = ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", f'/c {command}', None, 1)
        return result
    except Exception as e:
        return str(e)

def disable_hibernation():
    try:
        result = run_as_admin("powercfg.exe /hibernate off")
        if result == 42:
            QMessageBox.information(None, "Отключение гибернации", "Режим гибернации отключен.")
        else:
            QMessageBox.warning(None, "Ошибка", f"Произошла ошибка при отключении режима гибернации: {result}")
    except Exception as e:
        QMessageBox.warning(None, "Ошибка", f"Произошла ошибка: {e}")
