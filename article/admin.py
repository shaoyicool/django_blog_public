from django.contrib import admin

# Register your models here.
from .models import ArticlePost

admin.site.register(ArticlePost)

from .models import ArticleColumn

# 注册文章栏目
admin.site.register(ArticleColumn)