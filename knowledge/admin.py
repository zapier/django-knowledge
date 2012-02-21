from django.contrib import admin

from knowledge.models import Question, Response, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Category._meta.fields]
    prepopulated_fields = {'slug': ('title', )}
admin.site.register(Category, CategoryAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Question._meta.fields]
    list_select_related = True
admin.site.register(Question, QuestionAdmin)


class ResponseAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Response._meta.fields]
    list_select_related = True
admin.site.register(Response, ResponseAdmin)
