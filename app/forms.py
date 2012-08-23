# coding=utf-8
from django import forms
from django.forms.formsets import formset_factory

class ConditionForm(forms.Form):
    title = forms.CharField(label=u"条件",  max_length=100, required=None)
    variation1 = forms.CharField(label=u"選択肢1", max_length=40, required=None)
    variation2 = forms.CharField(label=u"選択肢2", max_length=40, required=None)
    variation3 = forms.CharField(label=u"選択肢3", max_length=40, required=None)
    variation4 = forms.CharField(label=u"選択肢4", max_length=40, required=None)
    variation5 = forms.CharField(label=u"選択肢5", max_length=40, required=None)

    def variations(self):
        return  [variation for variation in [
        self.cleaned_data.get('variation1'),
        self.cleaned_data.get('variation2'),
        self.cleaned_data.get('variation3'),
        self.cleaned_data.get('variation4'),
        self.cleaned_data.get('variation5')] if variation]

ConditionFormSet = formset_factory(ConditionForm, extra=5, max_num=5)


class ActionForm(forms.Form):
    title = forms.CharField(label=u"アクション", max_length=100, required=None)

ActionFormSet = formset_factory(ActionForm,  extra=5, max_num=5)






