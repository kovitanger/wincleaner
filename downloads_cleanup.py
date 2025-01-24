import os
import shutil
from PyQt5.QtWidgets import QMessageBox

def clean_downloads():
    downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    if not os.path.exists(downloads_dir):
        QMessageBox.information(None, "Очистка загрузок", "Папка загрузок не найдена.")
        return
    try:
        for item in os.listdir(downloads_dir):
            item_path = os.path.join(downloads_dir, item)
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        QMessageBox.information(None, "Очистка загрузок", "Очистка загрузок завершена.")
    except Exception as e:
        QMessageBox.warning(None, "Ошибка", f"Произошла ошибка: {e}")
