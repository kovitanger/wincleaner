import os
from PyQt5.QtWidgets import QMessageBox

def run_command_as_admin(command):
    try:
        result = os.system(command)
        if result != 0:
            raise Exception(f"Команда завершилась с ошибкой: {result}")
        return ""
    except Exception as e:
        return str(e)
