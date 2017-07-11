from django.conf.urls import url,include
from kingadmin.views import authuser, index, news, menu, message,carousel,company
from kingadmin.views import upload, sendmail


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
    url(r'menus/add', menu.MenuAdd.as_view()),
    url(r'menus', menu.MenuView.as_view()),

    url(r'activitytype/add', menu.Activitytypeadd.as_view()),
    url(r'activitytype/edit/(?P<cid>\d+)', menu.Activitytypeedit.as_view()),
    url(r'activitytype/', menu.Activitytype.as_view()),

    url(r'activity.html', menu.ActivityView.as_view()),
    url(r'activity/add', menu.Activityadd.as_view()),
    url(r'activity/edit/(?P<cid>\d+)', menu.Activityedit.as_view()),

    url(r'mailset/add', message.EmailAdd.as_view()),
    url(r'mailset/edit/(?P<cid>\d+)', message.EmailEdit.as_view()),
    url(r'mailset/delete/(?P<cid>\d+)', message.maildelete),
    url(r'mailset', message.EmailView.as_view()),

    url(r'lunbo/add', carousel.CarouseAdd.as_view()),
    url(r'lunbo/edit/(?P<cid>\d+)', carousel.CarouseEdit.as_view()),
    url(r'lunbo/delete/(?P<cid>\d+)', carousel.carousedelete),
    url(r'lunbo', carousel.CarouseView.as_view()),

    url(r'maillog', message.maillog),
    url(r'mailmb/add', message.EmailTmplatAdd.as_view()),
    url(r'mailmb/edit/(?P<cid>\d+)', message.EmailTmplatEdit.as_view()),
    url(r'mailmb/status/(?P<cid>\d+)', message.emailtmplatstatus),
    url(r'mailmb', message.EmailTmplatView.as_view()),

    url(r'company', company.CompanyMemberView.as_view()),


    url(r'follow$', company.follow),
    url(r'huiyuan/status$', company.companystatus),

    url(r'uplode_pic.html', upload.upload_kindeditor_img),
    url(r'mail.html', sendmail.sendmail),
    url(r'', index.Index.as_view()),

]
