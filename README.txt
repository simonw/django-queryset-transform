django_queryset_transform
=========================

Allows you to register a transforming map function with a Django QuerySet 
that will be executed only when the QuerySet itself has been evaluated.

This allows you to build optimisations like "fetch all tags for these 10 rows"
while still benefiting from Django's lazy QuerySet evaluation.

For example:
    
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
    
    qs = Item.objects.filter(name__contains = 'e').transform(lookup_tags)
    
    for item in qs:
        print item, item.fetched_tags

Prints:

    Winter comes to Ogglesbrook [<sledging>, <snow>, <winter>, <skating>]
    Summer now [<skating>, <sunny>]

But only executes two SQL queries - one to fetch the items, and one to fetch ALL of the tags for those items.

Since the transformer function can transform an evaluated QuerySet, it 
doesn't need to make extra database calls at all - it should work for things 
like looking up additional data from a cache.multi_get() as well.

Originally inspired by http://github.com/lilspikey/django-batch-select/
