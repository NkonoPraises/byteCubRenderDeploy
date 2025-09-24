
from django.db import models
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

class Category1(models.Model):
    name = models.CharField(max_length=100,default="name")

    def __str__(self):
        return self.name

class CodeSnippet1(models.Model):
    title = models.CharField(max_length=200)
    code = models.TextField()
    language = models.CharField(max_length=50, default='python')
    category = models.ForeignKey(Category1, on_delete=models.CASCADE, related_name='snippets',null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_highlighted_code(self):
        lexer = get_lexer_by_name(self.language)
        formatter = HtmlFormatter(style='monokai', full=True, lineos=True)  # Customize style as needed
        highlighted_code = highlight(self.code, lexer, formatter)
        return {"html": highlighted_code, "css": formatter.get_style_defs('.highlight')}