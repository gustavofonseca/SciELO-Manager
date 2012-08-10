# coding: utf-8

from django import (
    forms,
)


# class AbstractForm(forms.Form):
#     language = forms.SelectField('Language', choices=[('pt', 'Portuguese')])
#     abstract = forms.CharField('Title')


# class DatesForm(forms.Form):
#     thesis = forms.DateField()
#     conference = forms.DateField()
#     publication = forms.DateField()
#     revision = forms.DateField()


class PagesForm(forms.Form):
    first = forms.IntegerField()
    last = forms.IntegerField()


# class AffiliationForm(forms.Form):
#     name = forms.CharField('Name')
#     divisions = forms.FieldList(forms.CharField(),
#                                  min_entries=1)


# class AnalyticalAuthorForm(forms.Form):
#     firstname = forms.CharField('Firstname')
#     lastname = forms.CharField('Lastname')
#     role = forms.SelectField('Role', choices=[('coord', 'Coordinator')])
#     affiliations = forms.FieldList(forms.FormField(AffiliationForm),
#                                     min_entries=1)


# class CorporateAuthorForm(forms.Form):
#     name = forms.CharField('Name')
#     divisions = forms.FieldList(forms.CharField(),
#                                  min_entries=1)


# class TitleForm(forms.Form):
#     language = forms.SelectField('Language', choices=[('pt', 'Portuguese')])
#     title = forms.CharField('Title')


class ArticleForm(forms.Form):
    language = forms.CharField('Language')
    publication_city = forms.CharField('City of publication')
    publication_state = forms.CharField('State of publication')
    publication_country = forms.CharField('Country of publication')
    doctopic = forms.CharField('Doctopic')
    created_at = forms.DateField()
    bibliographic_standard = forms.CharField('Bibliographic standard')
    sponsor = forms.CharField()
    type_literature = forms.CharField('Type of literature')
    pid = forms.CharField('PID')
