import unittest
from verifier.functional_verifier import FunctionalVerifier

class TestVerificationTool(unittest.TestCase):
    def test_functional_verification(self):
        vhdl_code = """
        library ieee;
        use ieee.std_logic_1164.all;

        entity test is
        end entity;

        architecture behavior of test is
        begin
            process
            begin
                report "Hello, VHDL Verification!";
                wait;
            end process;
        end architecture;
        """
        verifier = FunctionalVerifier(vhdl_code, "test")
        result = verifier.run_verification()
        self.assertIn("Verification passed", result)  # Replace with actual success message

if __name__ == '__main__':
    unittest.main()
