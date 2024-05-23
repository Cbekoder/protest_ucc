from django.contrib import admin
from django import forms
from .models import Science, Question, Option, UserTest, UserTestQuestion, UserTestAnswer


# @admin.register(Science)
# class ScienceAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     search_fields = ('name',)

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

# @admin.register(Option)
# class OptionAdmin(admin.ModelAdmin):
#     list_display = ('question', 'option', 'is_correct')
#     search_fields = ('question__text', 'option')

@admin.register(UserTest)
class UserTestAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    search_fields = ('user__username', 'created_at')
    list_filter = ('created_at',)

@admin.register(UserTestQuestion)
class UserTestQuestionAdmin(admin.ModelAdmin):
    list_display = ('user_test', 'question', 'order')
    search_fields = ('user_test__user__username', 'question__text')
    list_filter = ('user_test',)

@admin.register(UserTestAnswer)
class UserTestAnswerAdmin(admin.ModelAdmin):
    list_display = ('user_test_question', 'selected_option')
    search_fields = ('user_test_question__question__text', 'selected_option__option')
    list_filter = ('user_test_question',)

