from django import forms

from journalmanager import choices


class ArticleTitleWidget(forms.widgets.MultiWidget):
    def __init__(self, attrs=None, choices=None):

        widget_list = (
            forms.widgets.TextInput(attrs),
            forms.widgets.Select(choices=choices)
        )
        super(ArticleTitleWidget, self).__init__(widget_list, attrs)

    def decompress(self, values):
        return values or (None, None)


class ArticleTitleField(forms.MultiValueField):

    def __init__(self, *args, **kwargs):
        fields = (
            forms.CharField(label='Title'),
            forms.ChoiceField(label='Language')
        )
        super(ArticleTitleField, self).__init__(fields, *args, **kwargs)
        self.widget = ArticleTitleWidget(choices=choices.LANGUAGE)

    def compress(self, data_list):
        if data_list:
            if data_list[0] in forms.fields.EMPTY_VALUES:
                raise forms.fields.ValidationError(u'Enter a valid title')
            if data_list[1] in forms.fields.EMPTY_VALUES:
                raise forms.fields.ValidationError(u'Enter a valid language')

            return {data_list[1]: data_list[0]}
        else:
            return None
