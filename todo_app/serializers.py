
from rest_framework import serializers
from .models import TodoItem, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class TodoItemSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = TodoItem
        fields = ['id', 'title', 'description', 'due_date', 'tags', 'status']

    @staticmethod
    def get_existing_tags(tags_data):
        existing_tags = []
        for tag_data in tags_data:
            tag_name = tag_data['name']
            tag_instance, created = Tag.objects.get_or_create(name=tag_name)
            if not created:
                existing_tags.append({'id': tag_instance.id, 'name': tag_instance.name})
        return existing_tags

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        todo_item = TodoItem.objects.create(**validated_data)
        tags_instances = [Tag.objects.get_or_create(name=tag_data['name'])[0] for tag_data in tags_data]
        todo_item.tags.set(tags_instances)
        return todo_item
