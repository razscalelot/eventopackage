from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from userApi.models import *

# Register your models here.


class AccountAdmin(UserAdmin):
    list_display = ['email',
                    'name',
                    'userId',
                    'phone_no',
                    'date',
                    'last_login',
                    'password',
                    'is_admin',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'refer_code',
                    'users_ref_code',
                    'profile_img']
    search_fields = ('email', 'phone_no')
    readonly_fields = ('userId', 'date', 'last_login')
    ordering = ('email',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    add_fieldsets = (
        (None, {'fields': ('email', 'name', 'phone_no', 'password', 'refer_code')}),
    )


admin.site.register(User, AccountAdmin)
admin.site.register(Transactions)
admin.site.register(RedeemCoins)
admin.site.register(EventCategory)
admin.site.register(createEvent)
admin.site.register(Place_Events)
admin.site.register(Add_Place_ev)
admin.site.register(Add_service_ev)
admin.site.register(Image_Event)
admin.site.register(Video_Event)
admin.site.register(O_PersonalSkills)
admin.site.register(ps_equipments)
admin.site.register(equipments_pskill)
admin.site.register(ps_photo)
admin.site.register(ps_video)
admin.site.register(ps_companyphotos)
admin.site.register(ps_companyvideos)
admin.site.register(O_PartnerCompanys)
admin.site.register(pc_equipments)
admin.site.register(equipments_pc)
admin.site.register(pc_artist)
admin.site.register(pc_decor)
admin.site.register(pc_photos)
admin.site.register(pc_videos)
admin.site.register(pc_companyphotos)
admin.site.register(Wishlists)
admin.site.register(O_Rats)
admin.site.register(Checkouts)
admin.site.register(Tickets)
admin.site.register(ForWho)
admin.site.register(PersonalSkillCategory)
admin.site.register(PersonalSkillSubCategory)
admin.site.register(PartnerCompanyCategory)
admin.site.register(Rooms)
admin.site.register(Message)
admin.site.register(ChatBot)
admin.site.register(fcmtoken)
admin.site.register(NotificationData)
admin.site.register(Notification)
admin.site.register(Subscriptionplan)
admin.site.register(Membership)
admin.site.register(Advertisement)
admin.site.register(GetInTouch)
admin.site.register(exceluser)
admin.site.register(Discounts)
