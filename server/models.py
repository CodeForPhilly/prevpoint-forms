from django.db import models
import json

# Using this instead of the postgres field for now since I'm using sqllite as the database
# TODO switch to django.contrib.postgres.fields.JSONField
class JSONField(models.Field):
    def db_type(self, connection):
        return 'text'

    def from_db_value(self, value, expression, connection):
        if value is not None:
            return self.to_python(value)
        return value

    def to_python(self, value):
        if value is not None:
            try:
                return json.loads(value)
            except (TypeError, ValueError):
                return value
        return value

    def get_prep_value(self, value):
        if value is not None:
            return str(json.dumps(value))
        return value

    def value_to_string(self, obj):
        return self.value_from_object(obj)

class FormCompletion(models.Model):
    STATUS_CHOICES = [
        ['new', 'new'],
        ['processing', 'processing'],
        ['needs_verify', 'needs_verify'],
        ['verified', 'verified'],
        ['error', 'error'],
    ]
    status = models.CharField(max_length=16, choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    form_type = models.CharField(max_length=16)
    image = models.ImageField(upload_to="forms")
    data = JSONField(default={})
    def process(self):
        # TODO this needs to set off a task in celery or some other queue
        # at very least it should be started in a sub process to kick it off to another thread
        if self.status == 'processing':
            return

        self.status = 'processing'
        self.save()

        # TODO actual process stuff here

        # TODO this would be in a separate post processing step
        # self.data = process_form_image(self.form_type, self.image)
        self.status = 'needs_verify'
        self.save()