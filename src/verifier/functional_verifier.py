from vunit import VUnit

class FunctionalVerifier:
    def __init__(self, hdl_code, top_module):
        self.hdl_code = hdl_code
        self.top_module = top_module

    def run_verification(self):
        vu = VUnit.from_argv()
        lib = vu.add_library("lib")
        lib.add_source_string(self.hdl_code, file_name=f"{self.top_module}.vhd")
        try:
            vu.main()
            return "Verification passed!"
        except SystemExit as e:
            return f"Verification failed with exit code {e.code}"

# Usage example
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
verification_output = verifier.run_verification()
print(verification_output)
