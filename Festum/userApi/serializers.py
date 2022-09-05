
# from django.db.models import fields
from dataclasses import fields
from pyexpat import model
from unicodedata import category
from rest_framework import serializers
from userApi.models import *


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ user


class O_RatSerializers(serializers.ModelSerializer):
    class Meta:
        model = O_Rats
        fields = (
            'User',
            'ratId',
            'eventId',
            'partnerId',
            'personalId',
            'stars',
            'name',
            'email',
            'review'
        )


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlists
        fields = (
            'user',
            'wishId',
            'eventId',
            'partnerId',
            'personalId',
            'img',
            'category',
            'name_ev',
            'place_ev',
            'price_ev',
        )
        extra_kwargs = {'wishId': {'read_only': True}}


class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = (
            'id',
            'user',
            'img',
            'translation_type',
            'details',
            'Amount',
            'date'
        )
        extra_kwargs = {'id': {'read_only': True}}


class RedeemCoinsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedeemCoins
        fields = (
            'id',
            'user',
            'Amount',
            'upi_id',
            'price',
            'date'
        )
        extra_kwargs = {'id': {'read_only': True}}


class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkouts
        fields = (
            'user',
            'eventId',
            'partnerId',
            'personalSkillId',
            'chkoId',
            'name',
            'email',
            'phone_no',
            'address'
        )
        extra_kwargs = {'chkoId': {'read_only': True}}


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = (
            'user',
            'orgId',
            'holdername',
            'holdercontact',
            'eventId',
            'partnerId',
            'personalSkillId',
            'ticketId',
            'trans_Id',
            'img',
            'ticket_no',
            'payment_status',
            'amount',
            'category',
            'name',
            'address',
            'receiver',
            'roomname',
            'date',
        )
        extra_kwargs = {'ticketId': {'read_only': True},
                        'ticket_no': {'read_only': True}}


class RegistrationSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ['userId', 'email', 'name', 'phone_no', 'password',
                  'refer_code', 'users_ref_code', 'profile_img', 'user_type', 'otp', 'coins']
        extra_kwargs = {
            'password': {'write_only': True}, 'Wishlist': {'read_only': True}, 'Refers': {'read_only': True}, 'Tickets': {'read_only': True}, 'otp': {'read_only': True}
        }

   


def checkPassword(self, **kwargs):
    print('call')
    print('self', self)
    account = User(
        email=self.validated_data['email'],
        name=self.validated_data['name'],
        phone_no=self.validated_data['phone_no'],
    )
    if self.validated_data['refer_code'] != None:
        refer_code = self.validated_data['refer_code'],

    password = self.validated_data['password']
    password2 = self.validated_data['password2']
    if password != password2:
        raise serializers.ValidationError(
            {'password': 'Passwords must match.'})
    account.set_password(password)
    return account


class AdminRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['userId', 'email', 'name', 'phone_no', 'password',
                  'password2', 'refer_code', 'users_ref_code', 'profile_img', 'user_type', 'otp', 'coins']

    def save(self, **kwargs):
        account = checkPassword(self, **kwargs)
        account.is_admin = True
        account.user_type = 1
        account.save()
        return account


class SubAdminRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['userId', 'email', 'name', 'phone_no', 'password',
                  'password2', 'refer_code', 'users_ref_code', 'profile_img', 'user_type', 'otp', 'coins']

    def save(self, **kwargs):
        account = checkPassword(self, **kwargs)
        account.is_staff = True
        account.user_type = 2
        account.save()
        return account


class ExecutiveRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['userId', 'email', 'name', 'phone_no', 'password',
                  'password2', 'refer_code', 'users_ref_code', 'profile_img', 'user_type', 'otp', 'coins']

    def save(self, **kwargs):
        account = checkPassword(self, **kwargs)
        account.user_type = 3
        account.save()
        return account


class OrganizerRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['userId', 'email', 'name', 'phone_no', 'password',
                  'password2', 'refer_code', 'users_ref_code', 'profile_img', 'user_type', 'otp', 'coins']

    def save(self, **kwargs):
        account = checkPassword(self, **kwargs)
        account.user_type = 4
        account.save()
        return account


class CustomerRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['userId', 'email', 'name', 'phone_no', 'password',
                  'password2', 'refer_code', 'users_ref_code', 'profile_img', 'user_type', 'otp', 'coins']

    def save(self, **kwargs):
        account = checkPassword(self, **kwargs)
        account.user_type = 5
        account.save()
        return account


class ResetpasswordSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    userId = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('userId', 'password', 'password2')

    def save(self):
        # print(kwargs)
        userId = self.validated_data['userId']
        account = User.objects.get(userId=userId)
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        print(password, password2, userId, account)
        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must match.'})
        account.set_password(password)
        account.save()
        return account


class forgotpasswordSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    email = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2')

    def save(self):
        # print(kwargs)
        email = self.validated_data['email']
        account = User.objects.get(email=email)
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        print(password, password2, email, account)
        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must match.'})
        account.set_password(password)
        account.save()
        return account


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emails
        fields = ['email']

    def save(self):

        email = Emails(
            email=self.validated_data['email']
        )
        email.save()
        return email


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Event


class addplaceevSerializers(serializers.ModelSerializer):
    class Meta:
        model = Add_Place_ev
        fields = [
            'Id',
            'user_id',
            'event',
            'place_banner',
            'place_price',
            'price_type',
            'details',
        ]
        extra_kwargs = {'id': {'read_only': True}}


class ServicSerializers(serializers.ModelSerializer):
    class Meta:
        model = Servic
        fields = [
            'id',
            'event',
            'service_name',
            'service_price',
            # 'details',
        ]
        extra_kwargs = {'id': {'read_only': True}}


class addserviceevSerializers(serializers.ModelSerializer):
    class Meta:
        model = Add_service_ev
        fields = [
            'Id',
            'user',
            'service_name',
            'service_price',
            'service_price_type',
            'service_desc',
        ]
        extra_kwargs = {'id': {'read_only': True}}


class eventimageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Image_Event
        fields = [
            'id',
            'event',
            'image',
            'image_details',
            'live'
        ]
        extra_kwargs = {'id': {'read_only': True}}


class eventvideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Video_Event
        fields = [
            'id',
            'event',
            'video',
            'live'
        ]
        extra_kwargs = {'id': {'read_only': True}}


class EventPersonalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventPersonalDetails
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}


class EventCompanyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCompanyDetails
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}


class Place_EventSerializers(serializers.ModelSerializer):
    service = ServicSerializers(read_only=True, many=True)

    class Meta:
        model = Place_Events
        fields = '__all__'
        # fields = (
        #     'id',
        #     'event',
        #     'for_who',
        #     'for_who_Id',
        #     'place_Id',
        #     'place_name',
        #     'place_price',
        #     'service',
        #     'place_description',
        #     'IncludingFacilities',
        #     # 'service_Id',
        #     # 'service_name',
        #     # 'service_price',
        #     'person_capacity',
        #     'parking_capacity',
        #     'address',
        #     'let',
        #     'long',
        #     't_and_c',
        #     'facebook',
        #     'youtube',
        #     'twitter',
        #     'pinterest',
        #     'instagram',
        #     'vimeo',

        # )
        extra_kwargs = {'eventId': {'read_only': True},
                        'service': {'read_only': True}}


class DiscountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Discounts
        fields = '__all__'


class EventCategorySerializers(serializers.ModelSerializer):
   
    class Meta:
        model = EventCategory
        fields = (
            'categoryId',
            'category_name',
            'display_name',
            'user'
        )
        extra_kwargs = {'categoryId': {'read_only': True}}


class createEventSerializers(serializers.ModelSerializer):
    image = eventimageSerializers(read_only=True, many=True)
    video = eventvideoSerializers(read_only=True, many=True)
    e_user = RegistrationSerializer(read_only=True)
    categoryId = EventCategorySerializers(read_only=True)
    serivceId = addserviceevSerializers(read_only=True)
    placeId = addplaceevSerializers(read_only=True)
    personal_details = serializers.SerializerMethodField()
    company_details = serializers.SerializerMethodField()
    place_event = Place_EventSerializers(read_only=True, many=True)
    discountId = serializers.SerializerMethodField()

    @staticmethod
    def get_discountId(obj):
        discount = Discounts.objects.filter(id=obj.discountId)
        discountId = DiscountSerializers(discount, many=True)
        return discountId.data

    @staticmethod
    def get_company_details(obj):
        company = EventCompanyDetails.objects.filter(eventId=obj.eventId)
        company_details = EventCompanyDetailsSerializer(company, many=True)
        return company_details.data

    @staticmethod
    def get_place_event(obj):
        p_event = Place_Events.objects.filter(event=obj.eventId)
        place_event = Place_EventSerializers(p_event, many=True)
        return place_event.data

    @staticmethod
    def get_personal_details(obj):
        personal = EventPersonalDetails.objects.filter(eventId=obj.eventId)
        personal_details = EventPersonalDetailsSerializer(personal, many=True)
        return personal_details.data

    @staticmethod
    def get_placeId(obj):
        place = Add_Place_ev.objects.filter(Id=obj.placeId)
        placeId = addplaceevSerializers(place)
        return placeId.data

    class Meta:
        model = createEvent
        fields = ('eventId', 'event_type', 'display_name', 'live', 'image',
                  'video', 'e_user', 'categoryId', 'serivceId', 'placeId', 'personal_details', 'company_details',
                  'place_event', 't_and_c', 'facebook', 'twitter', 'youtube', 'pinterest', 'instagram', 'linkedin',
                  'discountId', 'calender', 'is_active', 'timestampe')

    # EventRating = O_RatSerializers(read_only=True, many=True)
    # EventWishlist = WishlistSerializer(read_only=True, many=True)
    # event = Place_EventSerializers(read_only=True, many=True)
    # image = eventimageSerializers(read_only=True, many=True)
    # video = eventvideoSerializers(read_only=True, many=True)
    # EventCheckout = CheckoutSerializer(read_only=True, many=True)
    # EventTickets = TicketSerializer(read_only=True, many=True)

    # class Meta:
    #     model = createEvent
    #     fields = [
    #         'eventId',
    #         'User',
    #         'category',
    #         'categoryId',
    #         'display_name',
    #         'live',
    #         'price',
    #         'event',
    #         'EventRating',
    #         'image',
    #         'video',
    #         'EventWishlist',
    #         'EventCheckout',
    #         'EventTickets',
    #         'whishlist_status',
    #         'date'
    #     ]
    #     extra_kwargs = {'event_id': {'read_only': True}, 'EventRating': {
    #         'read_only': True}, 'image': {'read_only': True}, 'event': {'read_only': True}, 'video': {'read_only': True}, 'EventWishlist': {'read_only': True}, 'EventCheckout': {'read_only': True}, 'EventTickets': {'read_only': True}}


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Personal Skill
class addequipmentpsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ps_equipments
        fields = [
            'user',
            'Id',
            'equ_name',
            'equ_price',
            'equ_price_period',
            'equ_price_type',
            'equ_details',
        ]
        extra_kwargs = {'id': {'read_only': True}}


class addphotopsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ps_photo
        fields = [
            'id',
            'p_skill',
            'photo_file',
            'photo_price_period',
            'photo_details',
            'live'
        ]
        extra_kwargs = {'id': {'read_only': True}}


class addvideopsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ps_video
        fields = [
            'id',
            'p_skill',
            'video_file',
            'live'
        ]
        extra_kwargs = {'id': {'read_only': True}}


class companyphotopsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ps_companyphotos
        fields = [
            'id',
            'p_skill',
            'c_photo_file',
            'live'
        ]
        extra_kwargs = {'id': {'read_only': True}}


class companyvideopsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ps_companyvideos
        fields = [
            'id',
            'p_skill',
            'c_video_file',
            'live'
        ]
        extra_kwargs = {'id': {'read_only': True}}


class equipments_pskillSerializers(serializers.ModelSerializer):
    class Meta:
        model = equipments_pskill
        fields = [
            'pskillid',
            'equpmentId',
            'equpment',
            'equpment_price',
            'equpment_price_period',
            'equpment_price_type',
            'equpment_details'
        ]


class O_PersonalskillSerializers(serializers.ModelSerializer):
    Photo = addphotopsSerializers(read_only=True, many=True)
    Video = addvideopsSerializers(read_only=True, many=True)
    Company_photo = companyphotopsSerializers(read_only=True, many=True)
    Company_video = companyvideopsSerializers(read_only=True, many=True)
    PersonalSkillRating = O_RatSerializers(read_only=True, many=True)
    PersonalSkillCheckout = CheckoutSerializer(read_only=True, many=True)
    PersonalSkillTickets = TicketSerializer(read_only=True, many=True)
    PersonalSkillWishlist = WishlistSerializer(read_only=True, many=True)
    Equipment = equipments_pskillSerializers(read_only=True, many=True)

    class Meta:
        model = O_PersonalSkills
        fields = (
            'User',
            'perskillId',
            'pro_category',
            'pro_category_id',
            'profession',
            'profession_id',
            'name',
            'mobile_no',
            'alt_mobile_no',
            'email',
            'work_price',
            'is_price_per_hr',
            'work_discount',
            'travel_cost',
            'accommodation',
            'food',
            'equip_ids',
            'Equipment',
            'Photo',
            'Video',
            'com_name',
            'com_gstfile',
            'com_contact',
            'com_email',
            'com_address',
            'let',
            'long',
            'Company_photo',
            'Company_video',
            'price',
            'facebook',
            'youtube',
            'twitter',
            'pinterest',
            'instagram',
            'vimeo',
            'live',
            'whishlist_status',
            'PersonalSkillRating',
            'PersonalSkillCheckout',
            'PersonalSkillTickets',
            'PersonalSkillWishlist',
            'date'

        )
        extra_kwargs = {'perskillId': {'read_only': True}, 'Photo': {'read_only': True}, 'Video': {
            'read_only': True}, 'company_photo': {'read_only': True}, 'company_video': {'read_only': True}, 'PersonalSkillRating': {'read_only': True}, 'PersonalSkillCheckout': {'read_only': True}, 'PersonalSkillTickets': {'read_only': True}, 'PersonalSkillWishlist': {'read_only': True}, 'Equipment': {'read_only': True}}

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# 1


class pc_equipmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = pc_equipments
        fields = [
            'user',
            'Id',
            'equ_name',
            'equ_price',
            'equ_price_period',
            'equ_price_type',
            'equ_details'
        ]
        extra_kwargs = {'Id': {'read_only': True}}
# 2


class EquipmentsPcSerializers(serializers.ModelSerializer):
    class Meta:
        model = equipments_pc
        fields = [
            'pcid',
            'equpmentId',
            'equpment',
            'equpment_price',
            'equpment_price_period',
            'equpment_price_type',
            'equpment_details'
        ]


class pc_artistSerializers(serializers.ModelSerializer):
    class Meta:
        model = pc_artist
        fields = [
            'id',
            'artist',
            'price',
            'price_type'
        ]
        extra_kwargs = {'id': {'read_only': True}}

# 3


class pc_decorSerializers(serializers.ModelSerializer):
    class Meta:
        model = pc_decor
        fields = [
            'id',
            'decor_type',
            'decor_price'
        ]
        extra_kwargs = {'id': {'read_only': True}}

# 4


class pc_photosSerializers(serializers.ModelSerializer):
    class Meta:
        model = pc_photos
        fields = [
            'id',
            'pc',
            'photo_file',
            'live'
        ]
        extra_kwargs = {'id': {'read_only': True}}

# 5


class pc_videosSerializers(serializers.ModelSerializer):
    class Meta:
        model = pc_videos
        fields = [
            'id',
            'pc',
            'video_file',
            'live'
        ]
        extra_kwargs = {'id': {'read_only': True}}

# 6


class pc_companyphotosSerializers(serializers.ModelSerializer):
    class Meta:
        model = pc_companyphotos
        fields = [
            'id',
            'pc',
            'c_photo_file',
            'live'
        ]
        extra_kwargs = {'id': {'read_only': True}}
# 7


class pc_companyvideosSerializers(serializers.ModelSerializer):
    class Meta:
        model = pc_companyvideos
        fields = [
            'id',
            'pc',
            'c_video_file',
            'live'
        ]
        extra_kwargs = {'id': {'read_only': True}}


class O_PartnercompanySerializers(serializers.ModelSerializer):
    photo = pc_photosSerializers(read_only=True, many=True)
    video = pc_videosSerializers(read_only=True, many=True)
    Company_photo = pc_companyphotosSerializers(read_only=True, many=True)
    Company_video = pc_companyvideosSerializers(read_only=True, many=True)
    PartnerCompRating = O_RatSerializers(read_only=True, many=True)
    PartnerComCheckout = CheckoutSerializer(read_only=True, many=True)
    PartnerComTickets = TicketSerializer(read_only=True, many=True)
    PartnerCompWishlist = WishlistSerializer(read_only=True, many=True)
    Equipments = EquipmentsPcSerializers(read_only=True, many=True)

    class Meta:
        model = O_PartnerCompanys
        fields = (
            'User',
            'parcomId',
            'category',
            'categoryId',
            'name',
            'mobile_no',
            'alt_mobile_no',
            'email_id',
            'equip_ids',
            'Equipments',
            'artist',
            'artist_price',
            'decor',
            'decor_price',
            'w_price',
            'w_discount',
            'travel_cost',
            'accommodation',
            'food',
            'photo',
            'video',
            'com_name',
            'com_gstfile',
            'com_contact',
            'com_email',
            'com_address',
            'let',
            'long',
            'Company_photo',
            'Company_video',
            'price',
            'facebook',
            'youtube',
            'twitter',
            'pinterest',
            'instagram',
            'vimeo',
            'live',
            'whishlist_status',
            'PartnerCompRating',
            'PartnerComCheckout',
            'PartnerComTickets',
            'PartnerCompWishlist',
            'date'
        )
        extra_kwargs = {'perskillId': {'read_only': True},
                        'photo': {'read_only': True}, 'video': {'read_only': True}, 'Company_photo': {'read_only': True}, 'Company_video': {'read_only': True}, 'PartnerCompRating': {'read_only': True}, 'PartnerComCheckout': {'read_only': True}, 'PartnerComTickets': {'read_only': True}, 'PartnerCompWishlist': {'read_only': True}, 'Equipments': {'read_only': True}}


class ForWhoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ForWho
        fields = (
            'Id',
            'for_who',
            'plan_name',
        )
        extra_kwargs = {'Id': {'read_only': True}}


class PersonalSkillSubCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = PersonalSkillSubCategory
        fields = (
            'Id',
            'pscategoryid',
            'category',
        )
        extra_kwargs = {'Id': {'read_only': True}}


class PersonalSkillCategorySerializers(serializers.ModelSerializer):
    # SubCategory = PersonalSkillSubCategorySerializers(
    #     read_only=True, many=True)

    class Meta:
        model = PersonalSkillCategory
        fields = (
            'Id',
            'category'
        )
        extra_kwargs = {'Id': {'read_only': True}}


class PartnerCompanyCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = PartnerCompanyCategory
        fields = (
            'Id',
            'category',
        )
        extra_kwargs = {'Id': {'read_only': True}}


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = [
            'Id',
            'user',
            'sender',
            'receiver',
            'name',
            'roomid',
            'socketId'
        ]
        extra_kwargs = {'Id': {'read_only': True}}


class ChatBotSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChatBot
        fields = [
            'sender',
            'message',
            'reply',
            'timestamp'
        ]


class fcmtokenSerializers(serializers.ModelSerializer):
    class Meta:
        model = fcmtoken
        fields = [
            'user',
            'tokId',
            'apptoken',
            'platform_type'
        ]
        extra_kwargs = {'tokId': {'read_only': True}}


class SubscriptionplanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subscriptionplan
        fields = [
            'id',
            'plan_name',
            'plan_type',
            'price',
            'discount_value',
            'discount_type',
            'video_count',
            'image_count',
            'sms',
            'notifications',
            'emails',
            'socialmedia_promotion'
        ]
        extra_kwargs = {'id': {'read_only': True}}


class MembershipSerializers(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = [
            'id',
            'user',
            'order_id',
            'plan_name',
            'total_price',
            'video_count',
            'image_count',
            'sms',
            'notifications',
            'emails',
            'socialmedia_promotion',
            'date_of_purchase',
            'date_of_expiry',
            'status',
            'payment_id'
        ]
        extra_kwargs = {'id': {'read_only': True}}


class AdvertisementSerializers(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = [
            'id',
            'text',
            'link',
            'image',
            'video',
            'position'
        ]
        extra_kwargs = {'id': {'read_only': True}}


class NotificationDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = NotificationData
        fields = [
            'id',
            'text',
            'image',
            'notification_type',
            'date_time',
            'forwhat'
        ]
        extra_kwargs = {'id': {'read_only': True}}


class NotificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            # 'notificationid',
            'organizer',
            'membershipplan',
            'selected_business',
            'userIds',
            'status',
            'selected_page',
            'notification_title',
            'notification_type',
            'notification_text',
            'notification_img',
            'date_time'
        ]
        extra_kwargs = {'id': {'read_only': True}}


class GetInTouchSerializers(serializers.ModelSerializer):
    class Meta:
        model = GetInTouch
        fields = (
            'gitId',
            'name',
            'email',
            'contact',
            'message',
        )
        extra_kwargs = {'gitId': {'read_only': True}}


class excelUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = exceluser
        fields = (
            'id',
            'orgID',
            'email',
            'mobile_no',
            'name',
            'status'
        )
        extra_kwargs = {'id': {'read_only': True}}
