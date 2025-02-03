from django.db import models

# Create your models here.

    
class Home(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class Offer(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    content = models.TextField()
    url = models.URLField(default='https://wa.me/201067343755')

    def __str__(self):
        return self.title
    

class About(models.Model):
    title = models.CharField(max_length=200 , default='ماذا عنا')
    intro_content = models.TextField()   
    main_content = models.TextField()   
    img = models.ImageField(upload_to='about/', verbose_name="about")

    office = models.DecimalField(max_digits=10, decimal_places=2, default=0) 
    users = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    projects = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    workers = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.title

    

class ContactUs(models.Model):
    facebook = models.URLField(default='https://www.facebook.com/ebda3design')
    instgram = models.URLField(default='https://www.instagram.com/ebda3design')
    location = models.CharField(max_length=200, default='شارع الغشام, Zagazig, Egypt')
    title = models.CharField(max_length=200)
    email = models.EmailField(default='ebda3design2@gmail.com')
    whatsapp_number = models.CharField(default='https://wa.me/201067343755', max_length=200)
    location_url = models.URLField(blank=True, null=True)  # رابط الموقع على الخريطة
    

    def save(self, *args, **kwargs):
        # لو مش متحدد الرابط، هنعمل له generate من العنوان المدخل
        if not self.location_url:
            self.location_url = f"https://www.google.com/maps?q={self.location}"
        super().save(*args, **kwargs)

    
    def __str__(self):
        return self.title
    

class BusinessGallery(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/', verbose_name="gallery")

    def __str__(self):
        return self.title