import subprocess
import os

import pandas as pd
import numpy as np

from datetime import datetime

import requests
import json

def get_johns_hopkins():
    ''' Get data by a git pull request, the source code has to be pulled first
        Result is stored in the predifined csv structure. If there is no Repository 
        not present then clone the data from GitHub.
    '''
    
    if os.path.exists('data/raw/COVID-19-master/'):
        print('Repository Exists: Fetch the latest data from repository')
        git_pull = subprocess.Popen( "git pull" ,
                             cwd = os.path.dirname('data/raw/COVID-19-master/' ),
                             shell = True,
                             stdout = subprocess.PIPE,
                             stderr = subprocess.PIPE )
        (out, error) = git_pull.communicate()
    else:
        print('Repository not present. Fetch the entire repository')
        git_clone = subprocess.Popen( "git clone https://github.com/CSSEGISandData/COVID-19.git" ,
                             cwd = os.path.dirname('data/raw/' ),
                             shell = True,
                             stdout = subprocess.PIPE,
                             stderr = subprocess.PIPE )
        (out, error) = git_clone.communicate()

if __name__ == '__main__':
    get_johns_hopkins()