from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index(request):
    return render(request, "index.html")

def getInfo(request):
    wifisList=[{
        "max_channels_count": 40,
        "diap": 2.4,
        "power": 0.7,
        "time": "yesterday when i was young",
        "lat": 40.18,
        "lng": 44.51,
        "ip_addr": "192.168.1.235",
        "mac_addr": "aa:aa:aa:aa:aa",
        "type": "Open"
    },
    {
        "max_channels_count": 40,
        "diap": 2.4,
        "power": 0.7,
        "time": "yesterday when i was young",
        "lat": 40.18,
        "lng": 44.52,
        "ip_addr": "192.168.1.235",
        "mac_addr": "aa:aa:aa:aa:aa",
        "type": "Private"
    }]
    return JsonResponse({"wifi_list":wifisList})
