import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QMessageBox, QTabWidget, QHBoxLayout, QLabel, QToolBar, QAction
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import temp_cleanup
import recycle_bin_cleanup
import hibernation_cleanup
import windows_old_cleanup
import downloads_cleanup
import internet_temp_cleanup

class CleanupApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Программа для очистки Windows")
        self.setFixedSize(500, 350)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout(central_widget)

        sidebar = QVBoxLayout()
        sidebar.setAlignment(Qt.AlignTop)

        lbl_category = QLabel("Категории")
        lbl_category.setFont(QFont("Arial", 14, QFont.Bold))
        sidebar.addWidget(lbl_category)

        btn_clean = QPushButton("Очистка")
        btn_clean.setFont(QFont("Arial", 12))
        btn_clean.setStyleSheet("background-color: #4CAF50; color: white;")
        btn_clean.clicked.connect(self.show_cleaning_tab)
        sidebar.addWidget(btn_clean)

        btn_about = QPushButton("О приложении")
        btn_about.setFont(QFont("Arial", 12))
        btn_about.setStyleSheet("background-color: #2196F3; color: white;")
        btn_about.clicked.connect(self.show_about_info)
        sidebar.addWidget(btn_about)

        layout.addLayout(sidebar)

        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)

        self.cleaning_tab = QWidget()
        self.tabs.addTab(self.cleaning_tab, "Очистка")

        self.init_cleaning_tab()

    def init_cleaning_tab(self):
        layout = QVBoxLayout()
        font = QFont("Arial", 12, QFont.Bold)

        def create_button(text, color, callback):
            btn = QPushButton(text)
            btn.setFont(font)
            btn.setStyleSheet(f"background-color: {color}; color: white;")
            btn.clicked.connect(callback)
            layout.addWidget(btn)

        create_button("Очистка временных файлов", "#4CAF50", self.cleanup_temp)
        create_button("Очистка корзины", "#f44336", self.cleanup_recycle_bin)
        create_button("Отключение гибернации", "#2196F3", self.disable_hibernation)
        create_button("Удаление старой версии Windows", "#FF9800", self.delete_windows_old)
        create_button("Очистка загрузок", "#9C27B0", self.cleanup_downloads)
        create_button("Очистка временных файлов интернета", "#3F51B5", self.cleanup_internet_temp)

        self.cleaning_tab.setLayout(layout)

    def show_cleaning_tab(self):
        self.tabs.setCurrentWidget(self.cleaning_tab)

    def show_about_info(self):
        QMessageBox.information(self, "О приложении", "Версия: 1.0\nРазработчик: kovitang\nГод выпуска: 2025")

    def cleanup_temp(self):
        temp_cleanup.clean_temp_files()

    def cleanup_recycle_bin(self):
        recycle_bin_cleanup.empty_recycle_bin()

    def disable_hibernation(self):
        hibernation_cleanup.disable_hibernation()

    def delete_windows_old(self):
        windows_old_cleanup.delete_windows_old()

    def cleanup_downloads(self):
        downloads_cleanup.clean_downloads()

    def cleanup_internet_temp(self):
        internet_temp_cleanup.clean_internet_temp()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = CleanupApp()
    ex.show()
    sys.exit(app.exec_())
