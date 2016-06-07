from django import template
import datetime
import re
from django.db import models
from django.db import connection
from FirstApp.models import Blogger, Blog, Entry
from django.template.loader import get_template

#Opening the template library so we can register lattter
register = template.Library()


class CurrentTimeNode(template.Node):
    def __init__(self, format_string):
        self.format_string = str(format_string)

    def render(self, context):
        now = datetime.datetime.now()
        return now.strftime(self.format_string)
# Registering and creating tags
    @register.tag('current_time')
    def do_current_time(parser, token):
        try:
            # split_contents() knows not to split quoted strings.
            tag_name, format_string = token.split_contents()
        except ValueError:
            msg = '%r tag requires a single argument' % token.split_contents()[0]
            raise template.TemplateSyntaxError(msg)
        return CurrentTimeNode(format_string[1:-1])




#settings tags inside templates

class CurrentTimeNode3(template.Node):
    def __init__(self, format_string, var_name):
        self.format_string = str(format_string)
        self.var_name = var_name

    def render(self, context):
        now = datetime.datetime.now()
        context[self.var_name] = now.strftime(self.format_string)
        return ''
@register.tag
def do_current1_time(parser, token):
    # This version uses a regular expression to parse tag contents.
    try:
        # Splitting by None == splitting by spaces.
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        msg = '%r tag requires arguments' % token.contents[0]
        raise template.TemplateSyntaxError(msg)

    m = re.search(r'(.*?) as (\w+)', arg)
    if m:
        fmt, var_name = m.groups()
    else:
        msg = '%r tag had invalid arguments' % tag_name
        raise template.TemplateSyntaxError(msg)

    if not (fmt[0] == fmt[-1] and fmt[0] in ('"', "'")):
        msg = "%r tag's argument should be in quotes" % tag_name
        raise template.TemplateSyntaxError(msg)

    return CurrentTimeNode3(fmt[1:-1], var_name)

@register.simple_tag
def show_results(format_string):
    news_post = News.objects.all()
    return {'news_post': news_post}

class Item:
		@property
		def results(self):
			return News.objects.all()


## if you have an object you can define it as @property so you can get results without a call, e.g.

#class Item:
#    @property
#    def results(self):
#        return something
#then in the template:
#
#<% for result in item.results %>
#...
#<% endfor %>
