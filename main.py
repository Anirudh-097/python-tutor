import sys
from pathlib import Path

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QSplitter, QWidget, QVBoxLayout

from ui.course_pane import CoursePane
from ui.chat_pane import ChatPane
from ui.code_pane import CodePane
from ui.output_pane import OutputPane


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Tutor")
        self.resize(1200, 800)

        self.course_pane = CoursePane(course_dir="course_content")
        self.code_pane = CodePane()
        self.output_pane = OutputPane()
        self.chat_pane = ChatPane(
            get_topic=self.course_pane.current_topic_title,
            get_code=self.code_pane.code_text,
            get_output=self.output_pane.output_text,
        )

        # Code -> Output wiring
        self.code_pane.run_requested.connect(self._on_run)

        # Right side: chat on top, code + output stacked below
        right_splitter = QSplitter(Qt.Orientation.Vertical)
        right_splitter.addWidget(self.chat_pane)

        code_output_splitter = QSplitter(Qt.Orientation.Horizontal)
        code_output_splitter.addWidget(self.code_pane)
        code_output_splitter.addWidget(self.output_pane)
        code_output_splitter.setSizes([600, 600])

        right_splitter.addWidget(code_output_splitter)
        right_splitter.setSizes([350, 450])

        main_splitter = QSplitter(Qt.Orientation.Horizontal)
        main_splitter.addWidget(self.course_pane)
        main_splitter.addWidget(right_splitter)
        main_splitter.setSizes([350, 850])

        container = QWidget()
        layout = QVBoxLayout(container)
        layout.addWidget(main_splitter)
        self.setCentralWidget(container)

    def _on_run(self, code: str):
        self.code_pane.set_running(True)
        self.output_pane.run_code(
            code,
            on_finished=lambda: self.code_pane.set_running(False),
        )


def main():
    app = QApplication(sys.argv)

    qss_path = Path(__file__).parent / "ui" / "style.qss"
    if qss_path.exists():
        app.setStyleSheet(qss_path.read_text())

    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
