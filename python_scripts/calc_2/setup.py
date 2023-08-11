import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # For a GUI-based app on Windows

executables = [Executable("app.py", base=base)]

setup(
    name="CMGCalculator",
    version="1.0",
    description="A proud product of CMG Tech Lab.",
    executables=executables
)

