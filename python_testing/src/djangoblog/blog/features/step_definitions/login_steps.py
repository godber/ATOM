# -*- coding: utf-8 -*-
from lettuce import *
from nose.tools import assert_equals # why not unittest?
from lxml import html

@step(u'When I navigate to the login page')
def when_i_navigate_to_the_login_page(step):
    # world.browser is set in terrain.py
    response = world.browser.get('/admin/')
    world.dom = html.fromstring(response.content)
    assert_equals(200, response.status_code)

@step(u'Then I see the header \'(.*)\'')
def then_i_see_the_header_group1(step, group1):
    header = world.dom.cssselect('h1')[0]
    assert_equals(group1,header.text)

