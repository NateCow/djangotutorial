from django.db import models

# Create your models here.

# Some sets of choices to use in the models
# From Django documentation:
# must be a mapping of actual values to human readable names or an iterable containing (actual value, human readable name) tuples.

# Should think about what the actual values should be here. List of years should probably be its own list then.
COMP_NAMES = (
    ("LCC1", "Lightsaber Choreography Competition"),
    ("LCC2", "Lightsaber Choreography Competition 2.5"),
    ("LCC3", "Lightsaber Choreography Contest III"),
    ("LCC4", "Lightsaber Choreography Competition IV"),
    ("LCC5", "Lightsaber Choreography Contest V"),
    ("LCC6", "Lightsaber Choreography Contest VI"),
    ("LCC7", "Lightsaber Choreography Contest VII"), # Previously just LCC
    ("LCC8", "Lightsaber Choreography Competition VIII"),
    ("LCC9", "Lightsaber Choreography Competition IX"), # Previously just LCC
    ("LCC10", "Lightsaber Choreography Competition X"),
    ("LCC11", "Lightsaber Choreography Contest XI"),
    ("LCC12", "Lightsaber Choreography Contest XII"), # Previously just LCC
    ("LCC2015", "Lightsaber Choreography Contest 2015"), # Previously just LCC
    ("LCC2016", "Lightsaber Choreography Competition 2016"),
    ("LCC2017", "Lightsaber Choreography Competition 2017"), # Previously just LCC
    ("LCC2018", "Lightsaber Choreography Competition 2018"),
    ("SC19", "SaberComp 2019"),
    ("SC20", "SaberComp 2020"),
    ("SC21", "SaberComp 2021"),
    ("SC22", "SaberComp 2022"),
    ("SC23", "SaberComp 2023"),
    ("SC24", "SaberComp 2024"),
)

COMP_YEARS = (
    ("LCC1", 2002),
    ("LCC2", 2004), # 2003-2004
    ("LCC3", 2004), # 2004-2005
    ("LCC4", 2005),
    ("LCC5", 2007),
    ("LCC6", 2008),
    ("LCC7", 2009),
    ("LCC8", 2010),
    ("LCC9", 2011),
    ("LCC10", 2012),
    ("LCC11", 2013),
    ("LCC12", 2014),
    ("LCC2015", 2015),
    ("LCC2016", 2016),
    ("LCC2017", 2017),
    ("LCC2018", 2018),
    ("SC19", 2019),
    ("SC20", 2020),
    ("SC21", 2021),
    ("SC22", 2022),
    ("SC23", 2023),
    ("SC24", 2024),
)

ENTRY_STATUS = [
    ("Pending", "Pending Review"),
    ("Accepted", "Accepted"),
    ("Rejected", "Rejected"),
    ("Disqualified", "Disqualified"),
    ("Withdrawn", "Withdrawn"),
    ("Live", "Live"),
]


class LCCComp(models.Model):
    name = models.CharField(choices=COMP_NAMES, max_length=200, unique=True)
    # name = models.CharField(choices=[(name, name) for _, name in COMP_NAMES], max_length=200, unique=True)
    year = models.CharField(choices=COMP_YEARS, max_length=200, unique=True)
    # year = models.CharField(choices=[(year, year) for _, year in COMP_YEARS], max_length=10, unique=False)
    start_date = models.DateField(default="2020-05-04")
    end_date = models.DateField(default="2020-12-31")
    theme = models.CharField(max_length=200, blank=True, null=True, default="")
    rules = models.TextField(default="No rules. (This is a default value)", max_length=2000)
    announcment_promo = models.URLField(blank=True, null=True, default="http://", max_length=200)
    live_judging = models.URLField(blank=True, null=True, default="http://", max_length=200)
    highlight_reel = models.URLField(blank=True, null=True, default="http://", max_length=200)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "LCC Competition"
        verbose_name_plural = "LCC Competitions"
    
class LCCCreator(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "LCC Creator"
        verbose_name_plural = "LCC Creators"
    

class LCCEntry(models.Model):
    title = models.CharField(max_length=200, default="Untitled")
    status = models.CharField(max_length=200, choices=ENTRY_STATUS, default="Pending Review")
    top_10 = models.BooleanField(default=False)
    youtube_link = models.URLField(max_length=200)
    competition_name = models.ForeignKey(LCCComp, to_field='name', related_name="entries_by_name", on_delete=models.CASCADE)
    competition_year = models.ForeignKey(LCCComp, to_field='year', related_name="entries_by_year", on_delete=models.CASCADE)
    # competition_name = models.CharField(max_length=200)
    # competition_year = models.IntegerField()
    creator = models.ForeignKey(LCCCreator, related_name="entries", on_delete=models.CASCADE)
    production_company = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return self.title
    
    def competition_year(self):
        return self.competition_name.year
    
    class Meta:
        verbose_name = "LCC Entry"
        verbose_name_plural = "LCC Entries"
        
