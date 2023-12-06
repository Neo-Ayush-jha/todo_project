from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import TodoItem, Tag

class TodoItemModelTest(TestCase):
    def test_create_todo_item(self):
        todo_item = TodoItem.objects.create(
            title="Test Todo",
            description="This is a test todo item",
            status="OPEN"
        )
        self.assertTrue(isinstance(todo_item, TodoItem))
        self.assertEqual(str(todo_item), todo_item.title)

class TodoItemApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.todo_url = reverse('todo-list')
        self.tag = Tag.objects.create(name='TestTag')

    def test_create_todo_item(self):
        data = {
            'title': 'Test Todo',
            'description': 'This is a test todo item',
            'status': 'OPEN',
            'tags': [self.tag.id]
        }
        response = self.client.post(self.todo_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TodoItem.objects.count(), 1)
        self.assertEqual(TodoItem.objects.get().title, 'Test Todo')

    def test_read_todo_item(self):
        todo_item = TodoItem.objects.create(
            title='Test Todo',
            description='This is a test todo item',
            status='OPEN'
        )
        response = self.client.get(reverse('todo-detail', args=[todo_item.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Todo')

    def test_update_todo_item(self):
        todo_item = TodoItem.objects.create(
            title='Test Todo',
            description='This is a test todo item',
            status='OPEN'
        )
        updated_data = {
            'title': 'Updated Todo',
            'description': 'This is an updated todo item description',
            'status': 'WORKING'
        }
        response = self.client.put(reverse('todo-detail', args=[todo_item.id]), updated_data, format='json')

        # Assert the status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Fetch the latest data from the database
        todo_item.refresh_from_db()

        # Assert other fields
        self.assertEqual(todo_item.title, 'Updated Todo')
        self.assertEqual(todo_item.description, 'This is an updated todo item description')
        self.assertEqual(todo_item.status, 'WORKING')

    def test_delete_todo_item(self):
        todo_item = TodoItem.objects.create(
            title='Test Todo',
            description='This is a test todo item',
            status='OPEN'
        )
        response = self.client.delete(reverse('todo-detail', args=[todo_item.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(TodoItem.objects.count(), 0)


from django.test import TestCase
from django.core.wsgi import get_wsgi_application

class WSGITestCase(TestCase):
    def test_wsgi_application(self):
        application = get_wsgi_application()
        self.assertIsNotNone(application)