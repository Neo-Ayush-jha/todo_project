from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status



class TodoItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class TodoItemListView(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

    def create(self, request, *args, **kwargs):
        create_new_tags = request.data.get('create_new_tags', True)  
        tags_data = request.data.get('tags', [])
        if not create_new_tags:
            existing_tags = TodoItemSerializer.get_existing_tags(tags_data)
            request.data['tags'] = existing_tags

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = serializer.save()

        headers = self.get_success_headers(serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

