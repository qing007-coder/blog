from rest_framework import serializers
from .models import *

class ArticleSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')  # 显示选择字段的显示值

    class Meta:
        model = Article
        fields = [
            'id', 'title', 'content',
            'category', 'created_at', 'updated_at'
        ]


