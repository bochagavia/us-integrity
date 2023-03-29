from django.db import models


class Leagues(models.Model):
    abbr = models.CharField(max_length=10)
    name = models.CharField(max_length=200)

    class Meta:  
        verbose_name_plural = 'Leagues'

    def __str__(self):
         return self.abbr


class Teams(models.Model):
    league = models.ForeignKey(Leagues, on_delete=models.SET_NULL, null=True)
    abbr = models.CharField(max_length=10)
    name = models.CharField(max_length=200)

    class Meta:  
        verbose_name_plural = 'Teams'

    def __str__(self):
         return self.abbr
