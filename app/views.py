# coding=utf-8

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render_to_response
import itertools
from django.template import RequestContext
import tablib
from app.forms import ConditionFormSet, ActionFormSet, KindForm


def _create_sub_header_columns(name, header_length):
    condition_columns = ([None] * header_length)
    condition_columns[0] = name
    return tuple(condition_columns)


def render_index(action_formset, condition_formset, kind_form, request):
    return render_to_response('index.html', RequestContext(request, {
        'kind_form': kind_form,
        'condition_formset': condition_formset,
        'action_formset': action_formset
    }))


def index(request):
    kind_form = KindForm(prefix='kind')
    condition_formset = ConditionFormSet(prefix='condition')
    action_formset = ActionFormSet(prefix='action')
    return render_index(action_formset, condition_formset, kind_form, request)


def export(request):

    kind_form = KindForm(request.POST, prefix="kind")
    condition_formset = ConditionFormSet(request.POST, prefix='condition')
    action_formset = ActionFormSet(request.POST, prefix='action')

    if all([formset.is_valid() for formset in [condition_formset, action_formset, kind_form]]):

        if kind_form.cleaned_data["kind"] == 'all':
            variations = list(itertools.product(*[form.variations() for form in condition_formset if form.variations()]))

        else:
            import metacomm.combinatorics.all_pairs2
            all_pairs = metacomm.combinatorics.all_pairs2.all_pairs2
            variations = list(all_pairs([form.variations() for form in condition_formset if form.variations()]))

        # ヘッダ
        rule_count = len(variations)
        if (rule_count > 255):
            messages.error(request, '条件の組み合わせが多すぎます。全組み合わせを選択している場合はペア構成で試してみてください。')
            return render_index(action_formset, condition_formset, kind_form, request)

        headers = [u"ルール%s" % i for i in range(1, rule_count+1)]
        headers.insert(0, '')
        header_length = len(headers)
        data = tablib.Dataset(headers=tuple(headers))

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
        return render_index(action_formset, condition_formset, kind_form, request)


