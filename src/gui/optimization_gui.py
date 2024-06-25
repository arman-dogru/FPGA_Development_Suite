from PyQt5.QtWidgets import QMainWindow, QTextEdit, QVBoxLayout, QWidget, QPushButton, QFileDialog, QMessageBox
from optimizer.optimization_tool import OptimizationTool

class OptimizationGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('FPGA Development Suite - Optimization Tool')
        
        self.editor = QTextEdit()
        self.runButton = QPushButton('Run Optimization')
        self.runButton.clicked.connect(self.run_optimization)

        layout = QVBoxLayout()
        layout.addWidget(self.editor)
        layout.addWidget(self.runButton)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def run_optimization(self):
        hdl_code = self.editor.toPlainText()
        top_module = self.get_top_module_from_code(hdl_code)
        
        optimizer = OptimizationTool(hdl_code, top_module)
        optimization_output = optimizer.run_optimization()
        
        QMessageBox.information(self, "Optimization Output", optimization_output)

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
    gui = OptimizationGUI()
    gui.show()
    sys.exit(app.exec_())
