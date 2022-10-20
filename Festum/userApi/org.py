from signal import valid_signals
from django.db.models import Q
from requests import delete
from sqlalchemy import true
from yaml import serialize
from userApi.decorater import allowuser
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http.response import JsonResponse
from currency_converter import CurrencyConverter
from userApi.models import *
from userApi.serializers import *
from itertools import chain

# Create your views here.


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
@permission_classes([IsAuthenticated])
def orgEventTypeView(request):
    user = request._user.userId
    id = request.GET.get('id', '')
    if request.method == 'POST':
        vstatus = False
        verror = None
        request.data['user_id'] = user
        serializer = EventTypeSerializers(data=request.data)
        try:
            vstatus = serializer.is_valid(raise_exception=True)
        except Exception as error:
            verror = error
        if vstatus:
            serializer.save()
            discount = Discounts.objects.all()
            for dis in discount:
                OrgDiscounts.objects.create(
                    event_id_id=serializer.data['eventId'], user_id_id=user, discount_type=dis.discount_type, discount=dis.discount)
            return JsonResponse({"status": True, "data": serializer.data}, status=200)
        else:
            return JsonResponse(
                {"status": vstatus,
                 "error": serializer.errors
                 }, status=406)
    if request.method == 'GET':
        if id:
            eventtype = EventType.objects.filter(
                is_active=True, user_id=user, eventId=int(id))
        else:
            eventtype = EventType.objects.filter(is_active=True, user_id=user)
        serialize = EventTypeSerializers(eventtype, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': serialize.data,
            'isSuccess': True
        }, status=200)
    elif request.method == 'PUT':
        request.data['user_id'] = user
        eventtype = EventType.objects.get(eventId=int(id))
        serializer = EventTypeSerializers(eventtype, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': "Updeted Successfully",
                'data': serializer.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Error while updating",
            'data': serializer.errors,
            'isSuccess': False
        }, status=200)
    elif request.method == 'DELETE':
        eventtype = EventType.objects.get(eventId=int(id))
        eventtype.is_active = False
        eventtype.save()
        return JsonResponse({
            'message': "Deleted Successfully",
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def orgratsApi(request, id=0):
    if request.method == 'GET':
        rat = O_Rats.objects.all()
        rats_serializer = O_RatSerializers(rat, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': rats_serializer.data,
            'isSuccess': True
        }, status=200)
    elif request.method == 'POST':
        rat_data = JSONParser().parse(request)
        rats_serializer = O_RatSerializers(data=rat_data)
        if rats_serializer.is_valid():
            rats_serializer.save()
            return JsonResponse({
                'message': "Inserted Successfully",
                'data': rats_serializer.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Insertiong Faild",
            'data': rats_serializer.errors,
            'isSuccess': False
        }, status=200)
    elif request.method == 'PUT':
        rat_data = JSONParser().parse(request)
        rat = O_Rats.objects.get(ratId=rat_data['ratId'])
        rats_serializer = O_RatSerializers(rat, data=rat_data)
        if rats_serializer.is_valid():
            rats_serializer.save()
            return JsonResponse({
                'message': "Updeted Successfully",
                'data': rat_data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Error while updating",
            'data': rats_serializer.errors,
            'isSuccess': False
        }, status=200)
    elif request.method == 'DELETE':
        rat = O_Rats.objects.get(ratId=id)
        rat.delete()
        return JsonResponse({
            'message': "Deleted Successfully",
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Event


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def orggeteventApi(request, id=0):
    if request.method == 'GET':
        if id != 0:
            event = EventType.objects.filter(eventId=id)
            events_serializer = OrgEventTypeSerializers(event, many=True)
        else:
            event = EventType.objects.filter(is_active=True)
            events_serializer = OrgEventTypeSerializers(event, many=True)

            search = request.GET.get('search', "")
            place_name = request.GET.get('place_name', "")
            address = request.GET.get('address', "")
            price = request.GET.get('price', "")
            min_personcapacity = request.GET.get('min_personcapacity', "")
            max_personcapacity = request.GET.get('max_personcapacity', "")

            if search:
                product = EventType.objects.filter(Q(event__place_name__icontains=search) | Q(event__address__icontains=search) |
                                                   Q(category__icontains=search) | Q(display_name__icontains=search) | Q(
                    event__person_capacity__icontains=search)
                    | Q(event__for_who__icontains=search) | Q(event__place_name__icontains=search) | Q(event__place_price__icontains=search) |
                    Q(event__service__service_name__icontains=search) | Q(event__service__service_price__icontains=search) |
                    Q(event__person_capacity__icontains=search) | Q(event__parking_capacity__icontains=search) | Q(event__t_and_c__icontains=search) |
                    Q(event__facebook__icontains=search) | Q(event__youtube__icontains=search) | Q(event__twitter__icontains=search) |
                    Q(event__pinterest__icontains=search) | Q(event__instagram__icontains=search) |
                    Q(event__vimeo__icontains=search) | Q(price__icontains=search))
                events_serializer = OrgEventTypeSerializers(product, many=True)
            else:
                product = EventType.objects.filter(live=True)
                events_serializer = OrgEventTypeSerializers(event, many=True)

            if place_name:
                product = product.filter(
                    Q(event__place_name__icontains=place_name))
                events_serializer = OrgEventTypeSerializers(product, many=True)

            if address:
                product = product.filter(Q(event__address__icontains=address))
                events_serializer = OrgEventTypeSerializers(product, many=True)

            if price:
                p = int(price)
                product = product.filter(price__lte=p)
                events_serializer = OrgEventTypeSerializers(product, many=True)

            if min_personcapacity:
                if max_personcapacity:
                    min = int(min_personcapacity)
                    max = int(max_personcapacity)
                    product = product.filter(
                        event__person_capacity__gte=min, event__person_capacity__lte=max)
                    events_serializer = OrgEventTypeSerializers(
                        product, many=True)

        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': events_serializer.data,
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "This can be access by only GET method",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
@allowuser(allowrole=['0', '1', '2', '3'])
def liveEvent(request, id):
    if request.method == 'POST':
        event = createEvent.objects.filter(eventId=id).first()
        if event:
            event.live = True
            event.save()
        img_event = Image_Event.objects.filter(event=id)
        for img in img_event:
            if img:
                img.live = True
                img.save()
        v_event = Video_Event.objects.filter(event=id)
        for v in v_event:
            if v:
                v.live = True
                v.save()
        return JsonResponse({
            'message': "Event is live",
            'data': 1,
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "This can be access by only Post method",
        'data': '0',
        'isSuccess': False
    }, status=400)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def orgeventApi(request, id=0):
    user = request._user
    if request.method == 'GET':
        user = request._user
        if id != 0:
            event = EventType.objects.filter(
                user_id=user.userId, eventId=id)
            events_serializer = OrgEventTypeSerializers(event, many=True)

            catdata = EventCategory.objects.all()
            cat_serializer = EventCategorySerializers(catdata, many=True)
            cdata = cat_serializer.data
            for i in cdata:
                clue = i['categoryId']

                data = events_serializer.data
                for i in data:
                    catid = i['categoryId']

                    if catid == clue:
                        catdata = EventCategory.objects.filter(
                            categoryId=catid)
                        catserializers = EventCategorySerializers(
                            catdata, many=True)

                        cadata = catserializers.data
                        for j in cadata:
                            category = j["category"]
                        ev = EventType.objects.filter(
                            user_id=user.userId, eventId=id)
                        for e in ev:
                            e.category = category
                            e.save()
                    event = EventType.objects.filter(
                        user_id=user.userId, eventId=id)
                    events_serializer = OrgEventTypeSerializers(
                        event, many=True)

        else:
            event = EventType.objects.filter(user_id=user.userId)
            events_serializer = OrgEventTypeSerializers(event, many=True)

            catdata = EventCategory.objects.all()
            cat_serializer = EventCategorySerializers(catdata, many=True)
            cdata = cat_serializer.data
            for i in cdata:
                clue = i['categoryId']

                data = events_serializer.data
                for i in data:
                    catid = i['categoryId']

                    if catid == clue:
                        catdata = EventCategory.objects.filter(
                            categoryId=catid)
                        catserializers = EventCategorySerializers(
                            catdata, many=True)

                        cadata = catserializers.data
                        for j in cadata:
                            category = j["category"]
                        ev = EventType.objects.filter(
                            user_id=user.userId, categoryId=catid)
                        for e in ev:
                            e.category = category
                            e.save()
                    event = EventType.objects.filter(user_id=user.userId)
                    events_serializer = OrgEventTypeSerializers(
                        event, many=True)

        return JsonResponse({
                            'message': "Data fetch Successfully",
                            'data': events_serializer.data,
                            'isSuccess': True
                            }, status=200)
    elif request.method == 'POST':
        request.data['e_user'] = user.userId
        print('request.data', request.data)
        print('personal data')
        events_serializer = addcreateEventSerializers(data=request.data)
        if events_serializer.is_valid():
            events_serializer.save()
            return JsonResponse({
                'message': "Inserted Successfully",
                'data': events_serializer.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Insertion Faild",
            'data': events_serializer.errors,
            'isSuccess': False
        }, status=200)
    elif request.method == 'PUT':
        event_data = JSONParser().parse(request)
        event = createEvent.objects.get(eventId=event_data['eventId'])
        events_serializer = createEventSerializers(event, data=event_data)
        if events_serializer.is_valid():
            events_serializer.save()
            return JsonResponse({
                'message': "Updeted Successfully",
                'data': event_data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Error while updating",
            'data': events_serializer.errors,
            'isSuccess': False
        }, status=200)
    elif request.method == 'DELETE':
        event = createEvent.objects.get(eventId=id)
        event.delete()
        return JsonResponse({
            'message': "Deleted Successfully",
            'data': "1",
                    'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def orgEventPersonalDetails(request, id=0):
    if request.method == "POST":
        print('call')
        vstatus = False
        verror = None
        serializer = EventPersonalDetailsSerializer(data=request.data)

        try:
            vstatus = serializer.is_valid(raise_exception=True)
        except Exception as error:
            verror = error

        if vstatus:
            serializer.save()
            return JsonResponse({"isSuccess": True, "detail": serializer.data}, status=200)
        else:
            return JsonResponse(
                {"isSuccess": vstatus,
                 "error": str(verror)
                 }, status=200)


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def orgEventCompanyDetails(request, id=0):
    if request.method == "GET":
        print('request.data', request.GET.get('event_reg', 0))
        companydetail = EventCompanyDetails.objects.filter(
            eventId=request.GET.get('eventId', 0))
        serializer = EventCompanyDetailsSerializer(companydetail, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': serializer.data,
            'isSuccess': True
        }, status=200)

    if request.method == "POST":
        vstatus = False
        verror = None
        serializer = EventCompanyDetailsSerializer(data=request.data)

        try:
            vstatus = serializer.is_valid(raise_exception=True)
        except Exception as error:
            verror = error

        if vstatus:
            serializer.save()
            return JsonResponse({'message': "Inserted Successfully", "isSuccess": True, "detail": serializer.data}, status=200)
        else:
            return JsonResponse(
                {"isSuccess": vstatus,
                 "error": str(verror)
                 }, status=200)


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def orgEventCompanyImage(request, id=0):
    if request.method == "POST":
        vstatus = False
        verror = None
        serializer = EventCompanyImageSerializer(data=request.data)

        try:
            vstatus = serializer.is_valid(raise_exception=True)
        except Exception as error:
            verror = error

        if vstatus:
            serializer.save()
            return JsonResponse({'message': "Inserted Successfully", "isSuccess": True, "detail": serializer.data}, status=200)
        else:
            return JsonResponse(
                {"isSuccess": vstatus,
                 "error": str(verror)
                 }, status=200)

    if request.method == "DELETE":

        images = EventCompanyImage.objects.get(
            id=str(request.GET.get('id', 0))
        )

        images.image.delete()
        images.delete()

        return JsonResponse(
            {
                "detail": True,
            },
            status=200
        )


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def orgEventCompanyVideo(request, id=0):
    if request.method == "POST":
        vstatus = False
        verror = None
        serializer = EventCompanyVideoSerializer(data=request.data)

        try:
            vstatus = serializer.is_valid(raise_exception=True)
        except Exception as error:
            verror = error

        if vstatus:
            serializer.save()
            return JsonResponse({'message': "Inserted Successfully", "isSuccess": True, "detail": serializer.data}, status=200)
        else:
            return JsonResponse(
                {"isSuccess": vstatus,
                 "error": str(verror)
                 }, status=200)

    if request.method == "DELETE":

        videos = EventCompanyVideo.objects.get(
            id=str(request.GET.get('id', 0))
        )

        videos.video.delete()
        videos.delete()

        return JsonResponse(
            {
                "detail": True,
            },
            status=200
        )


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def event_place(request, id=0):
    user = request._user.userId
    if request.method == 'GET':
        if id != 0:
            place = Add_Place_ev.objects.filter(Id=id, user_id=user)
        else:
            place = Add_Place_ev.objects.filter(user_id=user)
        places_serializer = addplaceevSerializers(place, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': places_serializer.data,
            'isSuccess': True
        }, status=200)
    elif request.method == 'POST':
        request.data['user_id'] = user
        ev_place_serializer = addplaceevSerializers(data=request.data)
        if ev_place_serializer.is_valid():
            ev_place_serializer.save()
            return JsonResponse({
                'message': "Inserted Successfully",
                'data': ev_place_serializer.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Insertion Faild",
            'data': ev_place_serializer.errors,
            'isSuccess': False
        }, status=200)
    elif request.method == 'PUT':
        request.data['user_id'] = user
        place = Add_Place_ev.objects.get(Id=id, user_id=user)
        serializer = addplaceevSerializers(place, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': "Inserted Successfully",
                'data': serializer.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Insertion Faild",
            'data': ev_place_serializer.errors,
            'isSuccess': False
        }, status=200)
    elif request.method == 'DELETE':
        event = Add_Place_ev.objects.get(Id=id)
        event.is_active = False
        event.save()
        return JsonResponse({
            'message': "Deleted Successfully",
            'data': "1",
                    'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['POST', 'GET', 'PUT'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def event_service(request, id=0):
    user = request._user.userId
    if request.method == 'GET':
        if id != 0:
            service = Add_service_ev.objects.filter(Id=id, user_id=user)
        else:
            service = Add_service_ev.objects.filter(user_id=user)
        services_serializer = addserviceevSerializers(service, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': services_serializer.data,
            'isSuccess': True
        }, status=200)
    elif request.method == 'POST':
        request.data['user'] = user
        ev_service_serializer = addserviceevSerializers(data=request.data)
        if ev_service_serializer.is_valid():
            ev_service_serializer.save()
            return JsonResponse({
                'message': "Inserted Successfully",
                'data': ev_service_serializer.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Insertion Faild",
            'data': ev_service_serializer.errors,
            'isSuccess': False
        }, status=200)
    elif request.method == 'PUT':
        request.data['user'] = user
        service = Add_service_ev.objects.get(Id=id, user_id=user)
        ev_service_serializer = addserviceevSerializers(
            service, data=request.data)
        if ev_service_serializer.is_valid():
            ev_service_serializer.save()
            return JsonResponse({
                'message': "Updated Successfully",
                'data': ev_service_serializer.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Insertion Faild",
            'data': ev_service_serializer.errors,
            'isSuccess': False
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def event_service_list(request, id=0):
    if request.method == 'GET':
        service = Add_service_ev.objects.all()
        services_serializer = addserviceevSerializers(service, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': services_serializer.data,
            'isSuccess': True
        }, status=200)


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def event_service_image(request, id=0):
    user = request._user.userId
    if request.method == 'GET':
        service_id = request.GET.get('service_id')
        if id != 0:
            service = ServiceImage.objects.filter(
                id=id, service_id=int(service_id))
        else:
            service = ServiceImage.objects.filter(service_id=int(service_id))
        services_serializer = addserviceimageSerializers(service, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': services_serializer.data,
            'isSuccess': True
        }, status=200)
    if request.method == 'POST':
        services_serializer = addserviceimageSerializers(data=request.data)
        if services_serializer.is_valid():
            services_serializer.save()
            return JsonResponse({
                'message': "Inserted Successfully",
                'data': services_serializer.data,
                'isSuccess': True
            }, status=200)


def placedelete(id=0):
    places = Servic.objects.filter(event=id)
    places.delete()



@api_view(['GET', 'PUT', 'POST', 'DELETE'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def OrgDiscountView(request, id=0):
    if request.method == 'GET':
        print('if call')
        user = request._user.userId
        if id != 0:
            discount = OrgDiscounts.objects.filter(
                id=id, user_id=user, event_id=int(request.GET.get('event_id')))
        else:
            discount = OrgDiscounts.objects.filter(user_id=user, event_id=int(request.GET.get('event_id')))
        discount_serializer = OrgDiscountSerializers(discount, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': discount_serializer.data,
            'isSuccess': True
        }, status=200)

    # def post(self, request):
    #     vstatus = False
    #     verror = None
    #     _id = request.data['orgequipmentdiscounts_id']
    #     exist = OrgEquipment.objects.get(orgequipmentdiscounts_id=_id)
    #     if exist:
    #         serializer = OrgEquipmentSerializers(exist, data=request.data)
    #     else:
    #         serializer = OrgEquipmentSerializers(data=request.data)

    #     try:
    #         vstatus = serializer.is_valid(raise_exception=True)
    #     except Exception as error:
    #         verror = error

    #     if vstatus:
    #         model_obj = serializer.save()
    #         return Response({"status": True, "detail": serializer.data}, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(
    #             {"status": vstatus,
    #              #  "error": str(verror)
    #              "error": serializer.errors
    #              }, status=status.HTTP_406_NOT_ACCEPTABLE)

    if request.method == "PUT":       
        user = request._user.userId
        odiscount = OrgDiscounts.objects.get(id=id, event_id=int(request.GET.get('event_id')), user_id=user)            
        odiscount.equipment_id_id = request.data['equipment_id']
        odiscount.discount = request.data['discount']
        if odiscount:
            odiscount.save()
            discount_serializer = OrgDiscountSerializers(odiscount)
            if (request.data['equipment_id'] != None or '') and (odiscount.discount_type == 'discount_on_equipment_or_item'):
                u = OrgEquipmentId.objects.filter(orgdiscount_id__user_id=user)
                u.delete()
                for i in request.data['equipment_id']:
                    OrgEquipmentId.objects.update_or_create(orgdiscount_id_id=discount_serializer.data['id'], equipment_id_id=i)
                serializer = OrgDiscountSerializers(odiscount)
                return JsonResponse({
                    'message': "Updated Successfully",
                    'data': serializer.data,
                    'isSuccess': True
                }, status=200)
            return JsonResponse({
                    'message': "Updated Successfully",
                    'data': discount_serializer.data,
                    'isSuccess': True
                }, status=200)
        return JsonResponse({
            'message': "Insertion Faild",
            'data': discount_serializer.errors,
            'isSuccess': False
        }, status=200)




@api_view(['GET', 'PUT', 'POST', 'DELETE'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def DiscountView(request, id=0):
    if request.method == 'GET':
        print('req get', request.data)
        if id != 0:
            discount = Discounts.objects.filter(discountsId=id)
        else:
            discount = Discounts.objects.all()
        discount_serializer = DiscountSerializers(discount, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully.",
            'data': discount_serializer.data,
            'isSuccess': True
        }, status=200)

    elif request.method == 'POST':
        print('req post', request.data)
        vstatus = False
        verror = None
        serializer = DiscountSerializers(data=request.data)

        try:
            vstatus = serializer.is_valid(raise_exception=True)
        except Exception as error:
            verror = error

        if vstatus:
            model_obj = serializer.save()
            return JsonResponse({"isSuccess": True, "data": serializer.data}, status=201)
        else:
            return JsonResponse({
                 "message": "Insertion Faild",
                 "data": serializer.errors,
                "isSuccess": vstatus
                 }, status=406)

    elif request.method == 'PUT':
        discount = Discounts.objects.get(discountsId=id)
        discount_serializer = DiscountSerializers(discount, data=request.data)
        if discount_serializer.is_valid():
            discount_serializer.save()
            return JsonResponse({
                'message': "Updated Successfully",
                'data': discount_serializer.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Insertion Faild",
            'data': discount_serializer.errors,
            'isSuccess': False
        }, status=200)

    elif request.method == 'DELETE':
        eventtype = Discounts.objects.get(discountsId=id)
        eventtype.delete()
        eventtype.save()
        return JsonResponse({
            'message': "Deleted Successfully",
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


# @api_view(['GET', 'PUT'])
# @allowuser(allowrole=['0', '1', '2', '3', '4'])
# def DiscountView(request, id=0):
#     user = request._user.userId
#     if request.method == 'GET':
#         discount = Discounts.objects.all()
#         discount_serializer = DiscountSerializers(discount, many=True)
#         return JsonResponse({
#             'message': "Data fetch Successfully",
#             'data': discount_serializer.data,
#             'isSuccess': True
#         }, status=200)
#     elif request.method == 'PUT':
#         try:
#             discountID = OrgDiscounts.objects.filter(orgdiscount_id=id).get()
#         except:
#             discountID = Discounts.objects.filter(discountsId=id).get()

#         # request.data['orgdiscount_id'] = id
#         # request.data['orguser'] = user
#         discount_per = request.data['orgdiscount']
#         equipment_id = request.data['orgequipment_id']
#         description = request.data['orgdescription']

#         print('request.data', request.data)
#         OrgDiscounts.objects.create(orgdiscount=discount_per, orgdescription=description,
#                                     orgequipment_id=equipment_id, orguser_id=user, orgdiscount_id_id=discountID, is_active=True)
#         # discount_serializer = OrgDiscountSerializers(discountID, data=request.data)
#         if discount_serializer.is_valid():
#             discount_serializer.save()
#             return JsonResponse({
#                 'message': "Updated Successfully",
#                 'data': discount_serializer.data,
#                 'isSuccess': True
#             }, status=200)
#         return JsonResponse({
#             'message': "Insertion Faild",
#             'data': discount_serializer.errors,
#             'isSuccess': False
#         }, status=200)
#     return JsonResponse({
#         'message': "Connection error",
#         'data': '0',
#         'isSuccess': False
#     }, status=400)


@api_view(['POST', 'GET', 'DELETE'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def placeev(request, id=0):
    if request.method == 'GET':
        places = Servic.objects.all()
        place_serializer = ServicSerializers(places, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': place_serializer.data,
            'isSuccess': True
        }, status=200)
    elif request.method == 'DELETE':
        places = Servic.objects.filter(event=id)
        places.delete()
        return JsonResponse({
            'message': "Deleted Successfully",
            'data': "1",
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def craete_event(request, id=0):
    if request.method == 'GET':
        create = Place_Events.objects.all()
        creates_serializer = Place_EventSerializers(create, many=True)
        for i in creates_serializer.data:
            for_who_Id = i['for_who_Id']
            event = i['event']
            place_id = i["place_Id"]
            service = i['service']
            place_price = i['place_price']

            tp = 0
            for s in service:
                s_price = s["service_price"]
                tp += s_price
            price = int(place_price) + int(tp)
            fp = createEvent.objects.filter(eventId=event)
            for f in fp:
                f.price = price
                f.save()

            forwho = ForWho.objects.filter(Id=for_who_Id)
            forwho_serializer = ForWhoSerializers(forwho, many=True)
            fwdata = forwho_serializer.data
            for i in fwdata:
                plan_name = i['plan_name']
                ev = Place_Events.objects.filter(event=event)
                for e in ev:
                    e.for_who = plan_name
                    e.save()

            # Make one for place
            places = Add_Place_ev.objects.filter(Id=place_id)
            places_serializer = addplaceevSerializers(places, many=True)
            placesdata = places_serializer.data
            for k in placesdata:
                place_name = k['place_name']
                place_price = k['place_price']
                ev = Place_Events.objects.filter(event=event)
                for e in ev:
                    e.place_name = place_name
                    e.place_price = place_price
                    e.save()

        create = Place_Events.objects.all()
        creates_serializer = Place_EventSerializers(create, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': creates_serializer.data,
            'isSuccess': True
        }, status=200)
    elif request.method == 'POST':
        create = JSONParser().parse(request)
        eveId = create["event"]
        even = create["service_Id"]
        check = Place_Events.objects.filter(event=eveId)
        if check:
            return JsonResponse({
                'message': "Event already exists",
                'data': 1,
                'isSuccess': True
            }, status=200)
        else:
            create_serializer = Place_EventSerializers(data=create)
            if create_serializer.is_valid():
                create_serializer.save()
                eventId = create_serializer.data["id"]

                for i in even:
                    places = Add_service_ev.objects.filter(Id=i)
                    place_serializer = addserviceevSerializers(
                        places, many=True)
                    placedata = place_serializer.data
                    for data in placedata:

                        placed = {
                            "s_id": data['Id'],
                            "event": eventId,
                            "service_name": data['service_name'],
                            "service_price": data['service_price'],
                        }
                        place_serializer = ServicSerializers(data=placed)
                        if place_serializer.is_valid():
                            place_serializer.save()

                return JsonResponse({
                    'message': "Inserted Successfully",
                    'data': create_serializer.data,
                    'isSuccess': True
                }, status=200)
            return JsonResponse({
                'message': "Insertion Faild",
                'data': create_serializer.errors,
                'isSuccess': False
            }, status=200)

    elif request.method == 'PUT':
        event_data = JSONParser().parse(request)
        even = event_data["service_Id"]
        event = Place_Events.objects.get(event=event_data['event'])
        events_serializer = Place_EventSerializers(event, data=event_data)
        if events_serializer.is_valid():
            events_serializer.save()
            eventId = events_serializer.data["id"]
            placedelete(eventId)

            for i in even:
                places = Add_service_ev.objects.filter(Id=i)
                place_serializer = addserviceevSerializers(places, many=True)
                placedata = place_serializer.data
                for data in placedata:
                    placed = {
                        "s_id": data['Id'],
                        "event": eventId,
                        "service_name": data['service_name'],
                        "service_price": data['service_price'],
                    }

                    service_serializer = ServicSerializers(data=placed)
                    if service_serializer.is_valid():
                        service_serializer.save()

            return JsonResponse({
                'message': "Updeted Successfully",
                'data': events_serializer.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Error while updating",
            'data': events_serializer.errors,
            'isSuccess': False
        }, status=200)

    elif request.method == 'DELETE':
        event = Place_Events.objects.get(event=id)
        event.delete()
        return JsonResponse({
            'message': "Deleted Successfully",
            'data': "1",
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['POST', 'GET'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def eventImage(request):
    if request.method == 'GET':
        img = Image_Event.objects.filter(
            event_id=request.GET.get('eventId', 0))
        imgs_serializer = eventimageSerializers(img, many=True)

        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': imgs_serializer.data,
            'isSuccess': True
        }, status=200)

    elif request.method == 'POST':
        vstatus = False
        verror = None
        serializer = eventimageSerializers(data=request.data)

        try:
            vstatus = serializer.is_valid(raise_exception=True)
        except Exception as error:
            verror = error

        if vstatus:
            serializer.save()
            return JsonResponse({"status": True, "detail": serializer.data}, status=200)
        else:
            return JsonResponse(
                {"status": vstatus,
                 "error": str(verror)
                 }, status=400)


@api_view(['POST', 'GET'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def eventVideo(request):
    if request.method == 'GET':
        vid = Video_Event.objects.filter(
            event_id=request.GET.get('eventId', 0))
        vids_serializer = eventvideoSerializers(vid, many=True)
        return JsonResponse({
            'message': "video fetch Successfully",
            'data': vids_serializer.data,
            'isSuccess': True
        }, status=200)

    elif request.method == 'POST':
        vstatus = False
        verror = None
        serializer = eventvideoSerializers(data=request.data)

        try:
            vstatus = serializer.is_valid(raise_exception=True)
        except Exception as error:
            verror = error

        if vstatus:
            serializer.save()
            return JsonResponse({"status": True, "detail": serializer.data}, status=200)
        else:
            return JsonResponse(
                {"status": vstatus,
                 "error": str(verror)
                 }, status=400)


@api_view(['POST', 'GET'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def EntertainmentView(request):
    if request.method == 'GET':
        entertaimentImage = Image_Event.objects.all().order_by('-timestamp')
        image = eventimageSerializers(entertaimentImage, many=True)
        entertaimentVideo = Video_Event.objects.all().order_by('-timestamp')
        video = eventvideoSerializers(entertaimentVideo, many=True)
        data = list(chain(image.data, video.data))

        return JsonResponse({"status": True, "detail": data}, status=200)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ personal Skill
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def orggetpskillApi(request, id=0):
    if request.method == 'GET':

        getter = request.user
        fetch = User.objects.filter(email=getter)
        serialize = RegistrationSerializer(fetch, many=True)
        getId = serialize.data
        for gid in getId:
            g = gid['userId']

        if id != 0:
            pskill = O_PersonalSkills.objects.filter(perskillId=id)
            pskills_serializer = O_PersonalskillSerializers(pskill, many=True)

            d = pskills_serializer.data
            for data in d:
                # id = data['perskillId']
                u = data['PersonalSkillWishlist']
                newVar = False
                if u != []:
                    for ids in u:
                        i = ids["personalId"]
                        if g == ids['user']:
                            newVar = True
                    persSkill = O_PersonalSkills.objects.filter(perskillId=i)
                    if persSkill:
                        if newVar:
                            for ev in persSkill:
                                ev.whishlist_status = True
                                ev.save()
                        else:
                            for item in persSkill:
                                item.whishlist_status = False
                                item.save()
                else:
                    persSkill = O_PersonalSkills.objects.filter(
                        PersonalSkillWishlist=None)
                    for i in persSkill:
                        i.whishlist_status = False
                        i.save()

            pskill = O_PersonalSkills.objects.filter(perskillId=id)
            pskills_serializer = O_PersonalskillSerializers(pskill, many=True)

        else:
            pskill = O_PersonalSkills.objects.all()
            pskills_serializer = O_PersonalskillSerializers(pskill, many=True)

            d = pskills_serializer.data
            for data in d:
                # id = data['perskillId']
                u = data['PersonalSkillWishlist']
                newVar = False
                if u != []:
                    for ids in u:
                        i = ids["personalId"]
                        if g == ids['user']:
                            newVar = True
                    persSkill = O_PersonalSkills.objects.filter(perskillId=i)
                    if persSkill:
                        if newVar:
                            for ev in persSkill:
                                ev.whishlist_status = True
                                ev.save()
                        else:
                            for item in persSkill:
                                item.whishlist_status = False
                                item.save()
                else:
                    persSkill = O_PersonalSkills.objects.filter(
                        PersonalSkillWishlist=None)
                    for i in persSkill:
                        i.whishlist_status = False
                        i.save()

            pskill = O_PersonalSkills.objects.all()
            pskills_serializer = O_PersonalskillSerializers(pskill, many=True)

            search = request.GET.get('search', "")

            if search:
                product = O_PersonalSkills.objects.filter(Q(pro_category__icontains=search) | Q(profession__icontains=search)
                                                          | Q(name__icontains=search) | Q(mobile_no__icontains=search) | Q(alt_mobile_no__icontains=search)
                                                          | Q(email__icontains=search) | Q(work_price__icontains=search) | Q(work_discount__icontains=search)
                                                          | Q(travel_cost__icontains=search) | Q(accommodation__icontains=search) | Q(food__icontains=search)
                                                          | Q(Equipment__equpment__icontains=search) | Q(Equipment__equpment_price__icontains=search) | Q(Equipment__equpment_price_period__icontains=search)
                                                          | Q(Equipment__equpment_details__icontains=search) | Q(com_name__icontains=search) | Q(com_contact__icontains=search)
                                                          | Q(com_email__icontains=search) | Q(com_address__icontains=search) | Q(price__icontains=search) | Q(facebook__icontains=search)
                                                          | Q(youtube__icontains=search) | Q(twitter__icontains=search) | Q(pinterest__icontains=search) | Q(instagram__icontains=search) | Q(vimeo__icontains=search))
                pskills_serializer = O_PersonalskillSerializers(
                    product, many=True)
            else:
                product = O_PersonalSkills.objects.all()
                pskills_serializer = O_PersonalskillSerializers(
                    product, many=True)

        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': pskills_serializer.data,
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "This can be access by only GET method",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def livePersonalSkill(request, id):
    if request.method == 'POST':
        PersonalSkill = O_PersonalSkills.objects.filter(perskillId=id).first()
        if PersonalSkill:
            PersonalSkill.live = True
            PersonalSkill.save()
        img_PersonalSkill = ps_photo.objects.filter(p_skill=id)
        for img in img_PersonalSkill:
            if img:
                img.live = True
                img.save()
        v_PersonalSkill = ps_video.objects.filter(p_skill=id)
        for v in v_PersonalSkill:
            if v:
                v.live = True
                v.save()
        imgc_PersonalSkill = ps_companyphotos.objects.filter(p_skill=id)
        for imgc in imgc_PersonalSkill:
            if imgc:
                imgc.live = True
                imgc.save()
        vc_PersonalSkill = ps_companyvideos.objects.filter(p_skill=id)
        for vc in vc_PersonalSkill:
            if vc:
                vc.live = True
                vc.save()
        return JsonResponse({
            'message': "PersonalSkill is live",
            'data': 1,
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "This can be access by only Post method",
        'data': '0',
        'isSuccess': False
    }, status=400)


# #######################################################
def EqupmentPSdelete(id=0):
    places = equipments_pskill.objects.filter(pskillid=id)
    places.delete()


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def orgpskillApi(request, id=0):
    if request.method == 'GET':
        user = request.user
        pskill = O_PersonalSkills.objects.filter(User=user)
        pskills_serializer = O_PersonalskillSerializers(pskill, many=True)

        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': pskills_serializer.data,
            'isSuccess': True
        }, status=200)
    elif request.method == 'POST':
        pskills_serializer = O_PersonalskillSerializers(data=request.data)
        pskill = O_PersonalSkills.objects.filter(User=request.data["User"])
        # print("--->", type(pskill))
        if pskill:
            return JsonResponse({
                'message': "You alredy submited one form",
                'data': 1,
                'isSuccess': True
            }, status=200)
        else:
            if pskills_serializer.is_valid():
                pskills_serializer.save()
                for i in str(pskills_serializer.data["equip_ids"]).split(","):
                    eqpms = ps_equipments.objects.filter(Id=int(i))
                    # print("---0", eqpms)
                    eqpms_serializer = addequipmentpsSerializers(
                        eqpms, many=True)
                    eqpmsdata = eqpms_serializer.data
                    for data in eqpmsdata:
                        eqpment = {
                            "equpmentId": data["Id"],
                            "pskillid": pskills_serializer.data["perskillId"],
                            "equpment": data["equ_name"],
                            "equpment_price": data["equ_price"],
                            "equpment_price_period": data["equ_price_period"],
                            "equpment_price_type": data["equ_price_type"],
                            "equpment_details": data["equ_details"]
                        }
                        place_serializer = equipments_pskillSerializers(
                            data=eqpment)
                        if place_serializer.is_valid():
                            place_serializer.save()

                subcat = PersonalSkillSubCategory.objects.get(
                    Id=pskills_serializer.data["profession"])
                subcat_data = PersonalSkillSubCategorySerializers(subcat)

                category = PersonalSkillCategory.objects.get(
                    Id=pskills_serializer.data["pro_category"])
                category_data = PersonalSkillCategorySerializers(category)

                pskill_cat = O_PersonalSkills.objects.filter(
                    perskillId=pskills_serializer.data["perskillId"])
                for pskilldata in pskill_cat:
                    pskilldata.pro_category_id = category_data.data["Id"]
                    pskilldata.pro_category = category_data.data["category"]
                    pskilldata.profession_id = subcat_data.data["Id"]
                    pskilldata.profession = subcat_data.data["category"]
                    pskilldata.save()

                return JsonResponse({
                    'message': "Inserted Successfully",
                    'data': pskills_serializer.data,
                    'isSuccess': True
                }, status=200)
            return JsonResponse({
                'message': "Insertion Faild",
                'data': pskills_serializer.errors,
                'isSuccess': False
            }, status=200)

    elif request.method == 'PUT':
        # pskill_data = JSONParser().parse(request)
        pskill_data = request.data['User']
        pskill = O_PersonalSkills.objects.get(User=pskill_data)
        pskills_serializer = O_PersonalskillSerializers(
            pskill, data=request.data)
        if pskills_serializer.is_valid():
            pskills_serializer.save()

            psId = pskills_serializer.data["perskillId"]
            EqupmentPSdelete(psId)

            for i in str(pskills_serializer.data["equip_ids"]).split(","):
                eqpms = ps_equipments.objects.filter(Id=int(i))
                print("---0", eqpms)
                eqpms_serializer = addequipmentpsSerializers(eqpms, many=True)
                eqpmsdata = eqpms_serializer.data
                for data in eqpmsdata:
                    eqpment = {
                        "equpmentId": data["Id"],
                        "pskillid": pskills_serializer.data["perskillId"],
                        "equpment": data["equ_name"],
                        "equpment_price": data["equ_price"],
                        "equpment_price_period": data["equ_price_period"],
                        "equpment_price_type": data["equ_price_type"],
                        "equpment_details": data["equ_details"]
                    }
                    place_serializer = equipments_pskillSerializers(
                        data=eqpment)
                    if place_serializer.is_valid():
                        place_serializer.save()

            subcat = PersonalSkillSubCategory.objects.get(
                Id=pskills_serializer.data["profession"])
            subcat_data = PersonalSkillSubCategorySerializers(subcat)

            category = PersonalSkillCategory.objects.get(
                Id=pskills_serializer.data["pro_category"])
            category_data = PersonalSkillCategorySerializers(category)

            pskill_cat = O_PersonalSkills.objects.filter(
                perskillId=pskills_serializer.data["perskillId"])
            for pskilldata in pskill_cat:
                pskilldata.pro_category_id = category_data.data["Id"]
                pskilldata.pro_category = category_data.data["category"]
                pskilldata.profession_id = subcat_data.data["Id"]
                pskilldata.profession = subcat_data.data["category"]
                pskilldata.save()

            pskill = O_PersonalSkills.objects.filter(
                perskillId=pskills_serializer.data["perskillId"])
            pskills_serializer = O_PersonalskillSerializers(pskill, many=True)

            return JsonResponse({
                'message': "Updeted Successfully",
                'data': pskills_serializer.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Error while updating",
            'data': pskills_serializer.errors,
            'isSuccess': False
        }, status=200)
    elif request.method == 'DELETE':
        pskill = O_PersonalSkills.objects.get(perskillId=id)
        pskill.delete()
        return JsonResponse({
            'message': "Deleted Successfully",
            'data': "1",
                    'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['POST', 'GET'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def ps_equipment(request):
    if request.method == 'GET':
        user = request.user
        equp = ps_equipments.objects.filter(user=user)
        equps_serializer = addequipmentpsSerializers(equp, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': equps_serializer.data,
            'isSuccess': True
        }, status=200)
    elif request.method == 'POST':
        equp = JSONParser().parse(request)
        equp_serializer = addequipmentpsSerializers(data=equp)
        if equp_serializer.is_valid():
            equp_serializer.save()
            return JsonResponse({
                'message': "Inserted Successfully",
                'data': equp_serializer.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Insertion Faild",
            'data': equp_serializer.errors,
            'isSuccess': False
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['POST', 'GET'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def ps_photos(request):
    if request.method == 'GET':
        img = ps_photo.objects.all()
        imgs_serializer = addphotopsSerializers(img, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': imgs_serializer.data,
            'isSuccess': True
        }, status=200)
    elif request.method == 'POST':
        files = request.data
        p_skill = files['p_skill']
        photo_price_period = files['photo_price_period']
        photo_details = files['photo_details']

        img = ps_photo.objects.filter(p_skill=files['p_skill'])
        imgs_serializer = addphotopsSerializers(img, many=True)
        total_img = 20 - len(imgs_serializer.data)
        if len(imgs_serializer.data) < 20:
            if len(request.FILES.getlist('photo_file')) <= total_img:
                for i in request.FILES.getlist('photo_file'):
                    img_serializer = addphotopsSerializers(
                        data={'p_skill': p_skill, 'photo_price_period': photo_price_period, 'photo_details': photo_details, 'photo_file': i})
                    if img_serializer.is_valid():
                        img_serializer.save()
                return JsonResponse({
                    'message': "Inserted Successfully",
                    'data': "1",
                    'isSuccess': True
                }, status=200)
            else:
                return JsonResponse({
                    'message': "You can upload maximum " + str(total_img) + " photos, "+"You alredy uploaded " + str(len(imgs_serializer.data)) + " photos",
                    'data': "0",
                    'isSuccess': True
                }, status=200)
        else:
            return JsonResponse({
                'message': "You alredy uploaded " + str(len(imgs_serializer.data)) + " photos",
                'data': "0",
                'isSuccess': True
            }, status=200)

    return JsonResponse({
        'message': "Insertion Faild",
        'data': 0,
        'isSuccess': False
    }, status=400)


@api_view(['POST', 'GET'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def ps_videos(request):
    if request.method == 'GET':
        video = ps_video.objects.all()
        videos_serializer = addvideopsSerializers(video, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': videos_serializer.data,
            'isSuccess': True
        }, status=200)
    elif request.method == 'POST':
        files = request.data
        p_skill = files['p_skill']

        video = ps_video.objects.filter(p_skill=files['p_skill'])
        videos_serializer = addvideopsSerializers(video, many=True)
        # print("------------->", len(videos_serializer.data))
        total_vido = 20 - len(videos_serializer.data)
        # print("++++++++++++++++++++++++", total_vido)
        if len(videos_serializer.data) < 20:
            if len(request.FILES.getlist('video_file')) <= total_vido:
                for i in request.FILES.getlist('video_file'):
                    video_serializer = addvideopsSerializers(
                        data={'p_skill': p_skill, 'video_file': i})
                    if video_serializer.is_valid():
                        video_serializer.save()
                return JsonResponse({
                                    'message': "You have successfully uploaded videos",
                                    'data': "1",
                                    'isSuccess': True
                                    }, status=200)
            else:
                return JsonResponse({
                    'message': "You can upload maximum " + str(total_vido) + " videos, "+"You alredy uploaded " + str(len(videos_serializer.data)) + " Videos",
                    'data': "0",
                    'isSuccess': True
                }, status=200)
        else:
            return JsonResponse({
                'message': "You alredy uploaded " + str(len(videos_serializer.data)) + " Videos",
                'data': "0",
                'isSuccess': True
            }, status=200)

    return JsonResponse({
        'message': "Insertion Faild",
        'data': 0,
        'isSuccess': False
    }, status=400)


@api_view(['POST', 'GET'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def ps_com_photo(request):
    if request.method == 'GET':
        img = ps_companyphotos.objects.all()
        imgs_serializer = companyphotopsSerializers(img, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': imgs_serializer.data,
            'isSuccess': True
        }, status=200)
    elif request.method == 'POST':
        files = request.data
        p_skill = files['p_skill']
        img = ps_companyphotos.objects.filter(p_skill=files['p_skill'])
        imgs_serializer = companyphotopsSerializers(img, many=True)
        # print("------------->",len(imgs_serializer.data))
        total_img = 20 - len(imgs_serializer.data)
        # print("++++++++++++++++++++++++", total_img)
        if len(imgs_serializer.data) < 20:
            if len(request.FILES.getlist('c_photo_file')) <= total_img:
                for i in request.FILES.getlist('c_photo_file'):
                    img_serializer = companyphotopsSerializers(
                        data={'p_skill': p_skill, 'c_photo_file': i})
                    if img_serializer.is_valid():
                        img_serializer.save()
                return JsonResponse({
                                    'message': "Inserted Successfully",
                                    'data': 1,
                                    'isSuccess': True
                                    }, status=200)
            else:
                return JsonResponse({
                    'message': "You can upload maximum " + str(total_img) + " photos, "+"You alredy uploaded " + str(len(imgs_serializer.data)) + " photos",
                    'data': "0",
                    'isSuccess': True
                }, status=200)
        else:
            return JsonResponse({
                'message': "You alredy uploaded " + str(len(imgs_serializer.data)) + " photos",
                'data': "0",
                'isSuccess': True
            }, status=200)
    return JsonResponse({
        'message': "Insertion Faild",
        'data': 0,
        'isSuccess': False
    }, status=400)


@api_view(['POST', 'GET'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def ps_com_video(request):
    if request.method == 'GET':
        video = ps_companyvideos.objects.all()
        videos_serializer = companyvideopsSerializers(video, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': videos_serializer.data,
            'isSuccess': True
        }, status=200)
    elif request.method == 'POST':
        files = request.data
        p_skill = files['p_skill']
        imgs = request.FILES.getlist('c_video_file')
        video = ps_companyvideos.objects.filter(p_skill=files['p_skill'])
        videos_serializer = companyvideopsSerializers(video, many=True)
        # print("--------------------->", len(videos_serializer.data))
        total_vid = 20 - len(videos_serializer.data)
        # print("++++++++++++++++++++++++", total_vid)
        if len(videos_serializer.data) < 20:
            if len(imgs) <= total_vid:
                for a in imgs:
                    video_serializer = companyvideopsSerializers(
                        data={'p_skill': p_skill, 'c_video_file': a}
                    )
                    if video_serializer.is_valid():
                        video_serializer.save()
                return JsonResponse({
                                    'message': "Inserted Successfully",
                                    'data': 1,
                                    'isSuccess': True
                                    }, status=200)
            else:
                return JsonResponse({
                    'message': "You can upload maximum " + str(total_vid) + " videos, "+"You alredy uploaded " + str(len(videos_serializer.data)) + " videos",
                    'data': "0",
                    'isSuccess': True
                }, status=200)
        else:
            return JsonResponse({
                'message': "You alredy uploaded " + str(len(videos_serializer.data)) + " videos",
                'data': "0",
                'isSuccess': True
            }, status=200)
    return JsonResponse({
        'message': "Insertion faild",
        'data': 0,
        'isSuccess': False
    }, status=400)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Partner companys

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def orggetpcompanyApi(request, id=0):
    if request.method == 'GET':

        getter = request.user
        fetch = User.objects.filter(email=getter)
        serialize = RegistrationSerializer(fetch, many=True)
        getId = serialize.data
        for gid in getId:
            g = gid['userId']

        if id != 0:
            pcompany = O_PartnerCompanys.objects.filter(parcomId=id)
            pcompanys_serializer = O_PartnercompanySerializers(
                pcompany, many=True)

            d = pcompanys_serializer.data
            for data in d:
                u = data['PartnerCompWishlist']
                newVar = False
                if u != []:
                    for ids in u:
                        i = ids["partnerId"]
                        if g == ids['user']:
                            newVar = True

                    PartnerCompany = O_PartnerCompanys.objects.filter(
                        parcomId=i)
                    if PartnerCompany:
                        if newVar:
                            for ev in PartnerCompany:
                                ev.whishlist_status = True
                                ev.save()

                        else:
                            for item in PartnerCompany:
                                item.whishlist_status = False
                                item.save()
                else:
                    PartnerCompany = O_PartnerCompanys.objects.filter(
                        PartnerCompWishlist=None)
                    for i in PartnerCompany:
                        i.whishlist_status = False
                        i.save()

            pcompany = O_PartnerCompanys.objects.filter(parcomId=id)
            pcompanys_serializer = O_PartnercompanySerializers(
                pcompany, many=True)

        else:

            pcompany = O_PartnerCompanys.objects.all()
            pcompanys_serializer = O_PartnercompanySerializers(
                pcompany, many=True)

            d = pcompanys_serializer.data
            for data in d:
                u = data['PartnerCompWishlist']
                newVar = False
                if u != []:
                    for ids in u:
                        i = ids["partnerId"]
                        if g == ids['user']:
                            newVar = True

                    PartnerCompany = O_PartnerCompanys.objects.filter(
                        parcomId=i)
                    if PartnerCompany:
                        if newVar:
                            for ev in PartnerCompany:
                                ev.whishlist_status = True
                                ev.save()

                        else:
                            for item in PartnerCompany:
                                item.whishlist_status = False
                                item.save()
                else:
                    PartnerCompany = O_PartnerCompanys.objects.filter(
                        PartnerCompWishlist=None)
                    for i in PartnerCompany:
                        i.whishlist_status = False
                        i.save()

            pcompany = O_PartnerCompanys.objects.all()
            pcompanys_serializer = O_PartnercompanySerializers(
                pcompany, many=True)

            search = request.GET.get('search', "")

            if search:
                product = O_PartnerCompanys.objects.filter(
                    Q(category__icontains=search) | Q(name__icontains=search) |
                    Q(mobile_no__icontains=search) | Q(alt_mobile_no__icontains=search) |
                    Q(email_id__icontains=search) | Q(Equipments__equpment__icontains=search) |
                    Q(Equipments__equpment_price__icontains=search) | Q(Equipments__equpment_price_period__icontains=search) |
                    Q(Equipments__equpment_details__icontains=search) | Q(artist__icontains=search) |
                    Q(artist_price__icontains=search) | Q(decor__icontains=search) |
                    Q(decor_price__icontains=search) | Q(w_price__icontains=search) |
                    Q(w_discount__icontains=search) | Q(travel_cost__icontains=search) |
                    Q(accommodation__icontains=search) | Q(food__icontains=search) |
                    Q(com_name__icontains=search) | Q(com_contact__icontains=search) |
                    Q(com_email__icontains=search) | Q(com_address__icontains=search) |
                    Q(price__icontains=search) | Q(facebook__icontains=search) |
                    Q(youtube__icontains=search) | Q(twitter__icontains=search) |
                    Q(pinterest__icontains=search) | Q(instagram__icontains=search) |
                    Q(vimeo__icontains=search)
                )
                pcompanys_serializer = O_PartnercompanySerializers(
                    product, many=True)
            else:
                product = O_PartnerCompanys.objects.all()
                pcompanys_serializer = O_PartnercompanySerializers(
                    product, many=True)

        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': pcompanys_serializer.data,
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "This can be access by only GET method",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def livePartnerCompanys(request, id):
    if request.method == 'POST':
        PartnerCompanys = O_PartnerCompanys.objects.filter(parcomId=id).first()
        if PartnerCompanys:
            PartnerCompanys.live = True
            PartnerCompanys.save()
        img_PartnerCompanys = pc_photos.objects.filter(pc=id)
        for img in img_PartnerCompanys:
            if img:
                img.live = True
                img.save()
        imgc_PartnerCompanys = pc_companyphotos.objects.filter(pc=id)
        for imgc in imgc_PartnerCompanys:
            if imgc:
                imgc.live = True
                imgc.save()
        v_PartnerCompanys = pc_videos.objects.filter(pc=id)
        for v in v_PartnerCompanys:
            if v:
                v.live = True
                v.save()
        vc_PartnerCompanys = pc_companyvideos.objects.filter(pc=id)
        for vc in vc_PartnerCompanys:
            if vc:
                vc.live = True
                vc.save()
        return JsonResponse({
            'message': "PartnerCompanys is live",
            'data': 1,
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "This can be access by only Post method",
        'data': '0',
        'isSuccess': False
    }, status=400)


# #######################################################
def EqupmentPCdelete(id=0):
    places = equipments_pc.objects.filter(pcid=id)
    places.delete()


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def orgpcompanyApi(request, id=0):
    if request.method == 'GET':
        user = request.user
        pcompany = O_PartnerCompanys.objects.filter(User=user)
        pcompanys_serializer = O_PartnercompanySerializers(pcompany, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': pcompanys_serializer.data,
            'isSuccess': True
        }, status=200)
    elif request.method == 'POST':
        pcompanys_serializer = O_PartnercompanySerializers(data=request.data)
        pcompany = O_PartnerCompanys.objects.filter(User=request.data["User"])
        if pcompany:
            return JsonResponse({
                'message': "You alredy submited one form",
                'data': 1,
                'isSuccess': True
            }, status=200)

        else:
            if pcompanys_serializer.is_valid():
                pcompanys_serializer.save()

                for i in str(pcompanys_serializer.data["equip_ids"]).split(","):
                    eqpms = pc_equipments.objects.filter(Id=int(i))
                    eqpms_serializer = pc_equipmentSerializers(
                        eqpms, many=True)
                    eqpmsdata = eqpms_serializer.data
                    for data in eqpmsdata:
                        eqpment = {
                            "equpmentId": data["Id"],
                            "pcid": pcompanys_serializer.data["parcomId"],
                            "equpment": data["equ_name"],
                            "equpment_price": data["equ_price"],
                            "equpment_price_period": data["equ_price_period"],
                            "equpment_price_type": data["equ_price_type"],
                            "equpment_details": data["equ_details"]
                        }
                        place_serializer = EquipmentsPcSerializers(
                            data=eqpment)
                        if place_serializer.is_valid():
                            place_serializer.save()

                cat = PartnerCompanyCategory.objects.get(
                    Id=pcompanys_serializer.data['categoryId'])
                cat_data = PartnerCompanyCategorySerializers(cat)

                pcom_cat = O_PartnerCompanys.objects.filter(
                    parcomId=pcompanys_serializer.data["parcomId"])
                for data in pcom_cat:
                    data.category = cat_data.data["category"]
                    data.save()

                return JsonResponse({
                    'message': "Inserted Successfully",
                    'data': pcompanys_serializer.data,
                    'isSuccess': True
                }, status=200)
            return JsonResponse({
                'message': "Insertion Faild",
                'data': pcompanys_serializer.errors,
                'isSuccess': False
            }, status=200)
    elif request.method == 'PUT':
        pcompany_data = request.data["User"]
        pcompany = O_PartnerCompanys.objects.get(
            User=pcompany_data)
        pcompanys_serializer = O_PartnercompanySerializers(
            pcompany, data=request.data)
        if pcompanys_serializer.is_valid():
            pcompanys_serializer.save()

            pcId = pcompanys_serializer.data["parcomId"]
            EqupmentPCdelete(pcId)

            for i in str(pcompanys_serializer.data["equip_ids"]).split(","):
                eqpms = pc_equipments.objects.filter(Id=int(i))
                eqpms_serializer = pc_equipmentSerializers(eqpms, many=True)
                eqpmsdata = eqpms_serializer.data
                for data in eqpmsdata:
                    eqpment = {
                        "equpmentId": data["Id"],
                        "pcid": pcompanys_serializer.data["parcomId"],
                        "equpment": data["equ_name"],
                        "equpment_price": data["equ_price"],
                        "equpment_price_period": data["equ_price_period"],
                        "equpment_price_type": data["equ_price_type"],
                        "equpment_details": data["equ_details"]
                    }
                    place_serializer = EquipmentsPcSerializers(data=eqpment)
                    if place_serializer.is_valid():
                        place_serializer.save()

            cat = PartnerCompanyCategory.objects.get(
                Id=pcompanys_serializer.data['categoryId'])
            cat_data = PartnerCompanyCategorySerializers(cat)

            pcom_cat = O_PartnerCompanys.objects.filter(
                parcomId=pcompanys_serializer.data["parcomId"])
            for data in pcom_cat:
                data.category = cat_data.data["category"]
                data.save()

            pcompany = O_PartnerCompanys.objects.filter(
                parcomId=pcompanys_serializer.data["parcomId"])
            pcompanys_serializer = O_PartnercompanySerializers(
                pcompany, many=True)

            return JsonResponse({
                'message': "Updeted Successfully",
                'data': pcompanys_serializer.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Error while updating",
            'data': pcompanys_serializer.errors,
            'isSuccess': False
        }, status=200)
    elif request.method == 'DELETE':
        pcompany = O_PartnerCompanys.objects.get(parcomId=id)
        pcompany.delete()
        return JsonResponse({
            'message': "Deleted Successfully",
            'data': "1",
                    'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['POST', 'GET'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def perc_equipment(request):
    if request.method == 'GET':
        equip = pc_equipments.objects.all()
        equips_serializer = pc_equipmentSerializers(equip, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': equips_serializer.data,
            'isSuccess': True
        }, status=200)
    elif request.method == 'POST':
        equip = JSONParser().parse(request)
        equip_serializer = pc_equipmentSerializers(data=equip)
        if equip_serializer.is_valid():
            equip_serializer.save()
            return JsonResponse({
                'message': "Inserted Successfully",
                'data': equip_serializer.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Insertion Faild",
            'data': equip_serializer.errors,
            'isSuccess': False
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['POST', 'GET'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def perc_artist(request):
    if request.method == 'GET':
        artist = pc_artist.objects.all()
        artists_serializer = pc_artistSerializers(artist, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': artists_serializer.data,
            'isSuccess': True
        }, status=200)
    elif request.method == 'POST':
        artist = JSONParser().parse(request)
        artist_serializer = pc_artistSerializers(data=artist)
        if artist_serializer.is_valid():
            artist_serializer.save()
            return JsonResponse({
                'message': "Inserted Successfully",
                'data': artist_serializer.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Insertion Faild",
            'data': artist_serializer.errors,
            'isSuccess': False
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['POST', 'GET'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def perc_decors(request):
    if request.method == 'GET':
        decor = pc_decor.objects.all()
        decors_serializer = pc_decorSerializers(decor, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': decors_serializer.data,
            'isSuccess': True
        }, status=200)
    elif request.method == 'POST':
        decor = JSONParser().parse(request)
        decor_serializer = pc_decorSerializers(data=decor)
        if decor_serializer.is_valid():
            decor_serializer.save()
            return JsonResponse({
                'message': "Inserted Successfully",
                'data': decor_serializer.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Insertion Faild",
            'data': decor_serializer.errors,
            'isSuccess': False
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['POST', 'GET'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def pc_photo_add(request):
    if request.method == 'GET':
        img = pc_photos.objects.all()
        imgs_serializer = pc_photosSerializers(img, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': imgs_serializer.data,
            'isSuccess': True
        }, status=200)
    elif request.method == 'POST':
        files = request.data
        pc = files['pc']

        img = pc_photos.objects.filter(pc=files['pc'])
        imgs_serializer = pc_photosSerializers(img, many=True)
        # print("----------------->", len(imgs_serializer.data))
        total_img = 20 - len(imgs_serializer.data)
        # print("----------------->", total_img)
        if len(imgs_serializer.data) < 20:
            if len(request.FILES.getlist('photo_file')) <= total_img:
                for i in request.FILES.getlist('photo_file'):
                    img_serializer = pc_photosSerializers(
                        data={'pc': pc, 'photo_file': i})
                    if img_serializer.is_valid():
                        img_serializer.save()
                return JsonResponse({
                    'message': "Photos are successfully uploaded",
                    'data': "1",
                    'isSuccess': True
                }, status=200)
            else:
                return JsonResponse({
                    'message': "You can upload maximum " + str(total_img) + " photos, "+"You alredy uploaded " + str(len(imgs_serializer.data)) + " photos",
                    'data': "0",
                    'isSuccess': True
                }, status=200)
        else:
            return JsonResponse({
                'message': "You alredy uploaded " + str(len(imgs_serializer.data)) + " photos",
                'data': "0",
                'isSuccess': True
            }, status=200)
    return JsonResponse({
        'message': "Insertion Faild",
        'data': 0,
        'isSuccess': False
    }, status=400)


@api_view(['POST', 'GET'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def pc_video_add(request):
    if request.method == 'GET':
        video = pc_videos.objects.all()
        videos_serializer = pc_videosSerializers(video, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': videos_serializer.data,
            'isSuccess': True
        }, status=200)
    elif request.method == 'POST':
        files = request.data
        pc = files['pc']
        video = pc_videos.objects.filter(pc=files['pc'])
        videos_serializer = pc_videosSerializers(video, many=True)
        # print("________________________________!>",len(videos_serializer.data))
        total_vid = 20 - len(videos_serializer.data)
        # print("----------------->", total_vid)
        if len(videos_serializer.data) < 20:
            if len(request.FILES.getlist('video_file')) <= total_vid:
                for i in request.FILES.getlist('video_file'):
                    video_serializer = pc_videosSerializers(
                        data={'pc': pc, 'video_file': i})
                    if video_serializer.is_valid():
                        video_serializer.save()
                return JsonResponse({
                    'message': "Videos are successfully uploaded",
                    'data': "1",
                    'isSuccess': True
                }, status=200)
            else:
                return JsonResponse({
                    'message': "You can upload maximum " + str(total_vid) + " videos, "+"You alredy uploaded " + str(len(videos_serializer.data)) + " videos",
                    'data': "0",
                    'isSuccess': True
                }, status=200)
        else:
            return JsonResponse({
                'message': "You alredy uploaded " + str(len(videos_serializer.data)) + " videos",
                'data': "0",
                'isSuccess': True
            }, status=200)

    return JsonResponse({
        'message': "Insertion Faild",
        'data': 0,
        'isSuccess': False
    }, status=400)


@api_view(['POST', 'GET'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def pc_comp_photo_add(request):
    if request.method == 'GET':
        img = pc_companyphotos.objects.all()
        imgs_serializer = pc_companyphotosSerializers(img, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': imgs_serializer.data,
            'isSuccess': True
        }, status=200)
    elif request.method == 'POST':
        files = request.data
        pc = files['pc']
        img = pc_companyphotos.objects.filter(pc=files['pc'])
        imgs_serializer = pc_companyphotosSerializers(img, many=True)
        # print("____________________________________>", len(imgs_serializer.data))
        total_img = 20 - len(imgs_serializer.data)
        # print("----------------->", total_img)
        if len(imgs_serializer.data) < 20:
            if len(request.FILES.getlist('c_photo_file')) <= total_img:
                for i in request.FILES.getlist('c_photo_file'):
                    img_serializer = pc_companyphotosSerializers(
                        data={'pc': pc, 'c_photo_file': i})
                    if img_serializer.is_valid():
                        img_serializer.save()
                return JsonResponse({
                    'message': "Photos are successfully uploaded",
                    'data': "1",
                    'isSuccess': True
                }, status=200)
            else:
                return JsonResponse({
                    'message': "You can upload maximum " + str(total_img) + " photos, "+"You alredy uploaded " + str(len(imgs_serializer.data)) + " photos",
                    'data': "0",
                    'isSuccess': True
                }, status=200)
        else:
            return JsonResponse({
                'message': "You alredy uploaded " + str(len(imgs_serializer.data)) + " photos",
                'data': "0",
                'isSuccess': True
            }, status=200)

    return JsonResponse({
        'message': "Insertion Faild",
        'data': 0,
        'isSuccess': False
    }, status=400)


@api_view(['POST', 'GET'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def pc_comp_video_add(request):
    if request.method == 'GET':
        video = pc_companyvideos.objects.all()
        videos_serializer = pc_companyvideosSerializers(video, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': videos_serializer.data,
            'isSuccess': True
        }, status=200)
    elif request.method == 'POST':
        files = request.data
        pc = files['pc']
        video = pc_companyvideos.objects.filter(pc=files['pc'])
        videos_serializer = pc_companyvideosSerializers(video, many=True)
        # print("_______________________________@", len(videos_serializer.data))
        total_vid = 20 - len(videos_serializer.data)
        # print("----------------->", total_vid)
        if len(videos_serializer.data) < 20:
            if len(request.FILES.getlist('c_video_file')) <= total_vid:
                for i in request.FILES.getlist('c_video_file'):
                    video_serializer = pc_companyvideosSerializers(
                        data={'pc': pc, 'c_video_file': i})
                    if video_serializer.is_valid():
                        video_serializer.save()
                return JsonResponse({
                    'message': "Inserted Successfully",
                    'data': "1",
                            'isSuccess': True
                }, status=200)
            else:
                return JsonResponse({
                    'message': "You can upload maximum " + str(total_vid) + " videos, "+"You alredy uploaded " + str(len(videos_serializer.data)) + " videos",
                    'data': "0",
                    'isSuccess': True
                }, status=200)
        else:
            return JsonResponse({
                'message': "You alredy uploaded " + str(len(videos_serializer.data)) + " videos",
                'data': "0",
                'isSuccess': True
            }, status=200)
    return JsonResponse({
        'message': "Insertion Faild",
        'data': 0,
        'isSuccess': False
    }, status=400)


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def EventCategorylist(request, id=0):
    user = request._user.userId
    if request.method == 'GET':
        if id != 0:
            eventcategory = EventCategory.objects.filter(
                categoryId=id, user_id=user, is_active=True)
        else:
            eventcategory = EventCategory.objects.filter(
                user_id=user, is_active=True)
        eventcategorylist = EventCategorySerializers(eventcategory, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': eventcategorylist.data,
            'isSuccess': True
        }, status=200)
    elif request.method == 'POST':
        request.data['user'] = user
        print('request.data', request.data)
        categorySerializers = EventCategorySerializers(data=request.data)
        if categorySerializers.is_valid():
            categorySerializers.save()
            return JsonResponse({
                'message': "Inserted Successfully",
                'data': categorySerializers.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Insertion Faild",
            'data': categorySerializers.errors,
            'isSuccess': False
        }, status=200)
    elif request.method == 'PUT':
        request.data['user'] = user
        try:
            evc = EventCategory.objects.get(
                categoryId=id, user_id=user, is_active=True)
            evcserializers = EventCategorySerializers(evc, data=request.data)
            if evcserializers.is_valid(raise_exception=True):
                evcserializers.save()
                return JsonResponse({
                    'message': "Updeted Successfully",
                    'data': evcserializers.data,
                    'isSuccess': True
                }, status=200)
        except:
            return JsonResponse({
                'message': "Error while updating",
                'data': 0,
                'isSuccess': False
            }, status=200)

    elif request.method == 'DELETE':
        try:
            category = EventCategory.objects.get(
                categoryId=id, user_id=user, is_active=True)
            category.is_active = False
            category.save()
            return JsonResponse({
                'message': "Deleted Successfully",
                'data': "1",
                'isSuccess': True
            }, status=200)
        except:
            return JsonResponse({
                'message': "Connection error",
                'data': '0',
                'isSuccess': False
            }, status=400)


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def Categorylist(request, id=0):
    if request.method == 'GET':
        user = request._user
        eventcategory = EventCategory.objects.filter(is_active=True)
        eventcategorylist = EventCategorySerializers(eventcategory, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': eventcategorylist.data,
            'isSuccess': True
        }, status=200)


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def ForWholist(request, id=0):
    if request.method == 'GET':
        id = int(id)
        if id == 1:
            # print("-------------", type(id))
            forwho = ForWho.objects.filter(for_who=id)
            forwholist = ForWhoSerializers(forwho, many=True)

        elif id == 2:
            # print("-------------", type(id))
            forwho = ForWho.objects.filter(for_who=id)
            forwholist = ForWhoSerializers(forwho, many=True)

        else:
            # print("-------------", type(id))
            forwho = ForWho.objects.all()
            forwholist = ForWhoSerializers(forwho, many=True)

        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': forwholist.data,
            'isSuccess': True
        }, status=200)

    elif request.method == 'POST':
        forwhodata = JSONParser().parse(request)
        forwhoSerializers = ForWhoSerializers(data=forwhodata)
        if forwhoSerializers.is_valid():
            forwhoSerializers.save()
            return JsonResponse({
                'message': "Inserted Successfully",
                'data': forwhoSerializers.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Insertion Faild",
            'data': forwhoSerializers.errors,
            'isSuccess': False
        }, status=200)
    elif request.method == 'PUT':

        fw_data = JSONParser().parse(request)
        fw = ForWho.objects.get(Id=fw_data['Id'])
        fwserializers = ForWhoSerializers(fw, data=fw_data)
        if fwserializers.is_valid():
            fwserializers.save()
            return JsonResponse({
                'message': "Updeted Successfully",
                'data': fwserializers.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Error while updating",
            'data': fwserializers.errors,
            'isSuccess': False
        }, status=200)

    elif request.method == 'DELETE':
        forwho = ForWho.objects.get(Id=id)
        forwho.delete()
        return JsonResponse({
            'message': "Deleted Successfully",
            'data': "1",
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def PersonalSkillCategorylist(request, id=0):
    if request.method == 'GET':
        if id != 0:
            pscategory = PersonalSkillCategory.objects.filter(Id=id)
            pscategorylist = PersonalSkillCategorySerializers(
                pscategory, many=True)
        else:
            pscategory = PersonalSkillCategory.objects.all()
            pscategorylist = PersonalSkillCategorySerializers(
                pscategory, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': pscategorylist.data,
            'isSuccess': True
        }, status=200)
    elif request.method == 'POST':
        pscategorydata = JSONParser().parse(request)
        pscategorySerializers = PersonalSkillCategorySerializers(
            data=pscategorydata)
        if pscategorySerializers.is_valid():
            pscategorySerializers.save()
            return JsonResponse({
                'message': "Inserted Successfully",
                'data': pscategorySerializers.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Insertion Faild",
            'data': pscategorySerializers.errors,
            'isSuccess': False
        }, status=200)

    elif request.method == 'PUT':
        psc_data = JSONParser().parse(request)
        psc = PersonalSkillCategory.objects.get(Id=psc_data['Id'])
        pscserializers = PersonalSkillCategorySerializers(psc, data=psc_data)
        if pscserializers.is_valid():
            pscserializers.save()
            return JsonResponse({
                'message': "Updeted Successfully",
                'data': pscserializers.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Error while updating",
            'data': pscserializers.errors,
            'isSuccess': False
        }, status=200)

    elif request.method == 'DELETE':
        pscategory = PersonalSkillCategory.objects.get(Id=id)
        pscategory.delete()
        return JsonResponse({
            'message': "Deleted Successfully",
            'data': "1",
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def PersonalSkillSubCategorylist(request, id=0):
    if request.method == 'GET':
        if id != 0:
            pssubcategory = PersonalSkillSubCategory.objects.filter(
                pscategoryid=id)
            pssubcategorylist = PersonalSkillSubCategorySerializers(
                pssubcategory, many=True)
        else:
            pssubcategory = PersonalSkillSubCategory.objects.all()
            pssubcategorylist = PersonalSkillSubCategorySerializers(
                pssubcategory, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': pssubcategorylist.data,
            'isSuccess': True
        }, status=200)
    elif request.method == 'POST':
        pssubcategorydata = JSONParser().parse(request)
        pssubcategorySerializers = PersonalSkillSubCategorySerializers(
            data=pssubcategorydata)
        if pssubcategorySerializers.is_valid():
            pssubcategorySerializers.save()
            return JsonResponse({
                'message': "Inserted Successfully",
                'data': pssubcategorySerializers.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Insertion Faild",
            'data': pssubcategorySerializers.errors,
            'isSuccess': False
        }, status=200)
    elif request.method == 'PUT':

        pssc_data = JSONParser().parse(request)
        pssc = PersonalSkillSubCategory.objects.get(Id=pssc_data['Id'])
        psscserializers = PersonalSkillSubCategorySerializers(
            pssc, data=pssc_data)
        if psscserializers.is_valid():
            psscserializers.save()
            return JsonResponse({
                'message': "Updeted Successfully",
                'data': psscserializers.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Error while updating",
            'data': psscserializers.errors,
            'isSuccess': False
        }, status=200)

    elif request.method == 'DELETE':
        pssubcategory = PersonalSkillSubCategory.objects.get(Id=id)
        pssubcategory.delete()
        return JsonResponse({
            'message': "Deleted Successfully",
            'data': "1",
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@allowuser(allowrole=['0', '1', '2', '3', '4'])
def PartnerCompanyCategorylist(request, id=0):
    if request.method == 'GET':
        pccategory = PartnerCompanyCategory.objects.all()
        pccategorylist = PartnerCompanyCategorySerializers(
            pccategory, many=True)
        return JsonResponse({
            'message': "Data fetch Successfully",
            'data': pccategorylist.data,
            'isSuccess': True
        }, status=200)
    elif request.method == 'POST':
        pccategorydata = JSONParser().parse(request)
        pccategorySerializers = PartnerCompanyCategorySerializers(
            data=pccategorydata)
        if pccategorySerializers.is_valid():
            pccategorySerializers.save()
            return JsonResponse({
                'message': "Inserted Successfully",
                'data': pccategorySerializers.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Insertion Faild",
            'data': pccategorySerializers.errors,
            'isSuccess': False
        }, status=200)
    elif request.method == 'PUT':

        pcc_data = JSONParser().parse(request)
        pcc = PartnerCompanyCategory.objects.get(Id=pcc_data['Id'])
        pccserializers = PartnerCompanyCategorySerializers(pcc, data=pcc_data)
        if pccserializers.is_valid():
            pccserializers.save()
            return JsonResponse({
                'message': "Updeted Successfully",
                'data': pccserializers.data,
                'isSuccess': True
            }, status=200)
        return JsonResponse({
            'message': "Error while updating",
            'data': pccserializers.errors,
            'isSuccess': False
        }, status=200)

    elif request.method == 'DELETE':
        pccategory = PartnerCompanyCategory.objects.get(Id=id)
        pccategory.delete()
        return JsonResponse({
            'message': "Deleted Successfully",
            'data': "1",
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def GalleryImageApi(request):
    if request.method == 'GET':
        img1 = Image_Event.objects.all()
        imgs_serializer1 = eventimageSerializers(img1, many=True)

        img2 = pc_photos.objects.all()
        imgs_serializer2 = pc_photosSerializers(img2, many=True)

        img3 = pc_companyphotos.objects.all()
        imgs_serializer3 = pc_companyphotosSerializers(img3, many=True)

        img4 = ps_photo.objects.all()
        imgs_serializer4 = addphotopsSerializers(img4, many=True)

        img5 = ps_companyphotos.objects.all()
        imgs_serializer5 = companyphotopsSerializers(img5, many=True)
        return JsonResponse({
            'message': "Image fetch Successfully",
            'data': imgs_serializer1.data +
            imgs_serializer2.data +
            imgs_serializer3.data +
            imgs_serializer4.data +
            imgs_serializer5.data,
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def GalleryVideoApi(request):
    if request.method == 'GET':
        vid1 = Video_Event.objects.all()
        vids_serializer1 = eventvideoSerializers(vid1, many=True)

        vid2 = pc_videos.objects.all()
        vids_serializer2 = pc_videosSerializers(vid2, many=True)

        vid3 = pc_companyvideos.objects.all()
        vids_serializer3 = pc_companyvideosSerializers(vid3, many=True)

        vid4 = ps_video.objects.all()
        vids_serializer4 = addvideopsSerializers(vid4, many=True)

        vid5 = ps_companyvideos.objects.all()
        vids_serializer5 = companyvideopsSerializers(vid5, many=True)
        return JsonResponse({
            'message': "Video fetch Successfully",
            'data': vids_serializer1.data +
            vids_serializer2.data +
            vids_serializer3.data +
            vids_serializer4.data +
            vids_serializer5.data,
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def convert(request, price=0):
    if request.method == 'GET':
        c = CurrencyConverter()
        usd = c.convert(price, 'INR', 'USD')
        thb = c.convert(price, 'INR', 'THB')
        cny = c.convert(price, 'INR', 'CNY')
        eur = c.convert(price, 'INR', 'EUR')
        return JsonResponse({
            'message': "Converted successfully",
            'data': {"usd": usd, "thb": thb, "cny": cny, "eur": eur},
            'isSuccess': True
        }, status=200)
    return JsonResponse({
        'message': "Connection error",
        'data': '0',
        'isSuccess': False
    }, status=400)
