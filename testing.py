
import json
import requests
from backend.TMS_Models.models import *

# url = "http://localhost:8000/tms_api/country/"
# url = "http://localhost:8000/tms_api/state/"
url = "http://localhost:8000/tms_api/city/"
# url = "http://localhost:8000/tms_api/hotel_type_api/"


def get_data(url, id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    response = requests.get(url, data=json_data)
    data = response.json()
    return data


def post_data(url, data):
    json_data = json.dumps(data)
    response = requests.post(url, data=json_data)
    data = response.json()
    return data


if __name__ == "__main__":
    # # countryName = {'CountryName': 'Pakistan'}

    # data = post_data(url, countryName)
    country = Country.objects.get(CountryId=1)
    State = State.objects.filter(CountryId=country)
    City = {'CityName': 'Lahore', 'StateId': State[0].StateId}
    data = post_data(url, City)
    data = get_data(url)
    print(data)
