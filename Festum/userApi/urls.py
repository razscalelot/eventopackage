from django.conf.urls import url
from userApi import views, org
from userApi.views import CustomAuthToken, Logout
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [

    # url(r'register$', views.registration_view, name="register"),
    url(r'register/admin$', views.adminRegistration, name="Admin"),
    url(r'register/subadmin$', views.subAdminRegistration, name="SubAdmin"),
    url(r'register/organizer$', views.organizerRegistration, name="Organizer"),
    url(r'register/executive$', views.executiveRegistration, name="Executive"),
    url(r'register/customer$', views.customerRegistration, name="Customer"),

    url(r'login$', CustomAuthToken.as_view(), name="login"),
    url(r'logout$', Logout.as_view(), name='Logout'),
    url(r'updateuser$', views.updateuser, name="updateuser"),
    url(r'edituserbyId$', views.updateAnyUser, name="edituserbyId"),
    url(r'sendotp$', views.sms, name="sendotp"),
    url(r'verifyotp$', views.verifyOtp, name="verifyotp"),

    url(r'userlist$', views.userdataApi, name="userlist"),
    url(r'userlist/([0-9a-zA-Z]+)$', views.userdataApi, name="userlist"),
    url(r'userdelete/([0-9a-zA-Z]+)$', views.userdeleteApi, name="userdelete"),
    url(r'user$', views.ApiusergetList, name="user"),

    url(r'email_otp$', views.email_otp, name="email_otp"),
    url(r'reset_password$', views.resetpassApi, name="reset_password"),
    url(r'forgotpassApi$', views.forgotpassApi, name="forgotpassApi"),

    url(r'wishlist$', views.wishlistApi, name="wishlist"),
    url(r'wishlist/([0-9a-zA-Z]+)$', views.wishlistApi, name="wishlist"),


    url(r'checkout$', views.checkoutApi, name="checkout"),
    url(r'checkout/([0-9a-zA-Z]+)$', views.checkoutApi, name="checkout"),

    url(r'tickets$', views.ticketApi, name="tickets"),
    url(r'tickets/([0-9a-zA-Z]+)$', views.ticketApi, name="tickets"),
    url(r'alltickets$', views.allticket, name="alltickets"),

    url(r'clientslist$', views.clients, name="clientslist"),
    url(r'clientslist/([0-9a-zA-Z]+)$', views.clients, name="clientslist"),

    url(r'transaction$', views.TransactionApi, name="transaction"),
    url(r'alltransactions$', views.allTransactionApi, name="alltransactions"),
    url(r'transaction/([0-9a-zA-Z]+)$', views.TransactionApi, name="transaction"),

    url(r'redeem$', views.RedeemCoinsApi, name="redeem"),
    
    url(r'discount$', org.DiscountView, name="DiscountView"),
    url(r'discount/([0-9a-zA-Z]+)$', org.DiscountView, name="DiscountView"),

    url(r'rateus$', org.orgratsApi, name="rateus"),
    url(r'rateus/([0-9a-zA-Z]+)$', org.orgratsApi, name="rateus"),


    url(r'image_event$', org.eventImage, name="image_event"),
    url(r'video_event$', org.eventVideo, name="video_event"),

    url(r"entertainment$", org.EntertainmentView, name='EntertainmentView'),

    url(r'events/personaldetail$', org.orgEventPersonalDetails, name="orgEventPersonalDetails"),

    url(r'events/companydetail$', org.orgEventCompanyDetails, name="orgEventCompanyDetails"),    
    url(r'events/companydetail/image$', org.orgEventCompanyImage, name="orgEventCompanyImage"),
    url(r'events/companydetail/video$', org.orgEventCompanyVideo, name="orgEventCompanyVideo"),
    
    url(r'events$', org.orgeventApi, name="events"),
    url(r'events/([0-9a-zA-Z]+)$', org.orgeventApi, name="events"),

    url(r'events_get_list$', org.orggeteventApi, name="events_get_list"),
    url(r'events_get_list/([0-9a-zA-Z]+)$', org.orggeteventApi, name="events_get_list"),

    url(r'event/type', org.orgEventTypeView, name="orgEventTypeView"),
    
    url(r'add_place_event$', org.event_place, name="add_place_event"),
    url(r'create_event$', org.craete_event, name="create_event"),
    url(r'create_event/([0-9a-zA-Z]+)$', org.craete_event, name="create_event"),
    url(r'add_place_event/([0-9a-zA-Z]+)$', org.event_place, name="add_place_event"),
    url(r'add_service_event$', org.event_service, name="add_service_event"),
    url(r'add_service_event/([0-9a-zA-Z]+)$', org.event_service, name="add_service_event"),
    url(r'service_list$', org.event_service_list, name="add_service_event"),

    url(r'event_category$', org.EventCategorylist, name="event_category"),
    url(r'event_category_list$', org.Categorylist, name="event_category"),
    url(r'event_category/([0-9a-zA-Z]+)$', org.EventCategorylist, name="event_category"),
    url(r'event_forwho$', org.ForWholist, name="event_forwho"),
    url(r'event_forwho/([0-9a-zA-Z]+)$', org.ForWholist, name="event_forwho"),

    url(r'liveEvent/([0-9a-zA-Z]+)$', org.liveEvent, name="liveEvent"),

    url(r'partnercompany$', org.orgpcompanyApi, name="partnercompany"),
    url(r'partnercompany_get_list$', org.orggetpcompanyApi, name="partnercompany_get_list"),
    url(r'partnercompany_get_list/([0-9a-zA-Z]+)$', org.orggetpcompanyApi, name="partnercompany_get_list"),
    url(r'partnercompany/([0-9a-zA-Z]+)$', org.orgpcompanyApi, name="partnercompany"),
    url(r'pc_equipment$', org.perc_equipment, name="pc_equipment"),
    url(r'pc_artist$', org.perc_artist, name="pc_artist"),
    url(r'pc_decors$', org.perc_decors, name="pc_decors"),
    url(r'pc_photo$', org.pc_photo_add, name="pc_photo"),
    url(r'pc_video$', org.pc_video_add, name="pc_video"),
    url(r'pc_comp_photo$', org.pc_comp_photo_add, name="pc_comp_photo"),
    url(r'pc_comp_video$', org.pc_comp_video_add, name="pc_comp_video"),

    url(r'pc_category$', org.PartnerCompanyCategorylist, name="pc_category"),
    url(r'pc_category/([0-9a-zA-Z]+)$', org.PartnerCompanyCategorylist, name="pc_category"),

    url(r'livePartnerCompanys/([0-9a-zA-Z]+)$', org.livePartnerCompanys, name="livePartnerCompanys"),

    url(r'personalskill$', org.orgpskillApi, name="personalskill"),
    url(r'personalskill_get_list$', org.orggetpskillApi, name="personalskill_get_list"),
    url(r'personalskill_get_list/([0-9a-zA-Z]+)$', org.orggetpskillApi, name="personalskill_get_list"),
    url(r'personalskill/([0-9a-zA-Z]+)$', org.orgpskillApi, name="personalskill"),
    url(r'ps_add_equipment$', org.ps_equipment, name="ps_add_equipment"),
    url(r'ps_add_photo$', org.ps_photos, name="ps_add_photo"),
    url(r'ps_add_video$', org.ps_videos, name="ps_add_video"),
    url(r'ps_add_com_photo$', org.ps_com_photo, name="ps_add_com_photo"),
    url(r'ps_add_com_video$', org.ps_com_video, name="ps_add_com_video"),

    url(r'ps_category$', org.PersonalSkillCategorylist, name="ps_category"),
    url(r'ps_category/([0-9a-zA-Z]+)$', org.PersonalSkillCategorylist, name="ps_category"),
    url(r'ps_sub_category$', org.PersonalSkillSubCategorylist, name="ps_sub_category"),
    url(r'ps_sub_category/([0-9a-zA-Z]+)$', org.PersonalSkillSubCategorylist, name="ps_sub_category"),

    url(r'livePersonalSkill/([0-9a-zA-Z]+)$', org.livePersonalSkill, name="livePersonalSkill"),

    url(r'galleryimage$', org.GalleryImageApi, name="galleryimage"),
    url(r'galleryvideo$', org.GalleryVideoApi, name="galleryvideo"),

    url(r'convert/([0-9]+)$', org.convert, name="convert"),

    url(r'event_place$', org.placeev, name="event_place"),
    url(r'event_place/([0-9]+)$', org.placeev, name="event_place"),

    url(r'chatbot$', views.chatbot, name='chatbot'),

    url(r'pushnotification$', views.pushnotification, name='pushnotification'),

    url(r'notificationdata$', views.NotificationDATA, name='NotificationDATA'),
    url(r'notificationdata/([0-9]+)$', views.NotificationDATA, name='NotificationDATA'),
    url(r'notification$', views.Notifications, name='Notifications'),
    url(r'notification/([0-9]+)$', views.Notifications, name='Notifications'),
    url(r'exceldata$', views.excelusers, name='excelusers'),
    url(r'exceldata/([0-9]+)$', views.excelusers, name='excelusers'),

    url(r'apptoken$', views.AppToken, name='AppToken'),
    url(r'apptoken/([0-9a-zA-Z]+)$', views.AppToken, name='AppToken'),

    url(r'orderidgenerate$', views.OrderIdGenerate, name='OrderIdGenerate'),
    url(r'subscriptionplan$', views.subscriptionplan, name='Subscriptionplan'),
    url(r'subscriptionplan/([0-9a-zA-Z]+)$',
        views.subscriptionplan, name='Subscriptionplan'),

    url(r'usermembership$', views.UserMembership, name='UserMembership'),
    url(r'usermembership/([0-9a-zA-Z]+)$',
        views.UserMembership, name='UserMembership'),

    path('chat/', views.room, name='room'),
    path('evento_privacy_policy/', views.privacy, name='privacy_policy'),

    url(r'advertisement$', views.advertisementapi, name='advertisementapi'),
    url(r'advertisement/([0-9a-zA-Z]+)$', views.advertisementapi, name='advertisementapi'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
