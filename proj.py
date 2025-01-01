# project related functions

import os

def get_project_path(name: str) -> str:
    curpath = os.path.abspath(__file__)
    while True:
        curpath = os.path.dirname(curpath)
        if curpath == '/':
            raise FileNotFoundError('project path not found')
        if os.path.basename(curpath) == name:
            return curpath


if __name__ == '__main__':
    print(get_project_path('shared'))

