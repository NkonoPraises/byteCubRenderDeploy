from django.db import models

class SearchByteCub(models.Model):
    # title = models.CharField(max_length=200, blank=True)
    url_name = models.CharField(max_length=255, help_text="The full HTML link snippet, e.g., '<a href=\"{% url 'link_name' %}\"><li class=\"class name\"> Some name</li></a>'")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url_name
