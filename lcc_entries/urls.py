from django.urls import path

from . import views

app_name = "lcc_entries"
urlpatterns = [
    path("", views.index, name="index"),                                    # "index" is a custom name for this URL pattern
    path("search/", views.search, name="search"),                           # "search" is a custom name for this URL pattern
    path("about/", views.about, name="about"),                              # "about" is a custom name for this URL pattern     
    path("<str:comp_name>/", views.comp, name="comp"),                      # "comp" is a custom name for this URL pattern, "comp_name" is a URL parameter.
                                                                            # I think whatever is in place of "<str:comp_name>" will be passed to the view function as an argument, referred to elsewhere as "comp_name" 
    path("<str:comp_name>/<str:slug>/", views.entry, name="entry"),         # "entry" is a custom name for this URL pattern, "slug" is a URL parameter
    path("creator/<str:creator_name>/", views.creator, name="creator"),     # "creator" is a custom name for this URL pattern, "creator_name" is a URL parameter

]