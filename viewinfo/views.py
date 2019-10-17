from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from viewinfo.models import WifiDatabase
from viewinfo.client_server.server import Constants


def index(request):
    return render(request, "index.html")


# def getInfo(request):
#     wifis_list=[{
#         "max_channels_count": 40,
#         "diap": 2.4,
#         "power": 0.7,
#         "time": "yesterday when i was young",
#         "lat": 40.18,
#         "lng": 44.51,
#         "ip_addr": "192.168.1.235",
#         "mac_addr": "aa:aa:aa:aa:aa",
#         "type": "Open"
#     },
#     {
#         "max_channels_count": 40,
#         "diap": 2.4,
#         "power": 0.7,
#         "time": "yesterday when i was young",
#         "lat": 40.18,
#         "lng": 44.52,
#         "ip_addr": "192.168.1.235",
#         "mac_addr": "aa:aa:aa:aa:aa",
#         "type": "Private"
#     }]
#     return JsonResponse({"wifi_list": wifis_list})


def get_wifis(request):
    wifis = WifiDatabase.objects.all()
    all_wifis = []
    for wifi in wifis:
        conf = {Constants.LATITUDE: wifi.latitude,
                Constants.LONGITUDE: wifi.longitude,
                Constants.TIME: wifi.time,
                Constants.TYPE: wifi.type,
                Constants.DIAP: wifi.diap,
                Constants.CHANNELS: wifi.channels,
                Constants.MAC: wifi.mac,
                Constants.IP: wifi.ip,
                Constants.POWER: wifi.power}
        all_wifis.append(conf)
    return JsonResponse({"wifi_list": all_wifis})
