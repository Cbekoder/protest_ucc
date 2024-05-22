from django import forms
from django.contrib import admin
from .models import Science, Question, Option

class OptionFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()
        num_correct_options = 0
        for form in self.forms:
            if form.cleaned_data.get('is_correct'):
                num_correct_options += 1

        if num_correct_options != 1:
            raise forms.ValidationError("Bitta variant to'g'ri bo'lishi shart")

class OptionInline(admin.TabularInline):
    model = Option
    max_num = 4
    min_num = 4
    formset = OptionFormSet

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'science')
    search_fields = ('text', 'science__name')
    list_filter = ('science',)
    inlines = [OptionInline]

@admin.register(Science)
class ScienceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# @admin.register(Option)
# class OptionAdmin(admin.ModelAdmin):
#     list_display = ('option', 'question', 'is_correct')
#     search_fields = ('option', 'question__text')
#     list_filter = ('question', 'is_correct')
