from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, QEvent
import sys
import os
import subprocess
import signal

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Блокировка')

        browser = QWebEngineView()
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'index.html'))
        browser.setUrl(QUrl.fromLocalFile(file_path))

        self.setCentralWidget(browser)

        # Установка обработчика событий
        self.installEventFilter(self)

        # Запуск бота
        self.bot_process = subprocess.Popen([sys.executable, 'bot.py'])

    def eventFilter(self, source, event):
        if event.type() == QEvent.WindowStateChange:
            if self.isMinimized():
                self.showFullScreen()
        return super().eventFilter(source, event)

    def closeEvent(self, event):
        self.bot_process.terminate()
        event.accept()

def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.showFullScreen()

    app.exec_()

    # Прерывание процесса бота при выходе
    window.bot_process.terminate()
    window.bot_process.wait()

if __name__ == "__main__":
    main()
