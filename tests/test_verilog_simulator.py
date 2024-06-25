import unittest
from simulator.verilog_simulator import run_verilog_simulation

class TestVerilogSimulator(unittest.TestCase):
    def test_simulation(self):
        verilog_code = """
        module test;
            initial begin
                $display("Hello, Verilog!");
            end
        endmodule
        """
        result = run_verilog_simulation(verilog_code)
        self.assertIn("Hello, Verilog!", result)

if __name__ == '__main__':
    unittest.main()
