# # -*- coding: utf-8 -*-

import unittest
from page.ntfgetnew import *



def allRun():
    suite = unittest.TestLoader().discover(
        start_dir=os.path.dirname(__file__)
    )

    unittest.TextTestRunner(verbosity=2).run(suite)




if __name__ == '__main__':
    allRun()