from django.db import models

class News(models.Model):

    CATEGORY_CHOICES = [
        ('sport', 'Sport'),
        ('tech', 'Texnologiya'),
        ('politics', 'Siyasat'),
        ('education', 'Bilim'),
    ]

    title = models.CharField(max_length=200)

    image = models.ImageField(
        upload_to='news/',
        null=True,
        blank=True
    )

    author = models.CharField(max_length=100, default="Admin")

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='tech'
    )

    content = models.TextField()
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title