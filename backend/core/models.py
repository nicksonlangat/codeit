import uuid
import random, string
from django.db import models
from django.utils import timezone
from django.contrib import admin


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-updated_at",]


class Code(BaseModel):
    snippet = models.TextField()


class SharedLink(BaseModel):
    code = models.OneToOneField(Code, on_delete=models.CASCADE)
    link = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.link is None:
            self.link = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        super(SharedLink, self).save(*args, **kwargs)


admin.site.register(Code)
admin.site.register(SharedLink)
