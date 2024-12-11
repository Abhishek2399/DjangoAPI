"""
Following file will convert the model objects to json format data which is nothing but serializing the data
"""

from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the post model.
    1. Define the mode we want to serialize ( if we have used the ModelSerializer )
    2. Identify the props from the model we want to serialize

    Args:
        serializers (_type_): _description_
    """

    class Meta:
        model=Post
        # Method 2 - defining the fields we want to serialize
        fields = ['id', 'title', 'url', 'poster', 'created_at']

    # Method 1 - defining the fields we want to serialize
    # title = models.CharField(max_length=100)
    # url = models.URLField()
    # poster = models.ForeignKey(User, on_delete=models.CASCADE)
    # created_at = models.DataTimeField(auto_now_add=True)
