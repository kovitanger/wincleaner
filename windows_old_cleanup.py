import os
import ctypes
from PyQt5.QtWidgets import QMessageBox

def run_as_admin(command):
    try:
        result = ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", f'/c {command}', None, 1)
        return result
    except Exception as e:
        return str(e)

def delete_windows_old():
    windows_old_dir = "C:\\Windows.old"
    if not os.path.exists(windows_old_dir):
        QMessageBox.information(None, "Удаление старой версии Windows", "Папка Windows.old не найдена.")
        return
    try:
        result = run_as_admin(f'rd /s /q "{windows_old_dir}"')
        if result == 42:
            QMessageBox.information(None, "Удаление старой версии Windows", "Папка Windows.old удалена.")
        else:
            QMessageBox.warning(None, "Ошибка", f"Произошла ошибка при удалении папки Windows.old: {result}")
    except Exception as e:
        QMessageBox.warning(None, "Ошибка", f"Произошла ошибка: {e}")
