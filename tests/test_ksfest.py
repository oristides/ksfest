#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `ksfest` package."""


import unittest
import click
from click.testing import CliRunner

from ksfest import ksfest


class TestKsfest(unittest.TestCase):
    """Tests for `ksfest` package."""


    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_ks_fest_dicts(self):
    import pandas as pd
        """Test something."""
    iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
    gks=ksfest.ks_fest()
    
    OUTPUT=gks.get_ks(iris,var_dim='species', sample=0.3, na_number=-1)
    self.AssertIsInstance(OUTPUT, pd.DataFrame)