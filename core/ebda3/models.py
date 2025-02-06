from django.db import models
from datetime import datetime
from django.utils import timezone
import os


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
    offer_link = models.URLField(default='https://drive.google.com/file/d/1P_UBPWF6hiK5M_Jqd4D5LHFD6Tq_X8RG/view')

    def __str__(self):
        return self.title
    

class About(models.Model):
    title = models.CharField(max_length=200 , default='ماذا عنا')
    intro_content = models.TextField(default='هي واحدة من الشركات الرائدة في مجال التشطيبات والديكورات، حيث نقدم حلول تصميم هندسية مبتكرة ومتخصصة للمساحات الداخلية والخارجية. نحن نسعى جاهدين لتحقيق أعلى معايير الجودة في جميع مشاريعنا، مع التركيز على الابتكار والإبداع في كل تفصيلة. بالإضافة إلى ذلك، نقدم خدمات المقاولات العامة ملتزمين بتوفير بيئات عمل عملية وجميلة تلبي جميع احتياجات عملائنا وتتفوق على توقعاتهم.')   
    main_content = models.TextField(default='في شركة إبداع للتصميم، نفخر بإنجاز أكثر من خمسين مشروعًا بنجاح في مجالات التشطيبات والديكورات. نحن نلتزم بتقديم حلول تصميم مبتكرة تلبي احتياجات عملائنا وتتفوق على توقعاتهم، مع ضمان أعلى مستويات الجودة والاحترافية في كل مشروع.')   
    img = models.ImageField(upload_to='about/', verbose_name="about", blank=True)
    project_count = models.CharField(max_length=200, default='خمسين')

    office = models.IntegerField(default=1) 
    users = models.IntegerField(default=24)
    projects = models.IntegerField(default=13)
    workers = models.IntegerField(default=20)
    def __str__(self):
        return self.title

    

class ContactUs(models.Model):
    facebook = models.URLField(default='https://www.facebook.com/profile.php?id=100086633168247')
    instgram = models.URLField(default='https://www.instagram.com/ebda3designegy/')
    location = models.CharField(max_length=200, default='شارع الغشام, Zagazig, Egypt')
    title = models.CharField(default='ماذا عنا', max_length=200) 
    email = models.EmailField(default='ebda3design2@gmail.com')
    whatsapp_number = models.CharField(default='https://wa.me/201067343755', max_length=200)
    phone_number = models.CharField(default='01067343755', max_length=200)
    location_url = models.URLField(default='https://maps.app.goo.gl/XzVRa8YikcjNSJ3Y7' , blank=True, null=True)  # رابط الموقع على الخريطة
    

    def save(self, *args, **kwargs):
        # لو مش متحدد الرابط، هنعمل له generate من العنوان المدخل
        if not self.location_url:
            self.location_url = f"https://www.google.com/maps?q={self.location}"
        super().save(*args, **kwargs)

    
    def __str__(self):
        return self.title
    




class BusinessGallery(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='gallery/', verbose_name="gallery")
    created_at = models.DateTimeField(auto_now_add=True)  # حفظ وقت الإضافة تلقائيًا

    def save(self, *args, **kwargs):
        if not self.title and self.created_at:
            # توليد العنوان بناءً على الوقت الذي تم رفع الصورة فيه
            self.title = f"Image_{self.created_at.strftime('%Y%m%d_%H%M%S')}"

        super().save(*args, **kwargs)  # حفظ الصورة الجديدة أولًا

        # الاحتفاظ فقط بآخر 50 صورة وحذف الأقدم
        images = BusinessGallery.objects.order_by('-created_at')  # ترتيب تنازلي حسب الأحدث
        if images.count() > 50:
            old_images = images[50:]  # تحديد الصور الزائدة
            for img in old_images:
                if img.image:  # حذف الملف الفعلي من الميديا
                    if os.path.exists(img.image.path):
                        os.remove(img.image.path)
                img.delete()  # حذف السجل من قاعدة البيانات

    def __str__(self):
        return self.title