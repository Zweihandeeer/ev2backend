from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    class Meta:
        db_table = 'velasquezluis_usuarios'
    def __str__(self):
        return self.nombre
    def __unicode__(self):
        return self.nombre

# Create your models here.
class Chat(models.Model):
    chat = models.CharField(max_length= 140)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        db_table = 'velasquezluis_chats'
    def __str__(self):
        return str(self.user)
    def __unicode__(self):
        return self.user