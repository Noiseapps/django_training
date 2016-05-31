from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return "This <b>objects name </b>is %s" % self.name
