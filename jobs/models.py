from django.db import models


class Job(models.Model):
    STATUS_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    RESPONSE_CHOICES = (
        ('No response', 'No response'),
        ('In-progress', 'In-progress'),
        ('Accepted', 'Accepted'),
        ('Declined', 'Declined')
    )
    company_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    cv = models.CharField(max_length=5, choices=STATUS_CHOICES, default='No')
    cover_letter = models.CharField(max_length=5, choices=STATUS_CHOICES, default='No', blank=True)
    response = models.CharField(max_length=15, null=True, choices=RESPONSE_CHOICES, default='No response')
    date_applied = models.DateField(null=True)
    followup1 = models.DateField(blank=True, null=True)
    followup2 = models.DateField(blank=True, null=True)
    followup3 = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.company_name


class Contact(models.Model):
    job = models.OneToOneField(Job, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    phone_no = models.CharField(max_length=11, blank=True)
    email = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return self.name
