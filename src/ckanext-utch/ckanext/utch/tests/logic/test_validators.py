"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.utch.logic import validators


def test_utch_reauired_with_valid_value():
    assert validators.utch_required("value") == "value"


def test_utch_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.utch_required(None)
