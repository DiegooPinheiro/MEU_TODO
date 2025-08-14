from django.db import models
from django.conf import settings

class Task(models.Model):
    title = models.CharField("Título", max_length=120)
    description = models.TextField("Descrição", blank=True)
    done = models.BooleanField("Concluída", default=False)
    created_at = models.DateTimeField("Criada em", auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Usuário",
        on_delete=models.CASCADE,
        related_name="tasks"
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"

    def __str__(self):
        return self.title
