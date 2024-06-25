import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction
from gui.hdl_editor import HDLEditor
from gui.simulation_gui import SimulationGUI
from gui.synthesis_gui import SynthesisGUI
from gui.verification_gui import VerificationGUI
from gui.optimization_gui import OptimizationGUI

class FPGADevelopmentSuite(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('FPGA Development Suite')
        self.setGeometry(100, 100, 800, 600)

        menubar = self.menuBar()

        fileMenu = menubar.addMenu('File')
        exitAction = QAction('Exit', self)
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

        toolsMenu = menubar.addMenu('Tools')
        hdlEditorAction = QAction('HDL Editor', self)
        hdlEditorAction.triggered.connect(self.openHDLEditor)
        toolsMenu.addAction(hdlEditorAction)

        simulationAction = QAction('Simulation', self)
        simulationAction.triggered.connect(self.openSimulationTool)
        toolsMenu.addAction(simulationAction)

        synthesisAction = QAction('Synthesis', self)
        synthesisAction.triggered.connect(self.openSynthesisTool)
        toolsMenu.addAction(synthesisAction)

        verificationAction = QAction('Verification', self)
        verificationAction.triggered.connect(self.openVerificationTool)
        toolsMenu.addAction(verificationAction)

        optimizationAction = QAction('Optimization', self)
        optimizationAction.triggered.connect(self.openOptimizationTool)
        toolsMenu.addAction(optimizationAction)

    def openHDLEditor(self):
        self.hdlEditor = HDLEditor()
        self.hdlEditor.show()

    def openSimulationTool(self):
        self.simulationTool = SimulationGUI()
        self.simulationTool.show()

    def openSynthesisTool(self):
        self.synthesisTool = SynthesisGUI()
        self.synthesisTool.show()

    def openVerificationTool(self):
        self.verificationTool = VerificationGUI()
        self.verificationTool.show()

    def openOptimizationTool(self):
        self.optimizationTool = OptimizationGUI()
        self.optimizationTool.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainApp = FPGADevelopmentSuite()
    mainApp.show()
    sys.exit(app.exec_())
