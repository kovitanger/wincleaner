import os
import psutil
from PyQt5.QtWidgets import QMessageBox

def terminate_process_using_file(file_path):
    for proc in psutil.process_iter(['pid', 'open_files']):
        try:
            open_files = proc.info['open_files']
            if open_files:
                for open_file in open_files:
                    if open_file.path == file_path:
                        proc.terminate()
                        proc.wait()
                        return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def clean_temp_files():
    temp_dir = "C:\\Windows\\Temp"
    if not os.path.exists(temp_dir):
        QMessageBox.information(None, "Очистка временных файлов", "Папка не найдена.")
        return
    try:
        result = os.system(f'rd /s /q "{temp_dir}"')
        if result != 0:
            terminated = False
            for root, _, files in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    if terminate_process_using_file(file_path):
                        terminated = True
                        os.remove(file_path)
            if terminated:
                result = os.system(f'rd /s /q "{temp_dir}"')
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        QMessageBox.information(None, "Очистка временных файлов", "Очистка временных файлов завершена.")
    except Exception as e:
        QMessageBox.warning(None, "Ошибка", f"Произошла ошибка: {e}")
