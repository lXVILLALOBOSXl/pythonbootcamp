import requests
import xml.etree.ElementTree as ET
import json

def get_cars_info(make, model, year):
    url = f"https://www.fueleconomy.gov/ws/rest/vehicle/menu/options?year={year}&make={make}&model={model}"
    response = requests.get(url)
    return response.text

def get_fuel_economy(value):
    url = f"https://www.fueleconomy.gov/ws/rest/vehicle/{value}"
    response = requests.get(url)
    return response.text

def json_cars(xml_data):
    root = ET.fromstring(xml_data)
    menu_items = []
    for menu_item in root.findall('menuItem'):
        model = menu_item.find('text').text
        value = menu_item.find('value').text
        menu_items.append({"value": value, "model": model})
    return json.dumps(menu_items, indent=4)

def xml_to_dict(elem, dict_data=None):
    if dict_data is None:
        dict_data = {}
    for child in list(elem):
        if len(list(child)) > 0:
            xml_to_dict(child, dict_data)
        else:
            dict_data[child.tag] = child.text
    return dict_data

def convert_xml_to_json(xml_data):
    root = ET.fromstring(xml_data)
    data_dict = xml_to_dict(root)
    json_data = json.dumps(data_dict, indent=4)
    return json_data

make = input("Enter car make: ")
model = input("Enter car model: ")
year = input("Enter car year: ")
xml_response = get_cars_info(make, model, year)
json_result = json_cars(xml_response)
print(json_result)
value = input("Enter value: ")
xml_response = get_fuel_economy(value)
json_result = convert_xml_to_json(xml_response)
print(json_result)