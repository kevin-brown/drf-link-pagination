class LinkPaginationMixin(object):

    def paginate_queryset(self, *args, **kwargs):
        page = super(LinkPaginationMixin, self).paginate_queryset(*args, **kwargs)

        if page is not None:
            page_serializer = self.get_pagination_serializer(page)

            link_template = '<%(link)s>; rel="%(rel)s"'
            links = []

            self.object_list = page.object_list

            links_attributes = ("first", "next", "previous", "last", )

            for attribute in links_attributes:
                if attribute in page_serializer.data \
                        and page_serializer.data[attribute]:
                    link = link_template % {
                        "rel": attribute,
                        "link": page_serializer.data[attribute],
                    }

                    links.append(link)

            if links:
                self.headers["Link"] = ",".join(links)

        return None
