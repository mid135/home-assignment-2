#!/usr/bin/env python
import unittest
import os
import sys
from tests.test_fail import PostTestCase
from tests.test_create import PostCreateTestCase
from tests.test_sanity import MainTestCase

source_dir = os.path.join(os.path.dirname(__file__), 'tests')

if __name__ == '__main__':

    if 'TTHA2PASSWORD' not in os.environ:
        sys.exit('No password set')

    suite = unittest.TestSuite((
        unittest.makeSuite(PostTestCase),
        unittest.makeSuite(PostCreateTestCase),
        unittest.makeSuite(MainTestCase),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
