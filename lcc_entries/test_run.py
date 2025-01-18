from django.db import models
from lcc_entries.models import LCCComp

comps = [
    "LCC01",
    "LCC02",
    "LCC03",
    "LCC04",
    "LCC05",
    "LCC06",
    "LCC07",
    "LCC08",
    "LCC09",
    "LCC10",
    "LCC11",
    "LCC12",
    "LCC2015",
    "LCC2016",
    "LCC2017",
    "LCC2018",
    "SC19",
    "SC20",
    "SC21",
    "SC22",
    "SC23",
    "SC24",
]

for comp in comps:
    LCCComp.objects.create(name=comp, year=comp)