import random
import string
from django.utils.text import slugify
# from testapp.models import Reqdata


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    
    import ipdb; ipdb.set_trace()
    slug_str = ''
    for req in instance.Requesttype.all():
        slug_str += '-'+req.typ
    slug = slugify(slug_str)
    
    Reqdata = instance.__class__
    qs_exists = Reqdata.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
    
   