# serializers transform data into JSON
# It can also choose from the data to be added or not

from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','author','title','body','created_at',)
        model = Post