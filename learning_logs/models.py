from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=True)

    class Meta:
        unique_together = ('text', 'owner')

    def __str__(self):
        """Return a string representation of the model"""
        return self.text

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.text)
        return super().save(*args, **kwargs)


class Entry(models.Model):
    """something specific learned"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True)

    class Meta:
        verbose_name_plural = 'entries'
        unique_together = ('topic', 'text', 'id')

    def __str__(self):
        """Return a string representation of the model"""
        return self.text[:50]+"..." if len(self.text) > 50 else self.text

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.text)
        return super().save(*args, **kwargs)

    '''def save(self, *args, **kwargs):  # new
        if not self.slug:
            my_slug = slugify(self.text)
            startpoint = 1
            unique_slug = my_slug
            self.slug = my_slug
            while Entry.objects.filter(slug=unique_slug).exists():
                unique_slug = '{} {}'.format(my_slug, self.date_added)
                startpoint += 1
            self.slug = unique_slug
        return super().save(*args, **kwargs)'''



