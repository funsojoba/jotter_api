import uuid
from django.db import models
from authentication.models import User



class Jotter(models.Model):
    
    EVENT_TYPE = (
        ('Good', 'Good'),
        ('Bad', 'Bad'),
        ('Neutral', 'Neutral')
    )
    
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    event_date = models.DateField()
    event_type = models.CharField(choices=EVENT_TYPE, max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    