from django.db import models

class Article(models.Model):
    titre = models.CharField(max_length=200)
    image = models.ImageField(upload_to='news/', null=True, blank=True)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Actualité"
        ordering = ['-date_publication'] # Les plus récents en premier

    def __str__(self):
        return self.titre