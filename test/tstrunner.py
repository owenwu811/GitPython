import unittest

loader = unittest.TestLoader()
start_dir = "."
suite = loader.discover(start_dir)

runner = unittest.TextTestRunner()
runner.run(suite)

#python3 -m unittest tstrunner.py 
