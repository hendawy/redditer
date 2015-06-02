from django.db import models
from django.utils.translation import ugettext_lazy as _


class StarModel(models.Model):
    email = models.EmailField()
    listing = models.CharField(max_length=20)

    class Meta:
        verbose_name = _('StarModel')
        verbose_name_plural = _('StarModel')
        unique_together = ('email', 'listing',)

    def __unicode__(self):
        return '%s:%s' % (self.email, self.listing)
