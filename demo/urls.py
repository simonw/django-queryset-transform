from django.conf.urls.defaults import *
from django.contrib import admin
from django.http import HttpResponse
from django.db import connection

from demo_models.models import Item, Tag

from pprint import pformat

admin.autodiscover()

def example(request):
    def lookup_tags(item_qs):
        item_pks = [item.pk for item in item_qs]
        m2mfield = Item._meta.get_field_by_name('tags')[0]
        tags_for_item = Tag.objects.filter(
            item__in = item_pks
        ).extra(select = {
            'item_id': '%s.%s' % (
                m2mfield.m2m_db_table(), m2mfield.m2m_column_name()
            )
        })
        tag_dict = {}
        for tag in tags_for_item:
            tag_dict.setdefault(tag.item_id, []).append(tag)
        for item in item_qs:
            item.fetched_tags = tag_dict.get(item.pk, [])
    
    qs = Item.objects.all().transform(lookup_tags)
    
    s = []
    
    for item in qs:
        s.append('%s: %s' % (item, [t.name for t in item.fetched_tags]))
    
    return HttpResponse(
        '<br>'.join(s) + '<pre>%s</body></html>' % pformat(connection.queries)
    )

urlpatterns = patterns('',
    (r'^$', example),
    (r'^admin/', include(admin.site.urls)),
)
