# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    entry_points='''
        [ckan.plugins]
        utch=ckanext.utch.plugin:UtchPlugin
    ''',

    message_extractors={
        'ckanext': [
            ('**.py', 'python', None),
            ('**.js', 'javascript', None),
            ('**/templates/**.html', 'ckan', None),
        ],
    }
)