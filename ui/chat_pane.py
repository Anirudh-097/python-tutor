from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QPushButton


class _AskWorker(QThread):
    """Runs the (potentially slow) LLM call off the GUI thread."""
    finished = pyqtSignal(str)
    failed = pyqtSignal(str)

    def __init__(self, question, current_topic, code_pane, output_pane):
        super().__init__()
        self.question = question
        self.current_topic = current_topic
        self.code_pane = code_pane
        self.output_pane = output_pane

    def run(self):
        try:
            from rag.chain import answer_query
            result = answer_query(
                question=self.question,
                current_topic=self.current_topic,
                code_pane=self.code_pane,
                output_pane=self.output_pane,
            )
            self.finished.emit(result)
        except Exception as e:
            self.failed.emit(str(e))


class ChatPane(QGroupBox):
    """Right side chat: has access to current topic, code pane, and output pane via getter callbacks."""

    def __init__(self, get_topic, get_code, get_output, parent=None):
        super().__init__("Chatbot", parent)
        self.get_topic = get_topic
        self.get_code = get_code
        self.get_output = get_output
        self._worker = None

        layout = QVBoxLayout(self)

        self.history = QTextEdit()
        self.history.setReadOnly(True)
        layout.addWidget(self.history)

        input_row = QHBoxLayout()
        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Ask a question about the topic, your code, or the output...")
        self.input_box.returnPressed.connect(self.send)
        self.send_btn = QPushButton("Send")
        self.send_btn.clicked.connect(self.send)
        input_row.addWidget(self.input_box)
        input_row.addWidget(self.send_btn)
        layout.addLayout(input_row)

    def send(self):
        question = self.input_box.text().strip()
        if not question:
            return

        self._append("You", question)
        self.input_box.clear()
        self.send_btn.setEnabled(False)
        self.send_btn.setText("Thinking...")

        self._worker = _AskWorker(
            question=question,
            current_topic=self.get_topic(),
            code_pane=self.get_code(),
            output_pane=self.get_output(),
        )
        self._worker.finished.connect(self._on_answer)
        self._worker.failed.connect(self._on_error)
        self._worker.start()

    def _on_answer(self, text):
        self._append("Tutor", text)
        self._reset_button()

    def _on_error(self, msg):
        self._append("Tutor", f"[Error contacting local model: {msg}]")
        self._reset_button()

    def _reset_button(self):
        self.send_btn.setEnabled(True)
        self.send_btn.setText("Send")

    def _append(self, who, text):
        self.history.append(f"<b>{who}:</b> {text}<br>")
