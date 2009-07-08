#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.defaults import (patterns, include, handler404,
                                       handler500, url)
from django.contrib import admin
from django.utils import translation
from django.utils.translation import ugettext as _

admin.autodiscover()

handler404
handler500

# Switch language temporarily for "static" I18n of URLs
language_for_urls = settings.LANGUAGE_CODE[:2]
language_saved = translation.get_language()
translation.activate(language_for_urls)

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),

    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^(?P<path>favicon\.ico)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )

# Switch back to the language of choice
translation.activate(language_saved)
