#!/usr/bin/python
import subprocess
p = subprocess.Popen('ps -efH', shell=True)
p.wait()
print('subprocess exit status: {}'.format(p.returncode))
