from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QGroupBox, QVBoxLayout, QPlainTextEdit, QPushButton, QHBoxLayout


class CodePane(QGroupBox):
    """Code editor pane. Emits run_requested(code_text) when Run is clicked."""

    run_requested = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__("Code", parent)
        layout = QVBoxLayout(self)

        self.editor = QPlainTextEdit()
        self.editor.setPlaceholderText("# Type your Python code here\n")
        layout.addWidget(self.editor)

        btn_row = QHBoxLayout()
        self.run_btn = QPushButton("Run \u25B6")
        self.run_btn.clicked.connect(self._on_run_clicked)
        btn_row.addStretch()
        btn_row.addWidget(self.run_btn)
        layout.addLayout(btn_row)

    def _on_run_clicked(self):
        self.run_requested.emit(self.editor.toPlainText())

    def code_text(self):
        return self.editor.toPlainText()

    def set_running(self, running: bool):
        self.run_btn.setEnabled(not running)
        self.run_btn.setText("Running..." if running else "Run \u25B6")
