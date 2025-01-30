from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

# Define your choices
COMP_NAMES = (
    ("LCC01", "Lightsaber Choreography Competition"),
    ("LCC02", "Lightsaber Choreography Competition 2.5"),
    ("LCC03", "Lightsaber Choreography Contest III"),
    ("LCC04", "Lightsaber Choreography Competition IV"),
    ("LCC05", "Lightsaber Choreography Contest V"),
    ("LCC06", "Lightsaber Choreography Contest VI"),
    ("LCC07", "Lightsaber Choreography Contest VII"),
    ("LCC08", "Lightsaber Choreography Competition VIII"),
    ("LCC09", "Lightsaber Choreography Competition IX"),
    ("LCC10", "Lightsaber Choreography Competition X"),
    ("LCC11", "Lightsaber Choreography Contest XI"),
    ("LCC12", "Lightsaber Choreography Contest XII"),
    ("LCC2015", "Lightsaber Choreography Contest 2015"),
    ("LCC2016", "Lightsaber Choreography Competition 2016"),
    ("LCC2017", "Lightsaber Choreography Competition 2017"),
    ("LCC2018", "Lightsaber Choreography Competition 2018"),
    ("SC19", "SaberComp 2019"),
    ("SC20", "SaberComp 2020"),
    ("SC21", "SaberComp 2021"),
    ("SC22", "SaberComp 2022"),
    ("SC23", "SaberComp 2023"),
    ("SC24", "SaberComp 2024"),
)

COMP_YEARS = {
    "LCC01": 2002,
    "LCC02": 2004,
    "LCC03": 2004,
    "LCC04": 2005,
    "LCC05": 2007,
    "LCC06": 2008,
    "LCC07": 2009,
    "LCC08": 2010,
    "LCC09": 2011,
    "LCC10": 2012,
    "LCC11": 2013,
    "LCC12": 2014,
    "LCC2015": 2015,
    "LCC2016": 2016,
    "LCC2017": 2017,
    "LCC2018": 2018,
    "SC19": 2019,
    "SC20": 2020,
    "SC21": 2021,
    "SC22": 2022,
    "SC23": 2023,
    "SC24": 2024,
}

ENTRY_STATUS = [
    ("Pending", "Pending Review"),
    ("Accepted", "Accepted"),
    ("Rejected", "Rejected"),
    ("Disqualified", "Disqualified"),
    ("Withdrawn", "Withdrawn"),
    ("Live", "Live"),
]


# For "related videos" and other non-entries. We might need a separate model for this.
# Also need to look into how the YouTube API works; we might need to store the video ID instead of the full URL,
# and then use the API to get a bunch of the video's metadata.
CONTENT_TYPE = (
    ("LCC-SC", "Official Entry"),
    ("Special", "Special Edition"),
    ("Supp", "Supplemental"),
    ("Promo", "Official Promo"),
    ("Highlight", "Highlight Reel"),
    ("Other", "Other"),
)


class LCCComp(models.Model):
    name = models.CharField(choices=COMP_NAMES, max_length=200, unique=True)
    # year = models.IntegerField(editable=False)  # Automatically set, not editable
    # year = models.CharField(choices=COMP_YEARS, max_length=200, unique=True)
    year = models.IntegerField(default=2020)
    start_date = models.DateField(default="2020-05-04")
    open_submissions = models.DateField(default="2021-01-01")
    deadline = models.DateField(default="2021-01-31")
    # end_date = models.DateField(default="2020-12-31")
    theme = models.CharField(max_length=200, blank=True, null=True, default="")
    rules = models.TextField(default="No rules. (This is a default value)", max_length=2000)
    announcment_promo = models.URLField(blank=True, null=True, default="", max_length=200)
    live_judging = models.URLField(blank=True, null=True, default="", max_length=200)
    highlight_reel = models.URLField(blank=True, null=True, default="", max_length=200)
    
    def __str__(self):
        return self.get_name_display()
    
    class Meta:
        verbose_name = "LCC Competition"
        verbose_name_plural = "LCC Competitions"


# @receiver(pre_save, sender=LCCComp)
# def set_competition_year(sender, instance, **kwargs):
#     if instance.name in COMP_YEARS:
#         instance.year = COMP_YEARS[instance.name]


class LCCCreator(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "LCC Creator"
        verbose_name_plural = "LCC Creators"

    def get_entries(self):
        return LCCEntry.objects.filter(creator=self)

class LCCCompany(models.Model):
    company_name = models.CharField(max_length=200)
    company_url = models.URLField(max_length=200 , blank=True, null=True)
    owner = models.ForeignKey(LCCCreator, related_name="companies", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.company_name
    
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def get_entries(self):
        return LCCEntry.objects.filter(creator=self)

class CrewRole(models.Model):
    role = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.role
    
    class Meta:
        verbose_name = "Crew Role"
        verbose_name_plural = "Crew Roles"
    

class LCCEntry(models.Model):
    title = models.CharField(max_length=200, default="Untitled")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    status = models.CharField(max_length=200, choices=ENTRY_STATUS, default="Pending Review")
    content_type = models.CharField(max_length=200, choices=CONTENT_TYPE, default="LCC-SC")
    top_10 = models.BooleanField(default=False)
    youtube_link = models.URLField(max_length=200)
    competition_name = models.ForeignKey(LCCComp, to_field='name', related_name="entries_by_name", on_delete=models.CASCADE)
    creator = models.ForeignKey(LCCCreator, related_name="entries", on_delete=models.CASCADE)
    production_company = models.CharField(blank=True, null=True, max_length=200)
    company_new = models.ForeignKey(LCCCompany, related_name="entries", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_competition_name_display(self):
        return self.competition_name.get_name_display()
    
    class Meta:
        verbose_name = "LCC Entry"
        verbose_name_plural = "LCC Entries"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(LCCEntry, self).save(*args, **kwargs)
