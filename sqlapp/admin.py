from django.contrib import admin

from .models import Practice, PracticeChoice, Codepractice, Book, Category, Quota

admin.site.register(Practice)
admin.site.register(PracticeChoice)
admin.site.register(Codepractice)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Quota)
