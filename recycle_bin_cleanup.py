import os
import ctypes
from PyQt5.QtWidgets import QMessageBox

def run_as_admin(command):
    try:
        result = ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", f'/c {command}', None, 1)
        return result
    except Exception as e:
        return str(e)

def empty_recycle_bin():
    try:
        result = run_as_admin('rd /s /q %systemdrive%\\$Recycle.Bin')
        if result == 42:
            QMessageBox.information(None, "Очистка корзины", "Очистка корзины завершена.")
        else:
            QMessageBox.warning(None, "Ошибка", f"Произошла ошибка при очистке корзины: {result}")
    except Exception as e:
        QMessageBox.warning(None, "Ошибка", f"Произошла ошибка: {e}")
