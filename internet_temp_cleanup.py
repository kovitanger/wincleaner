import os
import shutil
from PyQt5.QtWidgets import QMessageBox

def clean_browser_cache(browser_name, cache_dir):
    if not os.path.exists(cache_dir):
        QMessageBox.information(None, f"Очистка кеша {browser_name}", f"Папка кеша {browser_name} не найдена.")
        return
    try:
        for item in os.listdir(cache_dir):
            item_path = os.path.join(cache_dir, item)
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        QMessageBox.information(None, f"Очистка кеша {browser_name}", f"Очистка кеша {browser_name} завершена.")
    except Exception as e:
        QMessageBox.warning(None, "Ошибка", f"Произошла ошибка: {e}")

def clean_internet_temp():
    chrome_cache_dir = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Google", "Chrome", "User Data", "Default", "Cache")
    clean_browser_cache("Google Chrome", chrome_cache_dir)

    firefox_cache_dir = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Mozilla", "Firefox", "Profiles")
    if os.path.exists(firefox_cache_dir):
        for profile in os.listdir(firefox_cache_dir):
            profile_cache_dir = os.path.join(firefox_cache_dir, profile, "cache2")
            clean_browser_cache("Mozilla Firefox", profile_cache_dir)
    
    chromium_cache_dir = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Chromium", "User Data", "Default", "Cache")
    clean_browser_cache("Chromium", chromium_cache_dir)
    
    brave_cache_dir = os.path.join(os.path.expanduser("~"), "AppData", "Local", "BraveSoftware", "Brave-Browser", "User Data", "Default", "Cache")
    clean_browser_cache("Brave", brave_cache_dir)
    
    yandex_cache_dir = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Yandex", "YandexBrowser", "User Data", "Default", "Cache")
    clean_browser_cache("Яндекс.Браузер", yandex_cache_dir)
    
    opera_cache_dir = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Opera Software", "Opera Stable", "Cache")
    clean_browser_cache("Opera", opera_cache_dir)
    
    opera_gx_cache_dir = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Opera Software", "Opera GX Stable", "Cache")
    clean_browser_cache("Opera GX", opera_gx_cache_dir)
