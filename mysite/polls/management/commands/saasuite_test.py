import io
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
        data = pkg_resources.resource_filename('polls', 'SAAV_203962_100_500.dat')
        with io.open(data, 'r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                print(row)

        # command = [
        #     "bash",
        #     pkg_resources.resource_filename('polls', 'scripts/run_docker.sh')
        # ]
        # process = subprocess.Popen(
        #     command,
        #     stdin=subprocess.PIPE,
        # )
        print("Hello, Welcome to the Jungle {}".format(name))
        df = pandas.read_csv(data, encoding="utf-8", parse_dates=["timestamp"])
        df = df.rename(columns=lambda x: x.strip().replace("\"", ""))
        df.index = df["timestamp"]

        sensor_x = set(i for i in df.filter(regex="sensor_X"))
        sensor_y = set(i for i in df.filter(regex="sensor_Y"))
        sensor_z = set(i for i in df.filter(regex="sensor_Z"))

        def save_to_db(sensor_no):
            for index, series in df[["record", sensor_no]].iterrows():
                timestamp = index.to_pydatetime()
                print("timestamp:", timestamp, "record:", series.get("record"),
                      "{}: {}".format(sensor_no, series.get(sensor_no)))

        for sensor_no in sensor_x:
            save_to_db(sensor_no)

        for sensor_no in sensor_y:
            save_to_db(sensor_no)

        for sensor_no in sensor_z:
            save_to_db(sensor_no)
