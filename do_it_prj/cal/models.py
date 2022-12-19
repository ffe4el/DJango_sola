from django.db import models
from django.urls import reverse
import datetime as dt

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        self.start_time = self.start_time.strftime('%H:%M')
        self.end_time = self.end_time.strftime('%H:%M')
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}">{self.start_time} ~ {self.end_time} &nbsp;&nbsp; {self.title} </a>'
