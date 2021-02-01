from django.db import models
class table(models.Model):
    url = models.CharField(max_length=200, null=False)
    result = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.result


