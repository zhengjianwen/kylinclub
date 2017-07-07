
from django.conf.urls import url,include
from kingadmin.views import authuser, index, news, menu
from kingadmin.views import upload


urlpatterns = [
    url(r'login.html$', authuser.Login.as_view()),
    url(r'logout.html$', authuser.Logout.as_view()),
    url(r'index.html$', index.Index.as_view()),
    url(r'news/$', news.NewsView.as_view()),
    url(r'news/add', news.Newsadd.as_view()),
    url(r'news/edit/(?P<cid>\d+)', news.NewsEdit.as_view()),
    url(r'news/delete/(?P<cid>\d+)', news.delete_new),
    url(r'news/status/(?P<cid>\d+)', news.status_new),

    url(r'menus/status/(?P<cid>\d+)', menu.MenuView.as_view()),
    url(r'menus/edit/(?P<cid>\d+)', menu.MenuEdit.as_view()),
    url(r'menus', menu.MenuView.as_view()),
    url(r'activitytype/add', menu.Activitytypeadd.as_view()),
    url(r'activitytype/edit/(?P<cid>\d+)', menu.Activitytypeedit.as_view()),
    url(r'^activitytype/', menu.Activitytype.as_view()),
    url(r'activity.html', menu.ActivityView.as_view()),
    url(r'^activity/add', menu.Activityadd.as_view()),

    url(r'uplode_pic.html', upload.upload_kindeditor_img),
    url(r'', index.Index.as_view()),

]
