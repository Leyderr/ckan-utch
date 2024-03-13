"""Tests for helpers.py."""

import ckanext.utch.helpers as helpers


def test_utch_hello():
    assert helpers.utch_hello() == "Hello, utch!"
