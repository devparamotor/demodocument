from django.db import models



class UserDoc(models.Model):
    user_name = models.IntegerField()
    document_name = models.CharField(max_length=100)

    def __str__(self):
        return self.document_name