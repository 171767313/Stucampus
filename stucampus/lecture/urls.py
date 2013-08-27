from django.conf.urls import url, patterns
from stucampus.lecture.views import index, manage, submit
from stucampus.lecture.views import delete, update, add_new


urlpatterns = patterns(
    '',
    url(r'^$', index, name='index'),
    url(r'^manage/$', manage, name='manage'),
    url(r'^submit/$', submit, name='submit'),
    url(r'^update/$', update, name='update'),
    url(r'^delete/$', delete, name='delete'),
    url(r'^add_new/$', add_new, name='add_new'),
)
