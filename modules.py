import requests
import pandas as pd


class APIRequest:
    def __init__(self, force_values=None):
        self.item_types = ["Currency", "Fragment", "Oil", "Artifact",
                           "DivinationCard", "Essence", "Fossil", "Resonator", "Scarab"]

        self.item_dataframe = pd.DataFrame(columns=['name', 'chaosValue', 'type'])

        for i in self.item_types:
            self.item_dataframe = self.item_dataframe.append(self.get_request(item_type=i))

        if force_values is not None:
            for name, value in force_values.items():
                self.item_dataframe = self.item_dataframe.append(pd.DataFrame({'name': [name],
                                                                               'chaosValue': [value],
                                                                               'type': ['forced']}))

    def get_request(self, item_type, league="Expedition"):
        query_parameters = {'league': league, 'type': item_type}

        if item_type in ["Currency", "Fragment"]:
            response = requests.get("https://poe.ninja/api/data/currencyoverview", params=query_parameters)
            dataframe = pd.DataFrame(response.json()['lines'])[['currencyTypeName', 'chaosEquivalent']]
            dataframe.rename(columns={'currencyTypeName': 'name', 'chaosEquivalent': 'chaosValue'}, inplace=True)

        elif item_type in ["Oil", "Artifact", "DivinationCard", "Essence", "Fossil", "Resonator", "Scarab"]:
            response = requests.get("https://poe.ninja/api/data/itemoverview", params=query_parameters)
            dataframe = pd.DataFrame(response.json()['lines'])[['name', 'chaosValue']]

        else:
            response = requests.get("https://poe.ninja/api/data/itemoverview", params=query_parameters)
            dataframe = pd.DataFrame(response.json()['lines'])

        dataframe['type'] = item_type

        return dataframe


def clipboard_to_item(cb):
    if cb[:11] != "Item Class:":
        return None, None

    cb_list = cb.split("\r\n")
    item_name = cb_list[2]

    item_type = cb_list[1][8:]

    if item_type == "Currency":
        item_stack = int(cb_list[4][12:].split('/')[0].replace(',', ''))
    else:
        item_stack = 1

    return item_name, item_stack


def clipboard_to_item_adv(cb):
    if cb[:11] != "Item Class:":
        return None, None

    cb_list = cb.split("\r\n")

    prefix, suffix = None, None

    for s in cb_list:
        if "Prefix Modifier" in s:
            prefix = s.split('\"')[1].lower()
        elif "Suffix Modifier" in s:
            suffix = s.split('\"')[1].lower()

    return prefix, suffix


