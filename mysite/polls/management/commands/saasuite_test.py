import io
import subprocess

import pkg_resources
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-n', '--name', type=str, required=True)

    def handle(self, *args, **options):
        name = options.get('name')
        data = pkg_resources.resource_filename('polls', 'SAAV_203962_100_500.dat')
        with io.open(data, 'r', encoding='utf-8') as f_data:
            set_data = set(i for i in f_data)
        print(len(data))
        print(len(set_data))
        # command = [
        #     "bash",
        #     pkg_resources.resource_filename('polls', 'scripts/run_docker.sh')
        # ]
        # process = subprocess.Popen(
        #     command,
        #     stdin=subprocess.PIPE,
        # )
        print("Hello, Welcome to the Jungle {}".format(name))
        #
        # process.stdin.close()
        # process.wait()
