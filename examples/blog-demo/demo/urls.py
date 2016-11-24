from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

# Note: the third pattern redirect the empty path
# to the blog list. The syntax is a cumbersome.

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
    url(r'^$', RedirectView.as_view(url='/blog/'))
]
