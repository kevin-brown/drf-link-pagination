class FakeQueryset(object):
    queryset = []

    def get_queryset(self):
        return [
            {
                "id": 1,
                "name": "example",
            },
            {
                "id": 2,
                "name": "test",
            },
            {
                "id": 3,
                "name": "other",
            },
        ]
