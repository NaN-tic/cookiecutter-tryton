# This file is part {{ cookiecutter.module_name }} module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.tests.test_tryton import ModuleTestCase


class {{ cookiecutter.module_name.replace('_', ' ').title().replace(' ', '') }}TestCase(ModuleTestCase):
    'Test {{ cookiecutter.module_name.replace('_', ' ').title() }} module'
    module = '{{ cookiecutter.module_name }}'

del ModuleTestCase
