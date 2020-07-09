import csv
import os

def string(name, description, **extra):
    return dict(name=name, description=description, type='string', **extra)

def get_schema(csv_name):
    properties = {}
    fpath = os.path.join('variable_dicts', csv_name+'.csv')
    with open(fpath, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in list(spamreader)[1:]:
            name, description, choices = row
            properties[name] = make_prop(name, description, choices)
    return {
        'type': 'object',
        'properties': properties,
    }

def make_prop(name, description, choices):
    bool_choices = [
        '"0" if there are no marks in the box, "1" if marks are present',
        '"0" if unchecked, "1" if checked',
    ]
    if choices in bool_choices or name == 'Signature':
        # These fields are a 1 or a zero, here represented as a boolean
        prop = dict(name=name, type='boolean')
        if not description.endswith('checked'):
            # Some fields have long redundant descriptions, not sure if we should keep these
            prop['description'] = description
        return prop
    if name.startswith('Date_') or name.startswith('DOB_'):
        # this is a date fragment ala __/__/__
        return string(name, description)
    if "If YES, why?" in description:
        return string(name, description)
    if '(free text)' in description:
        return string(name, description)
    if 'Yes,No' == choices.replace(' ', '').replace('"',''):
        # answer is yes or no checkbox, stored as string not boolean
        return string(name, description, choices=["Yes", "No"])
    if name in ['UniqueID', 'SEP', 'Age', 'Date', 'Staff']:
        # other misc text fields
        return string(name, description)

    # if none of the above, it's one of several multi-choice fields
    if name in ['Witness_times', 'Witness_recent', 'Trained', 'Medication']:
        return dict(
            description=description,
            name=name,
            type= 'string',
            choices= choices.replace('"', '').replace(', ',',').split(','),
        )
    e = f'Cannot find schema for field\nname="{name}"\ndescription="{description}"\nchoices="{choices}"'
    raise ValueError(e)

form_list = [f for f in os.listdir('variable_dicts') if f.endswith('.csv')]
form_map = {}

for fname in form_list:
    title = slug = fname.rstrip('.csv')
    title = title.replace('Dictionary','')
    entry = {}
    for i, letter in list(enumerate(slug))[::-1]:
        if letter != letter.lower():
            title = title[:i] + " " + title[i:]
    entry['title'] = title
    entry['slug'] = slug
    entry['schema'] = get_schema(slug)
    form_map[slug] = entry