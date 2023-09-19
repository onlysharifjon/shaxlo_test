from django.db import models

# Create your models here.
class Admins(models.Model):
    name = models.CharField(max_length = 255, blank=True, null=True)
    surname = models.CharField(max_length = 255, blank=True, null=True)
    father_name = models.CharField(max_length = 255, blank=True, null=True)
    date_birth = models.DateTimeField(blank=True, null=True)
    job = models.CharField(max_length = 255, blank=True, null=True)
    cv = models.FileField(upload_to = 'cv_of_workers/', blank=True, null=True)
    time_job = models.CharField(max_length=50000, blank=True, null=True)
    place = models.CharField(max_length = 500000, blank=True, null=True)
    username = models.CharField(max_length = 500, blank=True, null=True)
    password = models.CharField(max_length = 500, blank=True, null=True)
    count_news = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length = 20, blank=True, null=True)
    job_category = models.CharField(max_length = 255, blank=True, null=True)

    def __str__(self):
        return self.name

    def formatted_date(self):
        return self.date_birth.strftime('%d-%m-%Y')


class News(models.Model):
    oz = 'ozbek'
    ru = 'rus'
    en = 'eng'
    uz = 'uz'
    
    Uzbekiston =  "O'zbekiston"
    Dunyo= 'Dunyo'
    Jamiyat= 'Jamiyat'
    Madaniyat= 'Madaniyat'
    Iqtisodiyot= 'Iqtisodiyot'
    Texno= 'Texno'
    Sport= 'Sport'
    Salomatlik= 'Salomatlik'
    
    Toshkent= "Toshkent"
    Navoiy= 'Navoiy'
    Buxoro= 'Buxoro'
    Samarqand= 'Samarqand'
    Xorazm= 'Xorazm'
    Nukus= 'Nukus'
    Qoraqalpog= "Qoraqalpog'iston"
    Jizzax= 'Jizzax'
    Sirdaryo= 'Sirdaryo'
    Surxonndaryo= 'Surxondaryo'
    Qashqadaryo= 'Qashqadaryo'
    Fargona= 'Fargona'
    Andijon= 'Andijon'
    Namangan= "Namangan"
    
    choise = [
        (oz, 'ozbek'),
        (ru, 'rus'),
        (en, 'eng'),
        (uz, 'uz'),
        ]
        
    CHOISE1=[
        (Uzbekiston, "O'zbekiston"),
        (Dunyo,'Dunyo'),
        (Jamiyat,'Jamiyat'),
        (Madaniyat,'Madaniyat'),
        (Iqtisodiyot,'Iqtisodiyot'),
        (Texno,'Texno'),
        (Sport,'Sport'),
        (Salomatlik,'Salomatlik'),
    ]
    CHOISE2=[
        (Toshkent, "Toshkent"),
        (Navoiy, 'Navoiy'),
        (Buxoro, 'Buxoro'),
        (Samarqand, 'Samarqand'),
        (Xorazm, 'Xorazm'),
        (Nukus, 'Nukus'),
        (Qoraqalpog, "Qoraqalpog'iston"),
        (Jizzax, 'Jizzax'),
        (Sirdaryo, 'Sirdaryo'),
        (Surxonndaryo, 'Surxondaryo'),
        (Qashqadaryo, 'Qashqadaryo'),
        (Fargona, 'Fargona'),
        (Andijon, 'Andijon' ),
        (Namangan, "Namangan" )
    ]
    title = models.CharField(max_length=255, blank=True, null=True)
    text = models.CharField(max_length=500000, blank=True, null=True)
    field = models.FileField(upload_to = 'fields/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now = True, blank=True, null=True)
    creted_by = models.ForeignKey(Admins, on_delete =models.CASCADE, blank=True, null=True)
    is_reclama = models.BooleanField(default = False, blank=True, null=True)
    place = models.CharField(choices = CHOISE2, max_length = 5000, blank=True, null=True)
    language = models.CharField(choices = choise, max_length = 255, blank = True, default = "ozbek")
    category = models.CharField(choices = CHOISE1, max_length = 5000, blank=True, null=True)

    def __str__(self):
        return  self.title
        
    # def get_field_url(self):
    #     if self.field:
    #         return f"https://taknews-backend.uz{self.field.url}"
    #     return None

