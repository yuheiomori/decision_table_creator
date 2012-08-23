# coding=utf-8
from StringIO import StringIO
from django.http import HttpResponse
from django.shortcuts import render_to_response
import itertools
from django.template import RequestContext
import tablib
from app.forms import ConditionFormSet, ActionFormSet


def _create_sub_header_columns(name, header_length):
    condition_columns = ([None] * header_length)
    condition_columns[0] = name
    return tuple(condition_columns)


def index(request):

    condition_formset = ConditionFormSet(prefix='condition')
    action_formset = ActionFormSet(prefix='action')
    return render_to_response('index.html', RequestContext(request, {
    'condition_formset': condition_formset,
    'action_formset': action_formset
    }))


def export(request):

    condition_formset = ConditionFormSet(request.GET, prefix='condition')
    action_formset = ActionFormSet(request.GET, prefix='action')

    if all([formset.is_valid() for formset in [condition_formset,  action_formset]]):

        variation_counts = [len(form.variations()) for form in condition_formset if form.variations()]

        rule_count = 1
        for variation_count in variation_counts:
            rule_count = rule_count * variation_count

        headers = [u"ルール%s" % i for i in range(1, rule_count+1)]
        headers.insert(0, '')
        header_length = len(headers)

        data = tablib.Dataset(headers=tuple(headers))
        variations = list(itertools.product(*[form.variations() for form in condition_formset if form.variations()]))

        # 条件
        data.append(_create_sub_header_columns(u'条件', header_length))
        for i, condition_form in enumerate(condition_formset):

            if condition_form.variations():

                row = [ "    " + condition_form.cleaned_data['title']]
                for variation in variations:
                    row.append(variation[i])
                data.append(tuple(row))

        # アクション
        data.append(_create_sub_header_columns(u'アクション', header_length))
        for action_form in action_formset:
            if action_form.cleaned_data.get('title'):

                action_columns = [None] * header_length
                action_columns[0] = "    " + action_form.cleaned_data['title']
                data.append(tuple(action_columns))

        response = HttpResponse(data.xls,
                                mimetype='application/vnd.ms-excel; charset=utf-8')
        response['Content-Disposition'] = 'attachment; filename=decision_table.xls'

        return response

    else:
        return render_to_response('index.html', RequestContext(request, {
            'condition_formset': condition_formset,
            'action_formset': action_formset
        }))
