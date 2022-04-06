from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Category
from django.contrib.auth.models import User
from rest_framework.test import APIClient

class PostTests(APITestCase):
    
    def test_view_posts(self):
        """
        Ensure we can view all objects.
        """
        url = reverse('blog_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def create_post(self):
        """
        Ensure we can create a new Post object and view object.
        """        
        self.test_category = Category.objects.create(name='django')        
        self.testuser1 = User.objects.create_user(username='test_user1', password='test_password')        
        data = {"title": "new",
                "author": 1,
                "excerpt": "new",
                "content": "new"}
        
        url = reverse('blog_api:listcreate')
        reponse = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        root = reverse(('blog_api:detailcreate'), kwargs={'pk': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status.code, status.HTTP_200_OK)
        
    def test_post_update_not_author(self):
        
        client = APIClient()
        
        self.test_category = Category.objects.create(name='django')        
        self.testuser1 = User.objects.create_user(username='test_user1', password='test_password')   
        self.testuser2 = User.objects.create_user(username='test_user2', password='test_password') 
        
        test_post = Post.objects.create(category_id=1, title='Post Title', excerpt='Post excerpt', 
            content='Post content', slug='post-title', author_id=1, status='published')
        
        client.login(username=self.testuser2.username, password="test_password")
        
        url = reverse(('blog_api:detailcreate'), kwargs={'pk': 1})
        
        response = client.put(
            url, {
                "id": 1,
                "title": "New",
                "author": 1,
                "excerpt": "New",
                "content": "New",
                "status": "published"
            }, format='json'
        )
        
        #print(response.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_post_update_author(self):
        
        client = APIClient()
        
        self.test_category = Category.objects.create(name='django')        
        self.testuser1 = User.objects.create_user(username='test_user1', password='test_password')   
        self.testuser2 = User.objects.create_user(username='test_user2', password='test_password') 
        
        test_post = Post.objects.create(category_id=1, title='Post Title', excerpt='Post excerpt', 
            content='Post content', slug='post-title', author_id=1, status='published')
        
        client.login(username=self.testuser1.username, password="test_password")
        
        url = reverse(('blog_api:detailcreate'), kwargs={'pk': 1})
        
        response = client.put(
            url, {
                "id": 1,
                "title": "New",
                "author": 1,
                "excerpt": "New",
                "content": "New",
                "status": "published"
            }, format='json'
        )
        
        #print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
      