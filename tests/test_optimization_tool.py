import unittest
from optimizer.optimization_tool import OptimizationTool

class TestOptimizationTool(unittest.TestCase):
    def test_optimization(self):
        hdl_code = """
        module test;
            initial begin
                $display("Hello, Optimization!");
            end
        endmodule
        """
        optimizer = OptimizationTool(hdl_code, "test")
        result = optimizer.run_optimization()
        self.assertIn("Optimization successful", result)  # Replace with actual success message

if __name__ == '__main__':
    unittest.main()
