from django.db import models

# Create your models here.


class tweet(models.Model):
    date = models.DateField()
    influencer = models.CharField(max_length=50)
    tweeturl = models.URLField()
    subject = models.CharField(max_length=50)
    retweets = models.IntegerField()
    likes = models.IntegerField()
    views = models.IntegerField()
    sentiment = models.CharField(max_length=30)
    quote = models.TextField()

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.tweeturl

class tweettable(models.Model):
    tweets = models.ForeignKey(tweet, on_delete=models.CASCADE)