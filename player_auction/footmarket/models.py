from django.db import models

class player(models.Model):
     player_name=models.CharField(max_length=30)
     current_club=models.CharField(max_length=30)
     position=models.CharField(max_length=10)
     market_value=models.CharField(max_length=10)
     