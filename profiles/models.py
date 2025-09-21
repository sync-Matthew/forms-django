from django.db import models
import uuid

class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.UUIDField(editable=False)
    realm_id = models.UUIDField(editable=False)
    realm = models.CharField(editable=False, max_length=255)
    user_token = models.CharField(max_length=255)
    # Audit fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user_id', 'realm_id')
