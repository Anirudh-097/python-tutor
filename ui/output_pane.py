import subprocess
import sys

from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QGroupBox, QVBoxLayout, QPlainTextEdit


class _RunWorker(QThread):
    finished = pyqtSignal(str, str)  # (stdout, stderr)

    def __init__(self, code: str, timeout: int = 5):
        super().__init__()
        self.code = code
        self.timeout = timeout

    def run(self):
        try:
            result = subprocess.run(
                [sys.executable, "-c", self.code],
                capture_output=True,
                text=True,
                timeout=self.timeout,
            )
            self.finished.emit(result.stdout, result.stderr)
        except subprocess.TimeoutExpired:
            self.finished.emit("", f"Execution timed out after {self.timeout}s.")
        except Exception as e:
            self.finished.emit("", f"Failed to execute: {e}")


class OutputPane(QGroupBox):
    """Displays stdout/stderr of the last run. Owns the subprocess worker."""

    run_finished = pyqtSignal()  # fired after output is updated, so ChatPane context is fresh

    def __init__(self, parent=None):
        super().__init__("Output", parent)
        layout = QVBoxLayout(self)

        self.view = QPlainTextEdit()
        self.view.setReadOnly(True)
        layout.addWidget(self.view)

        self._worker = None
        self._on_started_cb = None
        self._on_finished_cb = None

    def run_code(self, code: str, on_started=None, on_finished=None):
        self._on_started_cb = on_started
        self._on_finished_cb = on_finished
        if on_started:
            on_started()

        self.view.setPlainText("Running...")
        self._worker = _RunWorker(code)
        self._worker.finished.connect(self._on_finished)
        self._worker.start()

    def _on_finished(self, stdout, stderr):
        text = stdout or ""
        if stderr:
            text += ("\n" if text else "") + stderr
        self.view.setPlainText(text or "(no output)")
        if self._on_finished_cb:
            self._on_finished_cb()
        self.run_finished.emit()

    def output_text(self):
        return self.view.toPlainText()
