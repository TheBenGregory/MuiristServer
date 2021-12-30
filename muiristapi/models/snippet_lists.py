from django.db import models



class SnippetList(models.Model):

    lists = models.ForeignKey("List", on_delete=models.CASCADE)
    snippets = models.ForeignKey("Snippet", on_delete=models.CASCADE, related_name="snippet_lists")
