from django.db import models

class TransformQuerySet(models.query.QuerySet):
    def __init__(self, *args, **kwargs):
        super(TransformQuerySet, self).__init__(*args, **kwargs)
        self._transform_fns = []
    
    def transform(self, fn):
        self._transform_fns.append(fn)
        return self
    
    def iterator(self):
        result_iter = super(TransformQuerySet, self).iterator()
        if self._transform_fns:
            results = list(result_iter)
            for fn in self._transform_fns:
                fn(results)
            return iter(results)
        return result_iter

class TransformManager(models.Manager):
    
    def get_query_set(self):
        return TransformQuerySet(self.model)
