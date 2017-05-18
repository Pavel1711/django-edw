#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from salmonella.widgets import SalmonellaIdWidget

from edw.models.term import BaseTerm, TermModel
from edw.models.entity import EntityModel
from edw.models.related import EntityRelationModel

from edw.admin.mptt.fields import FullPathTreeNodeChoiceField


#==============================================================================
# EntitiesUpdateRelationAdminForm
#==============================================================================
class EntitiesUpdateRelationAdminForm(forms.Form):

    to_set_term = FullPathTreeNodeChoiceField(queryset=TermModel.objects.attribute_is_relation(), required=False,
                                       joiner=' / ', label=_('Relation to set'))

    to_set_target = forms.ModelChoiceField(queryset=EntityModel.objects.all(), label=_('Target to set'),
                                              required=False, widget=SalmonellaIdWidget(
            EntityRelationModel._meta.get_field("to_entity").rel, admin.site))

    to_unset_term = FullPathTreeNodeChoiceField(queryset=TermModel.objects.attribute_is_relation(), required=False,
                                              joiner=' / ', label=_('Relation to unset'))

    to_unset_target = forms.ModelChoiceField(queryset=EntityModel.objects.all(), label=_('Target to unset'),
                                                required=False, widget=SalmonellaIdWidget(
            EntityRelationModel._meta.get_field("to_entity").rel, admin.site))

    def clean(self):
        cleaned_data = super(EntitiesUpdateRelationAdminForm, self).clean()
        to_set_term = cleaned_data.get("to_set_term")
        to_set_target = cleaned_data.get("to_set_target")

        to_unset_term = cleaned_data.get("to_unset_term")
        to_unset_target = cleaned_data.get("to_unset_target")

        if not (to_set_term or to_unset_term):
            raise forms.ValidationError(
                _("Select relation for set or unset")
            )

        if bool(to_set_term) ^ bool(to_set_target):
            raise forms.ValidationError(
                _("Select relation and target for set")
            )

        if bool(to_unset_term) ^ bool(to_unset_target):
            raise forms.ValidationError(
                _("Select relation and target for unset")
            )
        return cleaned_data
