from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=20)
    random_value = models.IntegerField()

    def __unicode__(self):
        return "This <b>objects name </b>is %s and random value %d" % (self.name, self.random_value)
