class LinkPaginationMixin(object):

    def paginate_queryset(self, *args, **kwargs):
        page = super(LinkPaginationMixin, self).paginate_queryset(*args, **kwargs)

        if page is not None:
            page_serializer = self.get_pagination_serializer(page)

            link_template = '<%(link)s>; rel="%(rel)s"'
            links = []

            self.object_list = page.object_list

            links_map = (
                ("next", "next"),
                ("previous", "prev"),
                ("first", "first"),
                ("last", "last"),
            )

            for original, new in links_map:
                if original in page_serializer.data \
                        and page_serializer.data[original]:
                    link = link_template % {
                        "rel": new,
                        "link": page_serializer.data[original],
                    }

                    links.append(link)

            if links:
                self.headers["Link"] = ",".join(links)

        return None
