from django.test import TestCase
from django.core.exceptions import ValidationError
from core.models import Tag, Category, Project


class ProjectModelTest(TestCase):
    def setUp(self):
        # Create common tags and categories
        self.tag1 = Tag.objects.create(name="Python")
        self.tag2 = Tag.objects.create(name="Django")
        self.tag3 = Tag.objects.create(name="React")
        self.tag4 = Tag.objects.create(name="AWS")

        self.cat1 = Category.objects.create(name="Web Dev")
        self.cat2 = Category.objects.create(name="Data Science")
        self.cat3 = Category.objects.create(name="Mobile")
        self.cat4 = Category.objects.create(name="DevOps")

    def test_project_creation(self):
        project = Project.objects.create(name="My Portfolio")
        self.assertEqual(str(project), "My Portfolio")

    def test_max_three_tags_validation(self):
        """Should raise ValidationError if more than 3 tags are added."""
        project = Project.objects.create(name="Test Project")
        # Add 4 tags
        project.technologies.set([self.tag1, self.tag2, self.tag3, self.tag4])

        with self.assertRaises(ValidationError):
            project.full_clean()

    def test_max_three_categories_validation(self):
        """Should raise ValidationError if more than 3 categories are added."""
        project = Project.objects.create(name="Test Project")
        # Add 4 categories
        project.fields.set([self.cat1, self.cat2, self.cat3, self.cat4])

        with self.assertRaises(ValidationError):
            project.full_clean()

    def test_valid_project(self):
        """Should pass validation with exactly 3 items."""
        project = Project.objects.create(name="Valid Project")
        project.technologies.set([self.tag1, self.tag2, self.tag3])
        project.fields.set([self.cat1, self.cat2])

        # This should not raise any error
        project.full_clean()