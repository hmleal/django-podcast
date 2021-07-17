from django.db import models


class ItemQuerySet(models.QuerySet):
    def draft(self):
        return self.filter(status=1)

    def public(self):
        return self.filter(status=2)

    def private(self):
        return self.filter(status=3)
