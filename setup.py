import cx_Freeze
import os.path
os.environ['TCL_LIBRARY'] = r'C:\Users\Dulet\AppData\Local\Programs\Python\Python36\tcl\tk8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Dulet\AppData\Local\Programs\Python\Python36\tcl\tk8.6'


executables = [cx_Freeze.Executable("alien_invasion.py")]
files = ['images/alien2.png', 'images/alieneasy.png', 'images/alienred.png', 'images/autofire.png', 'images/bullet.png',
         'images/bullet1.png', 'images/bullet2.png', 'images/bullet3.png', 'images/bullet32.png', 'images/bullet33.png',
         'images/bulletspeed.png', 'images/double.png', 'images/laserred.png', 'images/laserred1.png',
         'images/laserred2.png', 'images/pierce.png', 'images/ship.png', 'images/shipspeed.png', 'images/star3.png',
         'images/triple.png', 'sounds/double.wav', 'sounds/triple.wav', 'sounds/boom2.wav',
         'sounds/hit.wav', 'sounds/bullet.wav']

cx_Freeze.setup(
    name="Shmup",
    options={"build_exe": {"packages": ["pygame"], "include_files": files}},
    executables=executables
)
