from itertools import chain
from django.db.models import ForeignKey


def model_to_dict(instance, fields=None, exclude=None):
    opts = instance._meta
    data = {}
    for f in chain(opts.concrete_fields, opts.private_fields, opts.many_to_many):
        if not getattr(f, "editable", False):
            continue
        if fields is not None and f.name not in fields:
            continue
        if exclude and f.name in exclude:
            continue

        # Если поле является ForeignKey, добавляем приписку _id к имени поля
        if isinstance(f, ForeignKey):
            field_name = f.name + '_id'
        else:
            field_name = f.name

        data[field_name] = f.value_from_object(instance)

    return data