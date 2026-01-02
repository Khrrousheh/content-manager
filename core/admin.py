from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Tag, Category, Certificate, Blog, Note, Project


# --- CUSTOM FORMS ---

class ProjectAdminForm(forms.ModelForm):
    """
    Custom form for Project validation.
    M2M validation is handled here so the Admin can catch errors
    before the database save process.
    """

    class Meta:
        model = Project
        fields = '__all__'

    def clean_technologies(self):
        technologies = self.cleaned_data.get('technologies')
        if technologies and technologies.count() > 3:
            raise ValidationError("You can select a maximum of 3 technologies.")
        return technologies

    def clean_fields(self):
        fields = self.cleaned_data.get('fields')
        if fields and fields.count() > 3:
            raise ValidationError("You can select a maximum of 3 fields (categories).")
        return fields


# --- INLINES ---

class NoteInline(admin.TabularInline):
    """Allows adding/editing Notes directly inside the Blog admin page."""
    model = Note
    extra = 1
    fields = ('note_body', 'tag')


# --- ADMIN CLASSES ---

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'upload_date')
    list_filter = ('category', 'upload_date')
    filter_horizontal = ('tags',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'read_date', 'self_blog')
    list_filter = ('self_blog', 'categories', 'read_date')
    search_fields = ('name', 'short_description')
    filter_horizontal = ('categories', 'tags')
    inlines = [NoteInline]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm  # Link the custom validation form
    list_display = ('name', 'start_date', 'end_date', 'in_development')
    list_filter = ('in_development', 'fields', 'technologies')
    search_fields = ('name', 'short_description')

    # Side-by-side selection UI for ManyToMany fields
    filter_horizontal = ('technologies', 'fields')

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'short_description', 'repo_url')
        }),
        ('Classification', {
            'description': "<strong>Note:</strong> You can select a maximum of 3 items for each field below.",
            'fields': ('technologies', 'fields')
        }),
        ('Timeline', {
            'fields': ('start_date', 'end_date', 'in_development')
        }),
    )


# Note: We register Note via Blog Inline, but you can register it
# separately if you want a dedicated list view for all notes.
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('blog', 'tag', 'note_body_excerpt')
    list_filter = ('tag', 'blog')

    def note_body_excerpt(self, obj):
        return obj.note_body[:50] + "..." if len(obj.note_body) > 50 else obj.note_body

    note_body_excerpt.short_description = "Note Content"