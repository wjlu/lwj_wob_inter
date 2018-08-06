# # -*- coding: utf-8 -*-

import unittest
from page.ntfgetnew import *
import HTMLTestRunner
import time
# def allRun():
#     suite = unittest.TestLoader().discover(
#         start_dir=os.path.dirname(__file__)
#     )
#
#     unittest.TextTestRunner(verbosity=2).run(suite)
# allRun()



def allTestCase():
    suite = unittest.defaultTestLoader.discover(
        start_dir=os.path.dirname(__file__),
        pattern='test_*.py'
    )
    return suite


def run():

    HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='wob商城接口自动化报告',
        description='wob商城接口自动化报告，用于定时检测接口正确性'
    ).run(allTestCase())

if __name__ =="__main__":
    timestr=time.strftime('%Y%m%d%H',time.localtime(time.time()))
    filename = timestr+'AutoTest.html'
    with open('report.html', 'wb') as f:
        runner=HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title='wob商城接口自动化报告',
            description='wob商城接口自动化报告，用于定时检测接口正确性'
        ).run(allTestCase())

