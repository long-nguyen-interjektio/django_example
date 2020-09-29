import io
import pprint
import subprocess
import csv

import pandas
import pkg_resources
from django.core.management.base import BaseCommand, CommandError


def column_name(col_name, value):
    return col_name.strip().replace("\"", '').startswith(value)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-n', '--name', type=str, required=True)

    def handle(self, *args, **options):
        name = options.get('name')
        print("Hello, Welcome to the Jungle {}".format(name))

        import pprint
        dataposts = [
            '50044,sn,x,y,z,segT*99905,359080,29658,37124,17535,1883*99905,355859,48189,37593,32858,1909*99905,355860,29565,27952,47992,1870*99905,355861,37555,20850,42100,1864*99905,355862,40119,22059,23714*'
            '50044,sn,x,y,z,segT*99905,356421,48743,29694,33138,1845*99905,356422,27363,33367,47994,1877*99905,356423,31684,45542,41907,1850*99905,356424,23994,42649,23555,1836*99905,356425,37194,31605,17903*'
            '50044,sn,x,y,z,segT*99905,356421,48743,29694,33138,1845*99905,356422,27363,33367,47994,1877*99905,356423,31684,45542,41907,1850*99905,356424,23994,42649,23555,1836*99905,356425,37194,31605,17903*'
            '50044,sn,x,y,z,segT*99905,356673,37100,34653,47784,1837*99905,356674,45607,33816,42048,1833*99905,356675,45618,30536,23520,1842*99905,356676,28426,29899,17581,1853*99905,357249,28673,17161,32851*'
            '50044,sn,x,y,z,segT*99905,357251,20724,25304,41866,1882*99905,357252,43255,40223,23743,1882*99905,357253,33015,37695,17657,1852*99905,357138,34346,16868,32882,1815*99905,357137,29433,28141,47945*'
            '50044,sn,x,y,z,segT*99905,357135,42818,40951,23335,1896*99905,357134,35343,36580,17389,1899*99905,356591,15584,34022,32683,1836*99905,356592,33060,27391,47805,1850*99905,356593,29801,19830,42266*'
            '50044,sn,x,y,z,segT*99905,356595,36470,30793,17196,1874*99905,360123,16101,38552,31339,1866*99905,360124,16101,38552,31339,1866*',
        ]
        parsed = {}
        for post in dataposts:
            rows = post.strip('*').split('*')
            header = rows.pop(0)
            cols = ['timestamp'] + header.split(',')[1:]
            print(rows)
            print("header:", header)
            print(cols)
            for row in rows:
                cells = row.split(',')


                # if len(cells) != len(cols):
                #     raise ValueError('Unexpected row length, does not match column headers')
                row_data = dict(zip(cols, cells))
                parsed[row_data['sn']] = row_data
        pprint.pprint(parsed)
        print(len(parsed))
