import unittest

# Discover all tests in the tests/ folder
loader = unittest.TestLoader()
suite = loader.discover('tests')

runner = unittest.TextTestRunner()
runner.run(suite)
