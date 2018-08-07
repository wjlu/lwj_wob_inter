# # -*- coding: utf-8 -*-
import unittest
from page.ntfgetnew import *
import HTMLTestRunner
import time
# import pdfkit
# import wkhtmltopdf


def allTestCase():
    suite = unittest.defaultTestLoader.discover(
        start_dir=os.path.dirname(__file__),
        pattern='test_*.py'
    )
    return suite


if __name__ =="__main__":
    timestr=time.strftime('%Y%m%d%H',time.localtime(time.time()))

    with open('report.html', 'wb') as f:
        runner=HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title=timestr+'wob商城接口自动化报告',
            description='wob商城接口自动化报告，用于定时检测接口正确性'
        ).run(allTestCase())


# with open('report.html') as f:
#     wkhtmltopdf.from_file(f,'report.pdf')

