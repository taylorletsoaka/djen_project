from django.db import models


# Create your models here.
class Paste(models.Model):
    text = models.TextField()
    name = models.CharField(max_length=40,blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or str(self.id)

    @models.permalink
    def get_absolute_url(self):
        # call the url named pastebin_paste_detail with the parameter 'id'
        return 'pastebin_paste_detail', [self.id]
