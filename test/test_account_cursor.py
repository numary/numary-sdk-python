"""
    Ledger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ledgerclient
from ledgerclient.model.account import Account
from ledgerclient.model.account_cursor_all_of import AccountCursorAllOf
from ledgerclient.model.cursor import Cursor
globals()['Account'] = Account
globals()['AccountCursorAllOf'] = AccountCursorAllOf
globals()['Cursor'] = Cursor
from ledgerclient.model.account_cursor import AccountCursor


class TestAccountCursor(unittest.TestCase):
    """AccountCursor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAccountCursor(self):
        """Test AccountCursor"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AccountCursor()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
