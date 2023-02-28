from django.db import models
from django.urls import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Artist(models.Model):

    first_name = models.CharField(max_length=30, help_text='Enter the first name of artist.')
    middle_name = models.CharField(max_length=30, help_text='Enter the middle name of artist.')
    last_name = models.CharField(max_length=30, help_text='Enter the last name of artist.')
    name = models.CharField(max_length=30, help_text='Enter the professional name of artist.', primary_key=True)
    date_of_birth = models.DateField(help_text='Enter date of birth of artist.')
    photo = ProcessedImageField(upload_to='artists',
                                processors=[ResizeToFill(800, 800)],
                                format='JPEG',
                                options={'quality': 100})

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('artist-detail', args=[str(self.name), 1])

    def full_name(self):
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name

    def __str__(self):
        return self.name



class Album(models.Model):

    name = models.CharField(max_length=50, help_text='Enter the name of album.', primary_key=True)
    artist = models.ForeignKey(Artist, help_text='Select artist of the album.', on_delete=models.CASCADE)
    release_date = models.DateField(help_text='Enter release date of the album.')
    cover = ProcessedImageField(upload_to='albums',
                                processors=[ResizeToFill(800, 800)],
                                format='JPEG',
                                options={'quality': 100})

    class Meta:
        ordering = ['release_date', 'name', 'artist']

    def get_absolute_url(self):
        return reverse('album-detail', args=[str(self.name), 1])

    def __str__(self):
        return self.name



class Chart(models.Model):

    name = models.CharField(max_length=50, help_text='Enter name of the music chart.', primary_key=True)
    country = models.CharField(max_length=50, help_text='Enter the country which the chart belongs to.')
    flag = models.ImageField(upload_to='flags')

    class Meta:
        ordering = ['name']
    
    def get_absolute_url(self):
        return reverse('charts')

    def __str__(self):
        return self.name



class Position(models.Model):

    album = models.ForeignKey(Album, help_text='Select the album.', on_delete=models.CASCADE)
    chart = models.ForeignKey(Chart, help_text='Select a music chart.', on_delete=models.CASCADE)
    peak_position = models.IntegerField(default=0, help_text='Enter the peak position charted by the album.')
    weeks_on_chart = models.IntegerField(default=0, help_text='Enter the number of the weeks album appeared on the chart.')

    class Meta:
        ordering = ['chart', 'peak_position', 'weeks_on_chart']

    def __str__(self):
        return f'{self.album} - {self.chart} ({self.weeks_on_chart})'
