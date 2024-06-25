from PyQt5.QtWidgets import QMainWindow, QTextEdit, QVBoxLayout, QWidget, QPushButton, QFileDialog, QMessageBox
from verifier.functional_verifier import FunctionalVerifier
from verifier.formal_verifier import FormalVerifier

class VerificationGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('FPGA Development Suite - Verification Tool')
        
        self.editor = QTextEdit()
        self.runFunctionalButton = QPushButton('Run Functional Verification')
        self.runFormalButton = QPushButton('Run Formal Verification')

        self.runFunctionalButton.clicked.connect(self.run_functional_verification)
        self.runFormalButton.clicked.connect(self.run_formal_verification)

        layout = QVBoxLayout()
        layout.addWidget(self.editor)
        layout.addWidget(self.runFunctionalButton)
        layout.addWidget(self.runFormalButton)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def run_functional_verification(self):
        hdl_code = self.editor.toPlainText()
        top_module = self.get_top_module_from_code(hdl_code)
        
        verifier = FunctionalVerifier(hdl_code, top_module)
        verification_output = verifier.run_verification()
        
        QMessageBox.information(self, "Functional Verification Output", verification_output)

    def run_formal_verification(self):
        hdl_code = self.editor.toPlainText()
        top_module = self.get_top_module_from_code(hdl_code)
        
        verifier = FormalVerifier(hdl_code, top_module)
        verification_output = verifier.run_verification()
        
        QMessageBox.information(self, "Formal Verification Output", verification_output)

    def get_top_module_from_code(self, hdl_code):
        # Simple parser to extract top module name (placeholder)
        lines = hdl_code.splitlines()
        for line in lines:
            if line.strip().startswith('module') or line.strip().startswith('entity'):
                return line.split()[1]
        return "unknown"

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    gui = VerificationGUI()
    gui.show()
    sys.exit(app.exec_())
