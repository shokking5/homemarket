from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("set_payment/", hello.views.set_payment, name="set_payment"),
    path("get_backup/", hello.views.get_backup, name="get_backup"),
    path("get_orders/", hello.views.get_orders, name="get_orders"),
    path("remove_payment/", hello.views.remove_payment, name="remove_payment")
    # path("db/", hello.views.db, name="db"),
    # path("admin/", admin.site.urls),
]
