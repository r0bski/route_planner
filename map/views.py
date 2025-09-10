from django.shortcuts import render
from django.http import JsonResponse
from dotenv import load_dotenv
import requests
import os
import json


# Create your views here.
def map_view(request):
    return render(request, "map/planner_map.html")



def get_route(request):
    if request.method == "POST":
        data = json.loads(request.body)
        coords = data.get("coords", [])
        load_dotenv()
        api_key = os.getenv("ORS_API_KEY")
        uri = "https://api.openrouteservice.org/v2/directions/foot-walking/geojson"
        headers = {"Authorization": api_key,"Content-Type": "application/json"}
        payload = {"coordinates": coords}

        r = requests.post(uri, json=payload, headers=headers)
        if r.status_code!=200:
            print(f"Error Code: {r.status_code}, Response: {r.text}")
            return JsonResponse({"error": "Routing failed"}, status=r.status_code)
        return JsonResponse(r.json())

