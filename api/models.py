from django.db import models

from django.utils.html import format_html

from  django.core.validators import RegexValidator


class CommonInfoQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_gg=True)


class CommonInfoManager(models.Manager):
    def get_queryset(self):
        return CommonInfoQuerySet(self.model, using=self._db)

    def get_active(self, *args, **kwargs):
        items = super().all(*args, **kwargs)
        return items.filter(is_gg=True)
    
    # def active(self):
    #     return self.get_queryset().active()

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    is_gg = models.BooleanField()

    objects = CommonInfoQuerySet.as_manager()

class Person(models.Model):
    name = models.CharField(max_length=50, verbose_name='writerr', help_text="it's gg dude.")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Session(models.Model):
    name = models.CharField(max_length=50)

    book = models.ManyToManyField(Person, through='Membership')


    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Session, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)

class GEG(models.Model):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

    content = models.TextField(blank=True, null=True)

    birth = models.DateField(blank=True, null=True)
    is_active = models.BooleanField()
    people = models.ManyToManyField(Person, blank=True, null=True)
    number = models.CharField(max_length=50, blank=True, null=True, validators=[
            RegexValidator(
                regex='^(01)[0-9]{8}',
                message="number should be like this 0100000000.",
            ),
        ])
    color_code = models.CharField(max_length=6)

    def colored_name(self):
        return format_html(
            '<span style="color: #{};">Color</span>',
            self.color_code,
            )

    def __str__(self):
        return self.email


