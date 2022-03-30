import os
from multiprocessing import Process

import pytest


def main(path):
    # pytest.main(['%s' %path,'-m finished', '--html=report.html','--self-contained-html', '--capture=sys'])
    pytest.main(['%s' %path,'-n 3', '--html=report.html','--self-contained-html', '--capture=sys'])
    # pytest.main(['%s' %path,'-n=auto', '--html=report.html','--html=report.html', '--html=report.html'])
    # 在windows下报错，在centos是是可以的
    # cmd = 'pytest -s 大回归/小回归/  --workers 1 --tests-per-worker 2 --html=report.html --self-contained-html --capture=sys'
    # cmd = 'pytest -s testcase/大回归/小回归/冒烟 --th 10 --html=report.html --self-contained-html --capture=sys'
    # cmd = 'pytest -s testcase/大回归/小回归/冒烟 -n 3 --html=report.html --self-contained-html --capture=sys'


if __name__ == '__main__':
    # 大回归
    test_case = Process(target=main, args=("d:\\project\\auto_web_ui\\testcase\\大回归\\",))
    test_case.start()
    test_case.join()
    # 小回归

    # 冒烟
