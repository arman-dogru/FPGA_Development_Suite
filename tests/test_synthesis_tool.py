import unittest
from synthesizer.synthesis_tool import SynthesisTool

class TestSynthesisTool(unittest.TestCase):
    def test_synthesis(self):
        hdl_code = """
        module test;
            initial begin
                $display("Hello, Synthesis!");
            end
        endmodule
        """
        synth_tool = SynthesisTool(hdl_code, "test")
        result = synth_tool.run_synthesis()
        self.assertIn("Synthesis successful", result)  # Replace with actual success message

if __name__ == '__main__':
    unittest.main()
