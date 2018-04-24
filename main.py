#!/usr/bin/python3

import os
import subprocess
from subprocess import call,check_output,Popen

this_path = os.path.realpath('run.sh')

print os.system('export PATH=this_path/bin:$PATH')
# print check_output(['ls'])
# check_output('source ~/.bashrc',shell=True)
# call('bash run.sh'.split())
# Popen(['export','PATH='+this_path+'/bin:$PATH'],stdout=subprocess.PIPE)
