from django import template


register = template.Library()


def fake_management_form(prefix, fields):
    total_fields = len([i for i in fields])
    if total_fields < 1:
        total_fields = 1
    snippet = '''
    <input id="id_{0}-TOTAL_FORMS" type="hidden" value="{1}" name="{0}-TOTAL_FORMS">
    <input id="id_{0}-INITIAL_FORMS" type="hidden" value="0" name="{0}-INITIAL_FORMS">
    <input id="id_{0}-MAX_NUM_FORMS" type="hidden" name="{0}-MAX_NUM_FORMS">
    '''.format(prefix, total_fields)

    return snippet.strip()

register.simple_tag(fake_management_form)
