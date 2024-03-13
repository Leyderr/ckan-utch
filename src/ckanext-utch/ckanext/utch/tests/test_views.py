"""Tests for views.py."""

import pytest

import ckanext.utch.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "utch")
@pytest.mark.usefixtures("with_plugins")
def test_utch_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("utch.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, utch!"
