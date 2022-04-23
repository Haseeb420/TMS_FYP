import json
import requests
# url = "http://localhost:8000/tms_api/country/"
url = "http://localhost:8000/tms_api/state/"
# url = "http://localhost:8000/tms_api/city/"


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
    State = {'StateName': 'Lahore', 'CountryId': 1}
    City = {'CityName': 'Lahore', 'StateId': 1}
    # data = post_data(url, State)
    data = get_data(url)
    print(data)
