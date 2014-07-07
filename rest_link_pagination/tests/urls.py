from django.conf.urls import url

from rest_link_pagination.tests.views import none, generic


urlpatterns = (
    url("^none/list$",
        none.NoPaginationList.as_view(),
        name="none-list",
    ),

    url("^generic/list",
        generic.PaginatedList.as_view(),
        name="generic-list",
    )
)
