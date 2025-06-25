import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QTextEdit, QFileDialog, QAction, QMessageBox
)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Bangla Text Editor")
        self.setGeometry(300, 300, 800, 800)

        # QTextEdit for text input
        self.editor = QTextEdit(self)
        bangla_font = QFont("Siyam Rupali", 18)  # Make sure the font is installed
        self.editor.setFont(bangla_font)
        self.setCentralWidget(self.editor)

        # Create Menu Bar
        self.create_menu()

    def create_menu(self):
        menubar = self.menuBar()

        # File Menu
        file_menu = menubar.addMenu("File")

        # Open Action
        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        # Save Action
        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")
        if path:
            try:
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.editor.setText(content)
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to open file:\n{e}")

    def save_file(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)")
        if path:
            try:
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(self.editor.toPlainText())
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to save file:\n{e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
