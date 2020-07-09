# adapted from https://github.com/Cahersan/django-schemulator
from importlib import import_module

from django import forms

# Dictionaries for django form fields to json schema toolkit fields translation
# {FORM : JSON_SCHEMA}

KEYWORDS = {
    #Base keywords
    "label":"title",
    "help_text":"description",
    "initial":"default",
    "required":"optional",
    #String type-specific keywords
    "max_length":"maxLength",
    "min_length":"minLength",
    #Numerical type-specific keywords
    "min_value":"minimum",
    "max_value":"maximum",
    #Choice-specific keyword
    "choices":"enum",
}

TYPES = {
    'boolean':'BooleanField',
    'integer':'IntegerField',
    'number':'FloatField',
    'string':'CharField'
}

FORMATS = {
    'date-time':'DateTimeField',
    'email':'EmailField',
    'ipv4':'GenericIPAddressField',
    'ipv6':'GenericIPAddressField',
}

def schema_to_field(schema):
    """
    Returns a Django Forms field when given a schema fragment describing a
    field: that is, any entry of the 'properties' keyword
    """

    # This block sets the value of relevant field keyword arguments

    kwargs = {}

    for (field_kw, jschema_kw) in KEYWORDS.items():
        if jschema_kw in schema:
            value = schema[jschema_kw]
            if jschema_kw == "optional":
                value = not value
            kwargs[field_kw]=value

    # This block decides upon which form field should be used. This can be
    # explicitly specified in a JSON schema via the '__django_form_field_cls'
    # keyword

    if '__django_form_field_cls' in schema:
        field_type = schema['__django_form_field_cls']
    elif 'enum' in schema:
        field_type = 'ChoiceField'
    elif 'format' in schema and schema['type'] == 'string':
        field_type = FORMATS[schema['format']]
        # Special case for ipv6
        if schema['format'] == 'ipv6': kwargs['protocol']='ipv6'
    else:
        field_type = TYPES[schema['type']]

    if '__widget' in schema:
        mod = import_module('django.forms.widgets', schema['__widget'])
        widget = getattr(mod, schema['__widget'])()
        kwargs['widget'] = widget

    mod = import_module('django.forms', field_type)
    form_field = getattr(mod, field_type)
    field = form_field(**kwargs)

    return field


def schema_to_form(schema, *args, **kwargs):
    form = forms.Form(*args, **kwargs)

    for (name, prop) in schema['properties'].items():

        field = schema_to_field(prop)
        form.fields[name] = field

    return form

