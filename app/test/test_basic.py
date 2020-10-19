import os
import sys
print ("os.getcwd() -> ",os.getcwd())
sys.path.append(os.getcwd())

from nose.tools import eq_, ok_
import unittest 
import json
import server

class BasicTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        self.app = server.app.test_client()
    
        # executed after each test
    def tearDown(self):
        pass
 
    ###############
    #### tests ####
    ###############
 
    def test_hello(self):
        res = self.app.get("/")
        eq_(200, res.status_code)

if __name__ == "__main__":
    unittest.main()