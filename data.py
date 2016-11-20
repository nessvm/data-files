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
    data['variables'] = [OrderedDict(), ]
    data['variables'][0]['names'] = [
        'street_address', 'suite', 'colony', 'photo'
    ]
    data['variables'][0]['values'] = list()

    for i in range(n):
        data['variables'][0]['values'].append(
            [
                fake.street_address(),
                str(fake.random_int()),
                fake.city(),
                fake.image_url()
            ]
        )

    data_file = open("spot_data_{}".format(n), "w")
    data_file.write(json.dumps(data, ensure_ascii=False, indent=4))
    data_file.close()

    data = OrderedDict()
    data['version'] = 1
    data['variables'] = [OrderedDict(), ]
    data['variables'][0]['names'] = [
        'license_plate'
    ]
    data['variables'][0]['values'] = list()

    for i in range(n):
        data['variables'][0]['values'].append(
            [
                fake.bothify(text="???-####").upper()
            ]
        )

    data_file = open("vehicle_data_{}".format(n), "w")
    data_file.write(json.dumps(data, ensure_ascii=False, indent=4))
    data_file.close()


if __name__ == '__main__':
    main()
