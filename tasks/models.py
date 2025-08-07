from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharFild("Titulo", max_length=120)
    description = models.TextField("Descrição", blank= True)
    done = models.BooleanField("Concluido", default=False)
    created_at = models.DatetimeField("Criada em", auto_now_add=True)

    def __str__(self):
        return self.title