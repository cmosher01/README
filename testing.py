#!/usr/bin/python
import subprocess
p = subprocess.Popen('set', shell=True)
p.wait()
print('subprocess exit status: {}'.format(p.returncode))
