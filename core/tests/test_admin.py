from django.test import TestCase, Client
from django.contrib.admin.sites import site
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import Tag, Category, Project
from core.admin import ProjectAdmin


class AdminIntegrationTest(TestCase):
    def setUp(self):
        # 1. Create a superuser to access the admin
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@test.com',
            password='password123'
        )
        self.client = Client()
        self.client.login(username='admin', password='password123')

        # 2. Create sample data
        self.tags = [Tag.objects.create(name=f"Tag {i}") for i in range(5)]
        self.categories = [Category.objects.create(name=f"Cat {i}") for i in range(5)]

        # 3. URLs for Project Admin
        self.project_add_url = reverse('admin:core_project_add')

    def test_admin_registration(self):
        """Check if models are registered with the correct Admin classes."""
        self.assertIn(Project, site._registry)
        self.assertIsInstance(site._registry[Project], ProjectAdmin)

    def test_project_admin_ui_configuration(self):
        """Verify that filter_horizontal is correctly configured."""
        ma = site._registry[Project]
        self.assertEqual(ma.filter_horizontal, ('technologies', 'fields'))

    def test_max_three_validation_in_admin(self):
        """
        Functional test: Try to save a Project with 4 tags via POST request.
        """
        data = {
            'name': 'Overlimit Project',
            'short_description': 'Testing admin validation',
            'technologies': [t.id for t in self.tags[:4]],  # Sending 4 tags
            'fields': [c.id for c in self.categories[:2]],
            'in_development': 'on',
            '_save': 'Save'
        }

        response = self.client.post(self.project_add_url, data)

        # 1. Check status code is 200 (Form failed and stayed on page)
        self.assertEqual(response.status_code, 200)

        # 2. MATCH THE WORDING EXACTLY:
        self.assertContains(response, "You can select a maximum of 3 technologies.")

    def test_valid_project_admin_submission(self):
        """Functional test: Saving with 3 tags should succeed (302 redirect)."""
        data = {
            'name': 'Valid Admin Project',
            'short_description': 'This should work',
            'technologies': [t.id for t in self.tags[:3]],  # Exactly 3
            'fields': [c.id for c in self.categories[:1]],
            '_save': 'Save'
        }

        response = self.client.post(self.project_add_url, data)

        # Success results in a redirect to the changelist page
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Project.objects.filter(name='Valid Admin Project').exists())