from vunit import VUnit

def run_vhdl_simulation(vhdl_code):
    vu = VUnit.from_argv()
    lib = vu.add_library("lib")
    lib.add_source_string(vhdl_code, file_name="test.vhd")
    vu.main()

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
        report "Hello, VHDL!";
        wait;
    end process;
end architecture;
"""
run_vhdl_simulation(vhdl_code)
