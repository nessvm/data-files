#!/usr/bin/env python
import sys
from faker import Factory
from collections import OrderedDict
import json


def main():
    n = int(sys.argv[1])
    fake = Factory.create('es_MX')
    data = OrderedDict()
    data['version'] = 1
    data['keys'] = ['address', 'photo']
    data['values'] = list()

    for i in range(n):
        address = {
            'street_address': fake.street_address(),
            'suite': fake.random_int(),
            'colony': fake.city(),
            'municipality': 'Cuauhtémoc',
            'state': 'AGS',
            'postal_code': '00000',
            'latitude': 0.0,
            'longitude': 0.0
        }
        data['values'].append(
            [
                address, fake.image_url()
            ]
        )

    data_file = open("spot_data_{}".format(n), "w")
    data_file.write(json.dumps(data, ensure_ascii=False, indent=4))
    data_file.close()


if __name__ == '__main__':
    main()
