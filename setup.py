from setuptools import setup, find_packages

setup(
    name='FPGA_Development_Suite',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'PyQt5',  # For GUI development
        'pyverilog',  # For Verilog parsing and analysis
        'vunit_hdl',  # For VHDL and Verilog unit testing
        'pyopencl',  # For OpenCL integration
    ],
    entry_points={
        'console_scripts': [
            'fpga_dev_suite=src.main:main',
        ],
    },
)
