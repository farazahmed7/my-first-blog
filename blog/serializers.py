from .models import Post,Search
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','text')
		
class SearchSerializer(serializers.ModelSerializer):
	class Meta:
		model=Search
		fields=('stream')