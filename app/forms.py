# coding=utf-8
from django import forms
from django.forms.formsets import formset_factory


class KindForm(forms.Form):
    KIND_CHOICES = (
        ('all', u'全組み合わせ'),
        ('pair', u'ペア構成')
    )
    kind = forms.ChoiceField(required=True, label=u"種別", choices=KIND_CHOICES)


class ConditionForm(forms.Form):
    title = forms.CharField(label=u"条件", max_length=100, required=True,
                            widget=forms.TextInput(
                                attrs={'placeholder': u'項目名'}))
    variation1 = forms.CharField(label=u"選択肢1", max_length=40, required=None,
                                 widget=forms.TextInput(
                                     attrs={'placeholder': u'選択肢1'}))
    variation2 = forms.CharField(label=u"選択肢2", max_length=40, required=None,
                                 widget=forms.TextInput(
                                     attrs={'placeholder': u'選択肢2'}))
    variation3 = forms.CharField(label=u"選択肢3", max_length=40, required=None,
                                 widget=forms.TextInput(
                                     attrs={'placeholder': u'選択肢3'}))
    variation4 = forms.CharField(label=u"選択肢4", max_length=40, required=None,
                                 widget=forms.TextInput(
                                     attrs={'placeholder': u'選択肢4'}))
    variation5 = forms.CharField(label=u"選択肢5", max_length=40, required=None,
                                 widget=forms.TextInput(
                                     attrs={'placeholder': u'選択肢5'}))
    variation6 = forms.CharField(label=u"選択肢6", max_length=40, required=None,
                                 widget=forms.TextInput(
                                     attrs={'placeholder': u'選択肢6'}))
    variation7 = forms.CharField(label=u"選択肢7", max_length=40, required=None,
                                 widget=forms.TextInput(
                                     attrs={'placeholder': u'選択肢7'}))
    variation8 = forms.CharField(label=u"選択肢8", max_length=40, required=None,
                                 widget=forms.TextInput(
                                     attrs={'placeholder': u'選択肢8'}))
    variation9 = forms.CharField(label=u"選択肢9", max_length=40, required=None,
                                 widget=forms.TextInput(
                                     attrs={'placeholder': u'選択肢9'}))
    variation10 = forms.CharField(label=u"選択肢10", max_length=40, required=None,
                                  widget=forms.TextInput(
                                      attrs={'placeholder': u'選択肢10'}))

    def variations(self):
        return [variation for variation in [
            self.cleaned_data.get('variation1'),
            self.cleaned_data.get('variation2'),
            self.cleaned_data.get('variation3'),
            self.cleaned_data.get('variation4'),
            self.cleaned_data.get('variation5'),
            self.cleaned_data.get('variation6'),
            self.cleaned_data.get('variation7'),
            self.cleaned_data.get('variation8'),
            self.cleaned_data.get('variation9'),
            self.cleaned_data.get('variation10')] if variation]


ConditionFormSet = formset_factory(ConditionForm, extra=10, max_num=10)


class ActionForm(forms.Form):
    title = forms.CharField(label=u"アクション", max_length=100, required=None)


ActionFormSet = formset_factory(ActionForm, extra=5, max_num=5)
