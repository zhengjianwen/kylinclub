
from django.conf.urls import url,include
from kingadmin.views import authuser, index, news, menu

urlpatterns = [
    url(r'login.html$', authuser.Login.as_view()),
    url(r'logout.html$', authuser.Logout.as_view()),
    url(r'index.html$', index.Index.as_view()),
    url(r'news/$', news.News.as_view()),
    url(r'news/add/', news.Newsadd.as_view()),
    url(r'menus/', menu.MenuView.as_view()),
    url(r'activitytype/', menu.Activitytype.as_view()),
    url(r'activity/add$', menu.Activityadd.as_view()),
    url(r'activity.html', menu.ActivityView.as_view()),
    url(r'', index.Index.as_view()),

]
