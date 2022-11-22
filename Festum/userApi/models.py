from pyexpat import model
from django.db import models
from django.conf import settings
from django.db.models.fields import BigIntegerField
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from sqlalchemy import null

# from sqlalchemy import null, true
from userApi.utils import generate_ref_code, TicketNum

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MinLengthValidator

from PIL import Image
from io import BytesIO
from django.core.files import File


def compress(image):
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, 'png', quality=60)
    new_image = File(im_io, name=image.name)
    return new_image


class MyUserManager(BaseUserManager):
    def create_user(self, email, name, password=None, password2=None):
        if not email:
            raise ValueError("Users must have an email address.")
        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, name):
        user = self.create_user(
            email=self.normalize_email(email),
            name=name,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


def get_profile_image_filepath(self, filename):
    return f'profile_img/{self.pk}/{"profile_img.png"}'


def get_default_profile_img():
    return "../static/media/images.png"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class User(AbstractBaseUser):
    userId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    email = models.EmailField(verbose_name='email',
                              max_length=250, unique=True)
    phone_no = models.CharField(
        max_length=15, unique=True, null=True, blank=True)
    date = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    refer_code = models.CharField(max_length=8, null=True, blank=True)
    users_ref_code = models.CharField(max_length=8, blank=True, unique=True)
    profile_img = models.ImageField(max_length=255, upload_to=get_profile_image_filepath,
                                    default=get_default_profile_img)
    otp = models.CharField(max_length=4, blank=True, unique=True, null=True)
    coins = models.CharField(max_length=11, default=0)
    user_type_data = ((0, 'superadmin'), (1, 'admin'), (2, 'subadmin'),
                      (3, 'executive'), (4, 'organizer'), (5, 'user'))
    user_type = models.CharField(
        max_length=250, default=5, choices=user_type_data)

    objects = MyUserManager()
    ordering = ('email')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

# image

    def get_profile_image_filename(self):
        return str(self.profile_img)[str(self.profile_img).index(f'profile_img/{self.pk}/'):]

# refer code generator

    def save(self, *args, **kwargs):
        if self.users_ref_code == "":
            code_ = generate_ref_code()
            self.users_ref_code = code_
        super().save(*args, **kwargs)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_Label):
        return True


class OtpLog(models.Model):
    mobile = models.CharField(max_length=15)
    otp = models.CharField(max_length=10, null=True, blank=True)
    is_verify = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)


# email for otp
class Emails(models.Model):
    email = models.EmailField(max_length=250)

    def __all__(self):
        return self.email


class Transactions(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, related_name="Transactions", on_delete=models.CASCADE)
    img = models.TextField(
        max_length=5000, null=True)
    translation_type = models.CharField(max_length=255)
    details = models.CharField(max_length=255)
    Amount = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)


class RedeemCoins(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, related_name="RedeemCoins", on_delete=models.CASCADE)
    Amount = models.CharField(max_length=50, null=True)
    upi_id = models.TextField(max_length=1000, null=True)
    price = models.FloatField(max_length=50, null=True)
    date = models.DateTimeField(auto_now_add=True)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Event


def nullStr(statements):
    if statements != None:
        statements = str(statements)

    if statements and not statements.isspace():
        return str(statements)
    else:
        return ""


class EventCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categoryId = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)
    timestampe = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name


SERVICE_PRICE_TYPE_CHOICES = {
    ('per_day', 'Per Day'), ('per_person', 'Per Person'), ('per_event', 'Per Event'), }


class Add_service_ev(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=500)
    service_price = models.FloatField(max_length=50)
    service_price_type = models.CharField(
        max_length=50, choices=SERVICE_PRICE_TYPE_CHOICES, default='per_day')
    service_quantity = models.CharField(max_length=50)
    service_desc = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.service_name


class ServiceImage(models.Model):
    service = models.ForeignKey(
        Add_service_ev, related_name="image", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="service/", blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return nullStr(self.image.name)


DISCOUNT_TYPE = {('discount_on_total_bill', 'Discount On Total Bill'),
                 ('discount_on_equipment_or_item', 'Discount On Equipment Or Item'),
                 ('advance_and_discount_confirmation', 'Advance And Discount Confirmation')
                 }


class Discounts(models.Model):
    discountsId = models.AutoField(primary_key=True)
    discount_type = models.CharField(max_length=50, choices=DISCOUNT_TYPE)
    discount = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.discount



class OrgDiscounts(models.Model):
    event_id = models.ForeignKey('EventType',  on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    discount_type = models.CharField(max_length=50, choices=DISCOUNT_TYPE)
    discount = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.discount)


class OrgEquipmentId(models.Model):
    orgdiscount_id = models.ForeignKey(OrgDiscounts, on_delete=models.CASCADE)
    equipment_id = models.ForeignKey(Add_service_ev, on_delete=models.CASCADE)    
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.equipment_id)


SELECTED_BUSINESS = {
    ('places', 'Have You Place'),
    ('personal_skills', 'Personal Skills Bussiness'),
    ('group_skills', 'Group Skills Bussiness'),
}


class EventType(models.Model):
    eventId = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, related_name='user_id', on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50, choices=SELECTED_BUSINESS, default='places')
    category_id = models.ForeignKey(EventCategory, related_name='category', on_delete=models.CASCADE)
    display_name = models.CharField(max_length=50)   
    live = models.BooleanField(default=False) 
    is_active = models.BooleanField(default=True)
    timestampe = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_type


class EventWithDiscount(models.Model):
    selected_discount = models.ForeignKey(OrgDiscounts, related_name='selected_discount', on_delete=models.CASCADE)
    event_id = models.ForeignKey(EventType, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    timestampe = models.DateTimeField(auto_now_add=True)


class EventWithServices(models.Model):
    selected_service = models.ForeignKey(Add_service_ev, related_name='selected_service', on_delete=models.CASCADE)
    event_id = models.ForeignKey(EventType, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    timestampe = models.DateTimeField(auto_now_add=True)


class createEvent(models.Model):
    event_id = models.ForeignKey(EventType, related_name='event_id', on_delete=models.CASCADE)
    e_user = models.ForeignKey(User, on_delete=models.CASCADE)
    # serivceId = models.ForeignKey(Add_service_ev, related_name='service_id', on_delete=models.CASCADE, null=True, blank=True)
    # discountId = models.ForeignKey(OrgDiscounts, related_name='discount_id', on_delete=models.CASCADE, null=True, blank=True)
    t_and_c = models.TextField(max_length=5000)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    youtube = models.CharField(max_length=255, blank=True, null=True)
    pinterest = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)
    calender = models.CharField(max_length=255)
    live = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    timestampe = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_id.display_name


# class createEvent(models.Model):
#     event_type = models.CharField(
#         max_length=50, choices=SELECTED_BUSINESS, default='places')
#     eventId = models.AutoField(primary_key=True)
#     e_user = models.ForeignKey(
#         User, on_delete=models.CASCADE)
#     categoryId = models.ForeignKey(
#         EventCategory, related_name='category_id', on_delete=models.CASCADE)
#     serivceId = models.ForeignKey(
#         Add_service_ev, related_name='service_id', on_delete=models.CASCADE)
#     placeId = models.ForeignKey('Add_Place_ev', related_name='service_id', on_delete=models.CASCADE)
#     display_name = models.CharField(max_length=50)
#     t_and_c = models.TextField(max_length=5000)
#     facebook = models.CharField(max_length=255, blank=True, null=True)
#     twitter = models.CharField(max_length=255, blank=True, null=True)
#     youtube = models.CharField(max_length=255, blank=True, null=True)
#     pinterest = models.CharField(max_length=255, blank=True, null=True)
#     instagram = models.CharField(max_length=255, blank=True, null=True)
#     linkedin = models.CharField(max_length=255, blank=True, null=True)
#     discountId = models.CharField(max_length=50)
#     calender = models.CharField(max_length=255)
#     live = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     timestampe = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.display_name


class Image_Event(models.Model):
    event = models.ForeignKey(
        EventType, related_name='image', on_delete=models.CASCADE)
    image = models.FileField(upload_to='event/image/')
    image_details = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return nullStr(self.image.name)


class Video_Event(models.Model):
    event = models.ForeignKey(
        EventType, related_name='video', on_delete=models.CASCADE)
    video = models.FileField(upload_to='event/video/')
    thumbnail = models.ImageField(
        upload_to='event/video/thumbnail/', null=True, blank=True)
    detail = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return nullStr(self.video.name)


PLACES_EVENT_FACILITIES = {
    ('romantic_stay', 'Romantic Stay'),
    ('romantic_lunch_dinner', 'Romantic Lunch/Dinner'),
    ('romantic_candlelight_dinner', 'Romantic Candlelight Dinner')
}


class Place_Events(models.Model):
    event = models.ForeignKey(
        EventType, related_name='place_event', on_delete=models.CASCADE)
    IncludingFacilities = models.CharField(
        max_length=100, choices=PLACES_EVENT_FACILITIES, default='romantic_stay')
    person_capacity = models.FloatField(max_length=250)
    parking_capacity = models.FloatField(max_length=250)
    address = models.TextField(max_length=10000)
    let = models.TextField(max_length=5100, blank=True)
    long = models.TextField(max_length=5100, blank=True)
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event.display_name


class Servic(models.Model):
    event = models.ForeignKey(
        Place_Events, related_name='service', on_delete=models.CASCADE, blank=True)
    service_name = models.TextField(max_length=5000, blank=True, null=True)
    service_price = models.FloatField(max_length=50, blank=True, null=True)
    # details = models.CharField(max_length=2500, blank=True, null=True)


PLACE_PRICE_TYPE_CHOICES = {
    ('per_day', 'PER DAY'), ('per_hour', 'PER HOUR'), ('per_event', 'PER EVENT'), }


class Add_Place_ev(models.Model):
    Id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(
        EventType, related_name='event', on_delete=models.CASCADE)
    place_banner = models.ImageField(
        upload_to='place/banner/', null=True, blank=True)
    place_price = models.FloatField(max_length=50)
    price_type = models.CharField(
        max_length=255, choices=PLACE_PRICE_TYPE_CHOICES, default=0)
    details = models.CharField(max_length=2500, blank=True)
    is_active = models.BooleanField(default=True)
    timestampe = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.place_name  


class EventPersonalDetails(models.Model):
    Id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    eventId = models.ForeignKey(
        EventType, related_name='personal_details', on_delete=models.CASCADE)
    professional_skill = models.CharField(
        max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=20)
    is_mobile_no_hidden = models.BooleanField(default=True)
    alt_mobile_no = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100)
    is_email_hidden = models.BooleanField(default=True)
    skill_banner = models.FileField(upload_to='personal_details/banner/', null=True, blank=True)
    price_type = models.CharField(
        max_length=255, choices=PLACE_PRICE_TYPE_CHOICES, default=0)
    flat_no = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    area = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class EventCompanyDetails(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    eventId = models.ForeignKey(
        EventType, related_name='company_details', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    gst = models.FileField(
        max_length=255, upload_to='image/events/company/gst')
    contact_no = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    about = models.TextField(blank=True, null=True)
    flat_no = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pincode = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class EventCompanyImage(models.Model):
    company_id = models.ForeignKey(
        EventCompanyDetails, related_name='image', on_delete=models.CASCADE)
    image = models.FileField(
        upload_to='image/events/company', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return nullStr(self.image.name)


class EventCompanyVideo(models.Model):
    company_id = models.ForeignKey(
        EventCompanyDetails, related_name='video', on_delete=models.CASCADE)
    video = models.FileField(
        upload_to='image/events/company/video', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return nullStr(self.video.name)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Personal Skill
# Personal skills business


def get_personalskill_pdf_filepath(self, filename):
    return f'ps/org_personalskill/{self.pk}/{"personalskill.pdf"}'


class O_PersonalSkills(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    perskillId = models.AutoField(primary_key=True)
    pro_category = models.CharField(max_length=250)
    pro_category_id = models.IntegerField(null=True)
    profession = models.CharField(max_length=250)
    profession_id = models.IntegerField(null=True)
    name = models.CharField(max_length=250)
    mobile_no = models.CharField(max_length=12)
    alt_mobile_no = models.CharField(max_length=12)
    email = models.EmailField(verbose_name='email',
                              max_length=250)
    work_price = models.FloatField(max_length=250)
    is_price_per_hr = models.BooleanField(default=False)
    work_discount = models.CharField(max_length=250, null=True)
    travel_cost = models.CharField(max_length=250, null=True)
    accommodation = models.CharField(max_length=250, null=True)
    food = models.CharField(max_length=250, null=True)

    equip_ids = models.CharField(max_length=255, null=True)

    com_name = models.CharField(max_length=250)
    com_gstfile = models.FileField(
        max_length=255, upload_to=get_personalskill_pdf_filepath, null=True)
    com_contact = models.CharField(max_length=12)
    com_email = models.EmailField(
        verbose_name='email', max_length=250)
    com_address = models.TextField(max_length=200)
    let = models.TextField(max_length=5100, blank=True)
    long = models.TextField(max_length=5100, blank=True)
    price = models.FloatField(max_length=250, null=True)
    facebook = models.CharField(max_length=250, blank=True)
    youtube = models.CharField(max_length=250, blank=True)
    twitter = models.CharField(max_length=250, blank=True)
    pinterest = models.CharField(max_length=250, blank=True)
    instagram = models.CharField(max_length=250, blank=True)
    vimeo = models.CharField(max_length=250, blank=True)
    live = models.BooleanField(default=False)
    whishlist_status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)


# @@@@
TYPE_CHOICES = {
    ('1', 'PER HOUR'),
    ('2', 'PER DAY'),
}


class ps_equipments(models.Model):
    user = models.ForeignKey(
        User, related_name='Equipments', on_delete=models.CASCADE)
    Id = models.AutoField(primary_key=True)
    equ_name = models.CharField(max_length=255)
    equ_price = models.FloatField(max_length=50)
    equ_price_period = models.FloatField(max_length=50)
    equ_price_type = models.CharField(
        max_length=255, choices=TYPE_CHOICES, default=0)
    equ_details = models.TextField(max_length=500)

# @@@@


class equipments_pskill(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    pskillid = models.ForeignKey(
        O_PersonalSkills, related_name='Equipment', on_delete=models.CASCADE)
    equpmentId = models.IntegerField(primary_key=True)
    equpment = models.CharField(max_length=255)
    equpment_price = models.FloatField(max_length=50)
    equpment_price_period = models.FloatField(max_length=50)
    equpment_price_type = models.CharField(max_length=225, null=True)
    equpment_details = models.TextField(max_length=5000)


def get_personalskill_image_filepath(self, filename):
    return f'ps/org_personalskill_img/{self.pk}/{"personalskill_img.png"}'


class ps_photo(models.Model):
    p_skill = models.ForeignKey(
        O_PersonalSkills, related_name='Photo', on_delete=models.CASCADE)
    photo_file = models.FileField(
        max_length=255, upload_to=get_personalskill_image_filepath)
    photo_price_period = models.FloatField(max_length=50)
    photo_details = models.TextField(max_length=500)
    live = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        new_image = compress(self.photo_file)
        self.photo_file = new_image
        super().save(*args, **kwargs)


# @@@@


def get_personalskill_video_filepath(self, filename):
    return f'ps/org_personalskill_video/{self.pk}/{"personalskill_video.mp4"}'


class ps_video(models.Model):
    p_skill = models.ForeignKey(
        O_PersonalSkills, related_name='Video', on_delete=models.CASCADE)
    video_file = models.FileField(
        max_length=255,  upload_to=get_personalskill_video_filepath)
    live = models.BooleanField(default=False)


# @@@@
def get_per_company_photo_filepath(self, filename):
    return f'ps/company_photos{self.pk}/{"company_photo.png"}'


class ps_companyphotos(models.Model):
    p_skill = models.ForeignKey(
        O_PersonalSkills, related_name='Company_photo', on_delete=models.CASCADE)
    c_photo_file = models.FileField(
        max_length=255,  upload_to=get_per_company_photo_filepath)
    live = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        new_image = compress(self.c_photo_file)
        self.c_photo_file = new_image
        super().save(*args, **kwargs)


# @@@@
def get_per_company_videos_filepath(self, filename):
    return f'ps/company_videos{self.pk}/{"company_video.mp4"}'


class ps_companyvideos(models.Model):
    p_skill = models.ForeignKey(
        O_PersonalSkills, related_name='Company_video', on_delete=models.CASCADE)
    c_video_file = models.FileField(
        max_length=255,  upload_to=get_per_company_videos_filepath)
    live = models.BooleanField(default=False)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Partner Company Business


def get_partnercompany_pdf_filepath(self, filename):
    return f'PC/org_partnercompany/{self.pk}/{"partnercompany.pdf"}'


class O_PartnerCompanys(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    parcomId = models.AutoField(primary_key=True)

    category = models.CharField(max_length=250, null=True)
    categoryId = models.IntegerField(null=True)

    name = models.CharField(max_length=250)
    mobile_no = models.CharField(max_length=12)
    alt_mobile_no = models.CharField(max_length=12)
    email_id = models.EmailField(
        verbose_name='email', max_length=250)

    equip_ids = models.CharField(max_length=255, null=True)

    artist = models.CharField(max_length=250, null=True)
    artist_price = models.FloatField(max_length=250, null=True)
    decor = models.CharField(max_length=250, null=True)
    decor_price = models.FloatField(max_length=250, null=True)
    w_price = models.FloatField(max_length=250)
    w_discount = models.CharField(max_length=250, null=True)
    travel_cost = models.CharField(max_length=250, null=True)
    accommodation = models.CharField(max_length=250, null=True)
    food = models.CharField(max_length=250, null=True)
    com_name = models.CharField(max_length=250)
    com_gstfile = models.FileField(
        max_length=255, upload_to=get_partnercompany_pdf_filepath, null=True)
    com_contact = models.CharField(max_length=12)
    com_email = models.EmailField(
        verbose_name='email', max_length=250)
    com_address = models.TextField(max_length=200)
    let = models.TextField(max_length=5100, blank=True)
    long = models.TextField(max_length=5100, blank=True)
    price = models.FloatField(max_length=250, null=True)
    facebook = models.CharField(max_length=500, blank=True)
    youtube = models.CharField(max_length=500, blank=True)
    twitter = models.CharField(max_length=500, blank=True)
    pinterest = models.CharField(max_length=500, blank=True)
    instagram = models.CharField(max_length=500, blank=True)
    vimeo = models.CharField(max_length=500, blank=True)
    live = models.BooleanField(default=False)
    whishlist_status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)


class pc_equipments(models.Model):
    user = models.ForeignKey(
        User, related_name='EquipmentsPc', on_delete=models.CASCADE)
    Id = models.AutoField(primary_key=True)
    equ_name = models.CharField(max_length=255)
    equ_price = models.FloatField(max_length=100)
    equ_price_period = models.FloatField(max_length=100)
    equ_price_type = models.CharField(
        max_length=255, choices=TYPE_CHOICES, default=0)
    equ_details = models.TextField(max_length=1000)


class equipments_pc(models.Model):
    pcid = models.ForeignKey(
        O_PartnerCompanys, related_name='Equipments', on_delete=models.CASCADE)
    equpmentId = models.IntegerField(primary_key=True)
    equpment = models.CharField(max_length=255)
    equpment_price = models.FloatField(max_length=50)
    equpment_price_period = models.FloatField(max_length=50)
    equpment_price_type = models.CharField(max_length=225, null=True)
    equpment_details = models.TextField(max_length=5000)


TYPE_CHOICES_ARTIST = {
    ('1', 'PER HOUR'),
    ('2', 'PER DAY'),
}


class pc_artist(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Id = models.AutoField(primary_key=True)
    artist = models.CharField(max_length=255)
    price = models.FloatField(max_length=100)
    price_type = models.CharField(
        max_length=100, default=1, choices=TYPE_CHOICES_ARTIST)


class pc_decor(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Id = models.AutoField(primary_key=True)
    decor_type = models.CharField(max_length=255)
    decor_price = models.FloatField(max_length=100)

# @@@@


def get_pc_photo_filepath(self, filename):
    return f'PC/photos{self.pk}/{"pc_photo.png"}'


class pc_photos(models.Model):
    pc = models.ForeignKey(
        O_PartnerCompanys, related_name='photo', on_delete=models.CASCADE)
    photo_file = models.FileField(
        max_length=255,  upload_to=get_pc_photo_filepath)
    live = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        new_image = compress(self.photo_file)
        self.photo_file = new_image
        super().save(*args, **kwargs)


# @@@@
def get_pc_videos_filepath(self, filename):
    return f'PC/videos{self.pk}/{"pc_video.mp4"}'


class pc_videos(models.Model):
    pc = models.ForeignKey(
        O_PartnerCompanys, related_name='video', on_delete=models.CASCADE)
    video_file = models.FileField(
        max_length=255,  upload_to=get_pc_videos_filepath)
    live = models.BooleanField(default=False)


# @@@@
def get_pc_company_photo_filepath(self, filename):
    return f'PC/company_photos{self.pk}/{"company_photo.png"}'


class pc_companyphotos(models.Model):
    pc = models.ForeignKey(
        O_PartnerCompanys, related_name='Company_photo', on_delete=models.CASCADE)
    c_photo_file = models.FileField(
        max_length=255,  upload_to=get_pc_company_photo_filepath)
    live = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        new_image = compress(self.c_photo_file)
        self.c_photo_file = new_image
        super().save(*args, **kwargs)


# @@@@
def get_pc_company_videos_filepath(self, filename):
    return f'PC/company_videos{self.pk}/{"company_video.mp4"}'


class pc_companyvideos(models.Model):
    pc = models.ForeignKey(
        O_PartnerCompanys, related_name='Company_video', on_delete=models.CASCADE)
    c_video_file = models.FileField(
        max_length=255,  upload_to=get_pc_company_videos_filepath)
    live = models.BooleanField(default=False)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  Wishlist
class Wishlists(models.Model):
    user = models.ForeignKey(
        User, related_name='Wishlist', on_delete=models.CASCADE)
    eventId = models.ForeignKey(
        EventType, related_name="EventWishlist", on_delete=models.CASCADE, null=True)
    partnerId = models.ForeignKey(
        O_PartnerCompanys, related_name="PartnerCompWishlist", on_delete=models.CASCADE, null=True)
    personalId = models.ForeignKey(
        O_PersonalSkills, related_name="PersonalSkillWishlist", on_delete=models.CASCADE, null=True)
    wishId = models.AutoField(primary_key=True)
    img = models.TextField(max_length=5000)
    category = models.CharField(max_length=250)
    name_ev = models.CharField(max_length=250)
    place_ev = models.CharField(max_length=250)
    price_ev = models.FloatField(max_length=250)


class O_Rats(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    eventId = models.ForeignKey(
        EventType, related_name="EventRating", on_delete=models.CASCADE, null=True)
    partnerId = models.ForeignKey(
        O_PartnerCompanys, related_name="PartnerCompRating", on_delete=models.CASCADE, null=True)
    personalId = models.ForeignKey(
        O_PersonalSkills, related_name="PersonalSkillRating", on_delete=models.CASCADE, null=True)
    ratId = models.AutoField(primary_key=True)
    stars = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField(verbose_name='email',
                              max_length=250)
    review = models.CharField(max_length=250)


class Checkouts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    eventId = models.ForeignKey(
        EventType, related_name="EventCheckout", on_delete=models.CASCADE, null=True)
    partnerId = models.ForeignKey(
        O_PartnerCompanys, related_name="PartnerComCheckout", on_delete=models.CASCADE, null=True)
    personalSkillId = models.ForeignKey(
        O_PersonalSkills, related_name="PersonalSkillCheckout", on_delete=models.CASCADE, null=True)
    chkoId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    email = models.EmailField(verbose_name='email',
                              max_length=250)
    phone_no = models.CharField(max_length=12)
    address = models.TextField(max_length=1000)


class Tickets(models.Model):
    user = models.ForeignKey(
        User, related_name='Tickets', on_delete=models.CASCADE)
    holdername = models.TextField(max_length=5000, null=True, blank=True)
    holdercontact = models.CharField(max_length=225, null=True)
    eventId = models.ForeignKey(
        EventType, related_name="EventTickets", on_delete=models.CASCADE, null=True)
    partnerId = models.ForeignKey(
        O_PartnerCompanys, related_name="PartnerComTickets", on_delete=models.CASCADE, null=True)
    personalSkillId = models.ForeignKey(
        O_PersonalSkills, related_name="PersonalSkillTickets", on_delete=models.CASCADE, null=True)
    orgId = models.CharField(max_length=255, null=True)
    ticketId = models.AutoField(primary_key=True)
    trans_Id = models.CharField(max_length=250, null=True)
    img = models.TextField(max_length=5000, null=True)
    ticket_no = models.CharField(max_length=250, unique=True)
    payment_status = models.CharField(max_length=250, null=True)
    amount = models.FloatField(max_length=250, null=True)
    category = models.CharField(max_length=250, null=True)
    name = models.CharField(max_length=250, null=True)
    address = models.TextField(max_length=1000, null=True)
    date = models.DateTimeField(auto_now_add=True)
    receiver = models.CharField(max_length=255, null=True)
    roomname = models.TextField(max_length=2500, blank=True)
    # holdername = models.CharField(max_length=225, null=True)

    def save(self, *args, **kwargs):
        if self.ticket_no == "":
            num_ = TicketNum()
            self.ticket_no = num_
        super().save(*args, **kwargs)


class ForWho(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Id = models.AutoField(primary_key=True)
    for_who = models.IntegerField()
    plan_name = models.CharField(max_length=500)


class PersonalSkillCategory(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=500)


class PersonalSkillSubCategory(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Id = models.AutoField(primary_key=True)
    pscategoryid = models.ForeignKey(
        PersonalSkillCategory, related_name='SubCategory', on_delete=models.CASCADE)
    category = models.CharField(max_length=500)


class PartnerCompanyCategory(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=500)


class Rooms(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Id = models.AutoField(primary_key=True)
    user = models.BigIntegerField()
    name = models.TextField(max_length=2500, blank=True)
    roomid = models.TextField(max_length=2500, blank=True)
    socketId = models.TextField(max_length=2500, blank=True)


class Message(models.Model):
    author = models.ForeignKey(
        User, related_name='author_message', on_delete=models.CASCADE)
    sender = BigIntegerField()
    receiver = BigIntegerField()
    content = models.TextField()
    room = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.name

    def last_10_messages():
        return Message.objects.order_by('-timestamp').filter()[:5]


class ChatBot(models.Model):
    sender = models.ForeignKey(
        User, related_name='sender', on_delete=models.CASCADE)
    message = models.TextField(max_length=5000, blank=True)
    reply = models.TextField(max_length=5000, blank=True)
    timestamp = models.DateTimeField(auto_now=True)


class fcmtoken(models.Model):
    user = models.OneToOneField(
        User, related_name='token', on_delete=models.CASCADE)
    tokId = models.AutoField(primary_key=True)
    apptoken = models.TextField(max_length=5000)
    platform_type = models.TextField(max_length=2000)


NOTIFICATION_TYPE = (
    ('1', 'SMS'),
    ('2', 'NOTIFICATION'),
    ('3', 'EMAIL'),
)


def notification_image_filepath(self, filename):
    return f'notification/notification_img/{self.pk}/{"notification_img.png"}'


class NotificationData(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    text = models.TextField(max_length=5000, blank=True)
    image = models.FileField(
        max_length=255, upload_to=notification_image_filepath, blank=True)
    notification_type = models.CharField(
        max_length=10, choices=NOTIFICATION_TYPE, default=1)
    forwhat = models.CharField(max_length=255, null=True, blank=True)
    date_time = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)


NOTIFICATION_STATUS = (
    ('1', 'panding'),
    ('2', 'send')
)
SELECTED_BUSINESS = (
    ('1', 'HVE YOU PLACES?'),
    ('2', 'PERSONAL SKILL BUSINESS'),
    ('3', 'PARTNER COMPANY BUSINESS')
)
MEMBERSHIPPLAN = (
    ('1', 'LOCAL OFFER MONTHLY'),
    ('2', 'EVENT SUBSCRIPTION'),
    ('3', 'LIVE STREAM SUBSCRIPTION')
)


class Notification(models.Model):
    # notificationid = models.ForeignKey(NotificationData, related_name="NotificationData", on_delete=models.RESTRICT)
    organizer = models.ForeignKey(
        User, related_name="Notification", on_delete=models.CASCADE)
    userIds = models.TextField(max_length=50000, null=True)
    selected_business = models.CharField(
        max_length=10, choices=SELECTED_BUSINESS)
    status = models.CharField(
        max_length=10, choices=NOTIFICATION_STATUS, default=1)
    membershipplan = models.CharField(
        max_length=10, choices=MEMBERSHIPPLAN, default=1)
    selected_page = models.TextField(max_length=5000, null=True)
    notification_type = models.TextField(max_length=50000, null=True)
    notification_title = models.TextField(max_length=5000, null=True)
    notification_text = models.TextField(max_length=5000, null=True)
    notification_img = models.FileField(
        max_length=255, upload_to=notification_image_filepath, blank=True)
    date_time = models.DateTimeField(null=True, blank=True)


# Membership planing
DISCOUNT_CHOICES = (
    ('1', '%'),
    ('2', 'fix'),
)

PLAN_CHOICES = (
    ('0', 'Monthly'),
    ('1', 'Yearly'),
)


class Subscriptionplan(models.Model):
    id = models.AutoField(primary_key=True)
    plan_name = models.CharField(max_length=255)
    plan_type = models.CharField(
        max_length=10, choices=PLAN_CHOICES, default=1)
    price = models.FloatField()
    # yearly_price = models.FloatField()
    discount_value = models.FloatField()
    discount_type = models.CharField(
        max_length=10, choices=DISCOUNT_CHOICES, default=1)
    video_count = models.IntegerField()
    image_count = models.IntegerField()
    sms = models.BooleanField(default=False)
    notifications = models.BooleanField(default=False)
    emails = models.BooleanField(default=False)
    socialmedia_promotion = models.BooleanField(default=False)

    def __str__(self):
        return self.id


STATUS_CHOICES = (
    ('0', 'DELETED'),
    ('1', 'ACTIVE'),
    ('2', 'DEACTIVE'),
)


class Membership(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, related_name="Subscriptionplan", on_delete=models.RESTRICT)
    plan_name = models.CharField(max_length=255)
    total_price = models.FloatField(null=True)
    # price = models.FloatField(null=True)
    # yearly_price = models.FloatField(null=True)
    # discount_value = models.FloatField()
    # discount_type = models.CharField(
    # max_length=10, choices=DISCOUNT_CHOICES, default=1)
    video_count = models.IntegerField()
    image_count = models.IntegerField()
    sms = models.BooleanField(default=False)
    notifications = models.BooleanField(default=False)
    emails = models.BooleanField(default=False)
    socialmedia_promotion = models.BooleanField(default=False)
    date_of_purchase = models.DateField(auto_now=True)
    date_of_expiry = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default=1)
    payment_id = models.TextField(max_length=500, null=True)
    order_id = models.TextField(max_length=255, null=True)


def asd_image_filepath(self, filename):
    return f'ads/ads_img/{self.pk}/{"ads_img.png"}'


def asd_video_filepath(self, filename):
    return f'ads/ads_video/{self.pk}/{"ads_video.mp4"}'


POSITION_CHOICES = {
    ('0', 'HOME PAGE'),
    ('1', 'EVENT LISTING PAGE'),
    ('2', 'EVENT VIEW PAGE'),
}


class Advertisement(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    text = models.TextField(max_length=5000, blank=True, null=True)
    link = models.TextField(max_length=5000, blank=True)
    image = models.FileField(
        max_length=255, upload_to=asd_image_filepath, null=True, blank=True)
    video = models.FileField(
        max_length=255, upload_to=asd_video_filepath, null=True, blank=True)
    position = models.CharField(
        max_length=255, choices=POSITION_CHOICES, default=0)

    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)


class GetInTouch(models.Model):
    gitId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    email = models.EmailField(verbose_name='email',
                              max_length=250)
    contact = models.CharField(max_length=15, validators=[
                               MinLengthValidator(10)])
    message = models.TextField(max_length=50000)


class exceluser(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    orgID = models.ForeignKey(
        User, related_name="excelUser", on_delete=models.RESTRICT)
    email = models.TextField(max_length=500, null=True)
    mobile_no = models.TextField(max_length=15, null=True)
    name = models.TextField(max_length=500, null=True)
    status = models.CharField(
        max_length=255, choices=NOTIFICATION_STATUS, default=1)
