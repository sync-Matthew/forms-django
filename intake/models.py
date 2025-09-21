from django.db import models

class TimeStampedModel(models.Model):
    """Created/updated timestamps."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Form(TimeStampedModel):
    user_id = models.UUIDField(editable=False) # Stateless JWT user ID - tied to account microservice
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Section(TimeStampedModel):
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name="sections")
    title = models.CharField(max_length=255, blank=True)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f"{self.form.title} - {self.title or 'Untitled Section'}"
    

class Row(TimeStampedModel):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="rows")
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f"Row {self.position} in {self.section}"
    

class Field(TimeStampedModel):
    quickbase_id = models.PositiveIntegerField()
    row = models.ForeignKey(Row, on_delete=models.CASCADE, related_name="fields")
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f"Field {self.quickbase_id} in {self.row}"
