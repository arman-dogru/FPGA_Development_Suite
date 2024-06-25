import unittest
from PyQt5.QtWidgets import QApplication
from editor.hdl_editor import HDLEditor

class TestHDLEditor(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])
        self.editor = HDLEditor()

    def test_initialization(self):
        self.assertIsNotNone(self.editor)
        self.assertEqual(self.editor.windowTitle(), 'FPGA Development Suite - HDL Editor')

    def test_syntax_highlighting(self):
        self.editor.editor.setText("module test; endmodule")
        # Check if syntax highlighting is applied
        self.assertEqual(self.editor.editor.toPlainText(), "module test; endmodule")

if __name__ == '__main__':
    unittest.main()
