# Python Tutor — Local RAG + LangChain + PyQt6

## Setup
```bash
pip install -r requirements.txt
ollama pull qwen2.5:3b
ollama pull nomic-embed-text
```

## First run
1. Put your course markdown files under `course_content/<level_folder>/*.md`
   (a sample `01_basics/01_variables.md` is included).
2. Build the vector index (from your existing `rag/ingest.py`):
   ```bash
   python rag/ingest.py
   ```
3. Launch the app:
   ```bash
   python main.py
   ```

## Notes
- Chat and code execution both run on background QThreads so the UI never freezes.
- `rag/chain.py` is wired to your tuned fast config: `qwen2.5:3b`, `k=1`,
  `num_predict=200`, `keep_alive="1h"`. Adjust `k` or `num_predict` in that
  file if answers feel too shallow or get cut off.
- Code execution uses `subprocess` with a 5s timeout — adjust `timeout` in
  `ui/output_pane.py` if you need longer-running scripts.
- Replace/extend `ui/style.qss` to tweak the retro look further (title bar
  color, fonts, bevel widths).

## Next steps to consider
- Syntax highlighting in the code pane (e.g. `QSyntaxHighlighter` subclass or QScintilla).
- Persist chat history / topic progress across sessions (simple JSON file is enough).
- Add a "insert into code pane" button on chat responses containing code blocks.
