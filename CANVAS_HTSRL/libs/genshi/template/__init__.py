# -*- coding: utf-8 -*-
#
# Copyright (C) 2006-2007 Edgewall Software
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution. The terms
# are also available at http://genshi.edgewall.org/wiki/License.
#
# This software consists of voluntary contributions made by many
# individuals. For the exact contribution history, see the revision
# history and logs, available at http://genshi.edgewall.org/log/.

"""Implementation of the template engine."""

from libs.genshi.template.base import Context, Template, TemplateError, \
                                 TemplateRuntimeError, TemplateSyntaxError, \
                                 BadDirectiveError
from libs.genshi.template.loader import TemplateLoader, TemplateNotFound
from libs.genshi.template.markup import MarkupTemplate
from libs.genshi.template.text import TextTemplate

__docformat__ = 'restructuredtext en'
