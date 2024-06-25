from PyQt5.QtWidgets import QMainWindow, QTextEdit, QVBoxLayout, QWidget, QPushButton, QFileDialog, QMessageBox
from synthesizer.synthesis_tool.py import SynthesisTool

class SynthesisGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('FPGA Development Suite - Synthesis Tool')
        
        self.editor = QTextEdit()
        self.runButton = QPushButton('Run Synthesis')
        self.runButton.clicked.connect(self.run_synthesis)

        layout = QVBoxLayout()
        layout.addWidget(self.editor)
        layout.addWidget(self.runButton)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def run_synthesis(self):
        hdl_code = self.editor.toPlainText()
        top_module = self.get_top_module_from_code(hdl_code)
        
        synth_tool = SynthesisTool(hdl_code, top_module)
        synthesis_output = synth_tool.run_synthesis()
        
        QMessageBox.information(self, "Synthesis Output", synthesis_output)

    def get_top_module_from_code(self, hdl_code):
        # Simple parser to extract top module name (placeholder)
        lines = hdl_code.splitlines()
        for line in lines:
            if line.strip().startswith('module'):
                return line.split()[1]
        return "unknown"

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    gui = SynthesisGUI()
    gui.show()
    sys.exit(app.exec_())
