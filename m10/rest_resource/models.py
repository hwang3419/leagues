from django.db import models
from tastypie.utils.timezone import now
from django.contrib.auth.models import User
from tastypie.cache import SimpleCache

class Test(models.Model):
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField(default=now)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        return super(Test, self).save(*args, **kwargs)

class base(models.Model):
    class Meta:
        abstract = True
    Div = models.CharField(max_length = 5)
    Date = models.DateField()
    HomeTeam = models.CharField(max_length = 30)
    AwayTeam = models.CharField(max_length = 30)
    FTHG = models.IntegerField()
    FTAG = models.IntegerField()
    FTR = models.CharField(max_length = 1)
    HTHG = models.IntegerField(null = True)
    HTAG = models.IntegerField(null = True)
    HTR = models.CharField(max_length = 1, null = True)
    Referee = models.CharField(max_length = 30, null = True)
    HS = models.IntegerField(null = True)
    AS = models.IntegerField(null = True)
    HST = models.IntegerField(null = True)
    AST = models.IntegerField(null = True)
    HF = models.IntegerField(null = True)
    AF = models.IntegerField(null = True)
    HC = models.IntegerField(null = True)
    AC = models.IntegerField(null = True)
    HY = models.IntegerField(null = True)
    AY = models.IntegerField(null = True)
    HR = models.IntegerField(null = True)
    AR = models.IntegerField(null = True)
    B365H = models.FloatField(null = True)
    B365D = models.FloatField(null = True)
    B365A = models.FloatField(null = True)
    
    def __unicode__(self):
        return 'Raw data from%s'%self.Div

class SP1(base):
    pass


class E0(base):
    pass


class D1(base):
    pass

class I1(base):
    pass

class teambase(models.Model):
    class Meta:
        abstract = True
    name = models.CharField(max_length = 30)
    games = models.IntegerField()

class SP1teams(teambase):
    pass
    
class E0teams(teambase):
    pass

class I1teams(teambase):
    pass

class D1teams(teambase):
    pass