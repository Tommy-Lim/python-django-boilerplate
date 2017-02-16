urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^new/$', views.create, name="create"),
    url(r'^(?P<boardgame_id>[0-9]+)/$', views.details, name="details"),
    url(r'^(?P<boardgame_id>[0-9]+)/edit$', views.edit, name="edit")
]
