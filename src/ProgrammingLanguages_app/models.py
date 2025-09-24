from django.db import models
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

class Category(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural= "Categories"

    def __str__(self):
        return self.title
    
class PogrammingLanguage(models.Model):
    title = models.CharField(max_length=30)
    category = models.ForeignKey(Category, related_name="programming_language", on_delete=models.SET_NULL, null=True)
    code = models.TextField()
    language = models.CharField(max_length=50, default='python')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "PogrammingLanguages"

    def __str__(self):
        return self.title

    def get_highlighted_code(self):
        lexer = get_lexer_by_name(self.language)
        formatter = HtmlFormatter(style='monokai', full=True, lineos=True)  # Customize style as needed
        highlighted_code = highlight(self.code, lexer, formatter)
        return {"html": highlighted_code, "css": formatter.get_style_defs('.highlight')}
    



