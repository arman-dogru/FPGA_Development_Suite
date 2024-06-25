from PyQt5.QtWidgets import QMainWindow, QTextEdit, QVBoxLayout, QWidget
from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont
from PyQt5.QtCore import QRegExp

class HDLHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(HDLHighlighter, self).__init__(parent)
        self.highlightingRules = []

        keywordFormat = QTextCharFormat()
        keywordFormat.setForeground(QColor("blue"))
        keywordFormat.setFontWeight(QFont.Bold)
        keywords = ["entity", "architecture", "begin", "end", "process", "signal", "variable", "if", "else", "then", "for", "while", "loop", "case", "when", "others"]

        for keyword in keywords:
            pattern = QRegExp("\\b" + keyword + "\\b")
            self.highlightingRules.append((pattern, keywordFormat))

        singleLineCommentFormat = QTextCharFormat()
        singleLineCommentFormat.setForeground(QColor("green"))
        self.highlightingRules.append((QRegExp("--[^\n]*"), singleLineCommentFormat))

    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

class HDLEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('FPGA Development Suite - HDL Editor')
        self.editor = QTextEdit()
        self.highlighter = HDLHighlighter(self.editor.document())
        layout = QVBoxLayout()
        layout.addWidget(self.editor)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    editor = HDLEditor()
    editor.show()
    sys.exit(app.exec_())
