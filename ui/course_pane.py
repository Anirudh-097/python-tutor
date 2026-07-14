from pathlib import Path

import frontmatter
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QGroupBox, QVBoxLayout, QTreeWidget, QTreeWidgetItem, QTextEdit, QSplitter
from PyQt6.QtCore import Qt


class CoursePane(QGroupBox):
    """Left pane: topic tree (beginner -> advanced) + explanation viewer."""

    topic_selected = pyqtSignal(str, str)  # (title, body_markdown)

    def __init__(self, course_dir="course_content", parent=None):
        super().__init__("Course Topics", parent)
        self.course_dir = Path(course_dir)

        layout = QVBoxLayout(self)
        splitter = QSplitter(Qt.Orientation.Vertical)

        self.tree = QTreeWidget()
        self.tree.setHeaderHidden(True)
        self.tree.itemClicked.connect(self._on_item_clicked)

        self.viewer = QTextEdit()
        self.viewer.setReadOnly(True)

        splitter.addWidget(self.tree)
        splitter.addWidget(self.viewer)
        splitter.setSizes([300, 300])
        layout.addWidget(splitter)

        self._load_topics()

    def _load_topics(self):
        """Walk course_content/, group by folder (level), sort by 'order' in frontmatter."""
        self.tree.clear()
        if not self.course_dir.exists():
            return

        folders = sorted([d for d in self.course_dir.iterdir() if d.is_dir()])
        for folder in folders:
            folder_item = QTreeWidgetItem([folder.name])
            self.tree.addTopLevelItem(folder_item)

            entries = []
            for path in folder.glob("*.md"):
                post = frontmatter.load(path)
                entries.append((post.get("order", 0), post.get("title", path.stem), post.content, path))
            entries.sort(key=lambda e: e[0])

            for order, title, body, path in entries:
                child = QTreeWidgetItem([title])
                child.setData(0, Qt.ItemDataRole.UserRole, body)
                folder_item.addChild(child)

            folder_item.setExpanded(True)

    def _on_item_clicked(self, item, column):
        body = item.data(0, Qt.ItemDataRole.UserRole)
        if body is None:
            return  # a folder header, not a topic
        title = item.text(0)
        self.viewer.setMarkdown(body)
        self.topic_selected.emit(title, body)

    def current_topic_title(self):
        item = self.tree.currentItem()
        if item and item.data(0, Qt.ItemDataRole.UserRole) is not None:
            return item.text(0)
        return ""
