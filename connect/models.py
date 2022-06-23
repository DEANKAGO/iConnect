from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver

gender_choices = (
    ("male", "male"),
    ("female", "female"),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username  = models.CharField(max_length=60)
    profile_photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    ethnicity = models.CharField(max_length=30, null=True, blank=True)
    gender = models.CharField(choices=gender_choices, max_length=30, null=True, blank=True)
    location = models.CharField(max_length=30, null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    preference = models.TextField(max_length=500, blank=True, null=True)
    catfish = models.ManyToManyField(User, related_name='catfish', blank=True)
    phone_number = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ["-pk"]

    def get_absolute_url(self):
        return f"/profile/{self.id}"

    # def get_absolute_url(self):
    #     from django.core.urlresolvers import reverse
    #     return reverse('user.views.profileCatfishToggle', args=[str(self.id)])

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

    def total_catfish(self):
        return self.catfish.count()

    def __str__(self):
        return f'{self.user.username} profile'

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()



class Like(models.Model):
    created_on = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


# class Catfish(models.Model):
#     created_on = models.DateField(auto_now_add=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver',on_delete=models.CASCADE)
    text = models.TextField(max_length=500, null=False, blank=False)
    created_on = models.DateField(auto_now_add=True)
