from django import forms
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper
from blog.models import Comment, Post
from ckeditor.widgets import CKEditorWidget

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        # Adjust textarea size for content field
        self.fields['content'].widget.attrs['rows'] = 2
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['rating', 'author', 'created_at', 'modified_at', 'published_at']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
            'content': CKEditorWidget(config_name='default') 
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Auto-fill slug field based on title
        self.fields['summary'].widget.attrs['rows'] = 2
        self.fields['title'].widget.attrs['rows'] = 1
        self.fields['slug'].widget.attrs['readonly'] = True  # Make slug readonly
        self.fields['slug'].widget.attrs['style'] = 'background-color: #333; color: #fff;'  # Style to indicate readonly
        self.fields['title'].widget.attrs['onchange'] = 'set_slug(this.value)'  # Call JavaScript function to set slug
        self.fields['title'].widget.attrs['onkeyup'] = 'set_slug(this.value)'  # Call JavaScript function to set slug
        # Modify hero_image field
        self.fields['hero_image'].widget.attrs['accept'] = 'image/*'  # Allow only image files
        # Hide labels for hero_image field
        self.fields['hero_image'].label = False
        self.fields['content'].label = False

    # Override save method to auto-generate slug
    def save(self, commit=True):
        instance = super().save(commit=False)
        # Generate slug from title
        instance.slug = instance.title.lower().replace(' ', '_')
        if commit:
            instance.save()
        return instance

