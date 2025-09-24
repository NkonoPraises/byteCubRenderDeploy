from django.contrib import admin
from ProgrammingLanguages_app.models import Category, PogrammingLanguage


class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'language','created_at']

admin.site.register(Category)
admin.site.register(PogrammingLanguage, ProgrammingLanguageAdmin)
