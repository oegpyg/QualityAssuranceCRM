from django.db import models


class Status(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=50, blank=False, null=False)
    target_flow = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self) -> str:
        return f"{self.id} | {self.label}"
