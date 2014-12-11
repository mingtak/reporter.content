import doctest
import unittest

from Testing import ZopeTestCase as ztc

from Products.Five import zcml
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
from Products.PloneTestCase.layer import onsetup

import reporter.content

OPTION_FLAGS = doctest.NORMALIZE_WHITESPACE | \
               doctest.ELLIPSIS

ptc.setupPloneSite(products=['reporter.content'])


class TestCase(ptc.PloneTestCase):

    class layer(PloneSite):

        @classmethod
        def setUp(cls):
            zcml.load_config('configure.zcml',
              reporter.content)

        @classmethod
        def tearDown(cls):
            pass


def test_suite():
    return unittest.TestSuite([

        # Unit tests
        #doctestunit.DocFileSuite(
        #    'README.txt', package='reporter.content',
        #    setUp=testing.setUp, tearDown=testing.tearDown),

        #doctestunit.DocTestSuite(
        #    module='reporter.content.mymodule',
        #    setUp=testing.setUp, tearDown=testing.tearDown),


        # Integration tests that use PloneTestCase
        ztc.ZopeDocFileSuite(
            'INTEGRATION.txt',
            package='reporter.content',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),

        # -*- extra stuff goes here -*-

        # Integration tests for Author
        ztc.ZopeDocFileSuite(
            'Author.txt',
            package='reporter.content',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),


        # Integration tests for EventInfo
        ztc.ZopeDocFileSuite(
            'EventInfo.txt',
            package='reporter.content',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),


        # Integration tests for Competition
        ztc.ZopeDocFileSuite(
            'Competition.txt',
            package='reporter.content',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),


        # Integration tests for Article
        ztc.ZopeDocFileSuite(
            'Article.txt',
            package='reporter.content',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),


        # Integration tests for CustomNews
        ztc.ZopeDocFileSuite(
            'CustomNews.txt',
            package='reporter.content',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),


        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
