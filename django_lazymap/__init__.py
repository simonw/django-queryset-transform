from django.db import models

class LazyMapQuerySet(models.query.QuerySet):
    def __init__(self, *args, **kwargs):
        super(LazyMapQuerySet, self).__init__(*args, **kwargs)
        self._lazymap_fns = []
    
    def lazymap(self, fn):
        self._lazymap_fns.append(fn)
        return self
    
    def iterator(self):
        result_iter = super(LazyMapQuerySet, self).iterator()
        if self._lazymap_fns:
            results = list(result_iter)
            for fn in self._lazymap_fns:
                fn(results)
            return iter(results)
        return result_iter

class LazyMapManager(models.Manager):
    
    def get_query_set(self):
        return LazyMapQuerySet(self.model)
