import sys
from cx_Freeze import setup , executable

build_exe_options = {"packages": ["os"],"include":["pygame"]}
base =None
if sys.platform == "win32":
    base = "win32GUI"
setup(
    nome = "music player",
    version = "0.1",
    description = "toca musica",
    Options = {"build_exe": build_exe_options},
    executables = [executable("music.py",base=base)]
)