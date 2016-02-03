from __future__ import absolute_import, division, with_statement

from tornado.test.util import unittest

from pilbox.errors import *


class ErrorsTest(unittest.TestCase):

    def test_unique_error_codes(self):
        errors = [SignatureError, ClientError, HostError, BackgroundError,
                  DimensionsError, FilterError, FormatError, ModeError,
                  OptimizeError, PositionError, PreserveExifError,
                  ProgressiveError, QualityError, UrlError, ImageFormatError,
                  ImageSaveError, FetchError, DegreeError, OperationError,
                  RectangleError, RetainError]
        codes = []
        for error in errors:
            code = str(error.get_code())
            if code in codes:
                self.fail("The error code, %s, is repeated" % str(code))
            codes.append(code)

    def test_base_not_implemented(self):
        self.assertRaises(NotImplementedError, PilboxError.get_code)
