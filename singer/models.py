from django.db import models

# Create your models here.

class Song(models.Model):
	SID = models.AutoField(primary_key = True)
	SName = models.CharField(max_length = 100)
	Language = models.CharField(max_length = 100)
	Composer = models.CharField(max_length = 100)
	Tonality = models.CharField(max_length = 100)
	Verion = models.CharField(max_length = 100)
	def __str__(self):
		return self.SName

class Style(models.Model):
	SID = models.AutoField(primary_key = True)
	SName = models.CharField(max_length = 100)
	def __str__(self):
		return self.SName

class Performance(models.Model):
	PID = models.AutoField(primary_key = True)
	PName = models.CharField(max_length = 100)
	Date = models.CharField(max_length = 100)
	Company = models.CharField(max_length = 100)
	Venue = models.CharField(max_length = 100)
	Equipment = models.CharField(max_length = 100)
	def __str__(self):
		return self.PName

class Vocalist(models.Model):
	VID = models.AutoField(primary_key = True)
	VName = models.CharField(max_length = 100)
	Gender = models.CharField(max_length = 100)
	Vocal_Range = models.CharField(max_length = 100)
	Vocal_Type = models.CharField(max_length = 100)
	Language = models.CharField(max_length = 100)
	Music_Training = models.CharField(max_length = 100)
	def __str__(self):
		return self.VName

class Instrumentalist(models.Model):
	IID = models.AutoField(primary_key = True)
	IName = models.CharField(max_length = 100)
	Gender = models.CharField(max_length = 100)
	Instrument = models.CharField(max_length = 100)
	Music_Training = models.CharField(max_length = 100)
	def __str__(self):
		return self.IName