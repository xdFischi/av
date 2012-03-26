from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
import notification.models

notification_models = ('NoticeType', 'NoticeSetting', 'Notice',
    'NoticeQueueBatch', 'ObservedItem')
notification_models = map(lambda x: getattr(notification.models, x),
    notification_models)
admin.site.unregister(notification_models)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('rcal_registration.urls')),
#    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^', include('rcal.urls')),
)
