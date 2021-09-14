#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `ksfest` package."""
# Any changes to the distributions library should be reinstalled with
#  pip install --upgrade .

# For running unit tests, use
# /usr/bin/python -m unittest test

from .ksfest.ksfest import ks_fest
import unittest


class TestKsfest(unittest.TestCase):
    """Tests for `ksfest` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.ksf = ks_fest()

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_initialization(self):
        self.assertEqual(self.gaussian.mean, 25, 'incorrect mean')
        self.assertEqual(self.gaussian.stdev, 2,
                         'incorrect standard deviation')
