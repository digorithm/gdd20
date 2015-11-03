# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required

class SearchRecipes(Form):
	recipe_item = TextField('item', [Required(message=u'Enter the item of revenue to be searched')])