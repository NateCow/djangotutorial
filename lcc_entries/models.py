from django.db import models

# Create your models here.

# Some sets of choices to use in the models
# From Django documentation:
# must be a mapping of actual values to human readable names or an iterable containing (actual value, human readable name) tuples.

# Should thinkg about what the actual values should be here. List of years should probably be its own list then.
COMP_NAMES = (
    (2002, "LCC"),
    (2004, "LCC 2.5"),
    (2004, "LCC III"),
    (2005, "LCC IV"),
    (2007, "LCC V"),
    (2008, "LCC VI"),
    (2009, "LCC VII"),
    (2010, "LCC VIII"),
    (2011, "LCC IX"),
    (2012, "LCC X"),
    (2013, "LCC XI"),
    (2014, "LCC XII"),
    (2015, "LCC 2015"),
    (2016, "LCC 2016"),
    (2017, "LCC 2017"),
    (2018, "LCC 2018"),
    (2019, "SaberComp 2019"),
    (2020, "SaberComp 2020"),
    (2021, "SaberComp 2021"),
    (2022, "SaberComp 2022"),
    (2023, "SaberComp 2023"),
    (2024, "SaberComp 2024"),
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
    # name = models.CharField(choices=COMP_NAMES, max_length=200, unique=True)
    name = models.CharField(choices=[(name, name) for _, name in COMP_NAMES], max_length=200, unique=True)
    # year = models.IntegerField(choices=COMP_NAMES, unique=True)
    year = models.IntegerField(choices=[(year, year) for year, _ in COMP_NAMES], unique=False)
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
    title = models.CharField(max_length=200)
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
        
