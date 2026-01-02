from django.db import models
from django.core.exceptions import ValidationError

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Certificate(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    upload_date = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    name = models.CharField(max_length=250)
    short_description = models.TextField(max_length=500, null=True, blank=True)
    read_date = models.DateField()
    categories = models.ManyToManyField(Category, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    self_blog = models.BooleanField(default=False)
    blog_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class Note(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="notes")
    note_body = models.TextField(max_length=750)
    tag = models.ForeignKey(Tag, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Note for {self.blog.name}"

class Project(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    short_description = models.TextField(max_length=250, blank=True)
    # Changed 'name=' to standard field naming
    technologies = models.ManyToManyField(Tag, blank=True)
    fields = models.ManyToManyField(Category, blank=True)
    start_date = models.DateField(null=True, blank=True)
    in_development = models.BooleanField(default=True)
    end_date = models.DateField(null=True, blank=True)
    repo_url = models.URLField(null=True, blank=True)

    def clean(self):
        """Custom validation for M2M limits."""
        super().clean()
        # Validation for existing projects (M2M requires a PK)
        if self.pk:
            if self.technologies.count() > 3:
                raise ValidationError({'technologies': "A project can have at most 3 technologies (tags)."})
            if self.fields.count() > 3:
                raise ValidationError({'fields': "A project can have at most 3 fields (categories)."})

    def __str__(self):
        return self.name or "Unnamed Project"