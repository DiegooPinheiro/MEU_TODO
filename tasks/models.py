from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField("Título", max_length=120)
    description = models.TextField("Descrição", blank=True)
    done = models.BooleanField("Concluído", default=False)
    created_at = models.DateTimeField("Criada em", auto_now_add=True)

    def __str__(self):
        return self.title
