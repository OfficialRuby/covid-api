from django.core.management.base import BaseCommand
import csv
from api.models import CovidData
from pathlib import Path
import os

BASE_DIR = os.getcwd()


class Command(BaseCommand):
    help = "Load covid-19 data from from csv file(s)"

    def handle(self, *args, **kwargs):
        folder = "csse_covid_19_daily_reports/"
        path = os.path.join(BASE_DIR, folder)

        files = os.listdir(path)
        if files:
            try:
                for item in range(len(files)):
                    self.stdout.write(self.style.WARNING(
                        f"Reading data from {files[item]}: {item+1} out of {len(files)}"))

                    try:
                        with open(path+files[item]) as csv_file:
                            ...
                            csv_reader = csv.reader(csv_file)
                            next(csv_reader)
                            for row in csv_reader:
                                obj, created = CovidData.objects.get_or_create(

                                    fips=row[0],
                                    admin2=row[1],
                                    province_state=row[2],
                                    country_region=row[3],
                                    last_updated=row[4],
                                    lattitude=row[5],
                                    longtitude=row[6],
                                    confirmed_cases=row[7],
                                    deaths=row[8],
                                    recovered=row[9],
                                    active=row[10],
                                    combined_key=row[11],
                                    incident_rate=row[12],
                                    case_fatality_ratio=row[13],

                                )
                            os.remove(path+files[item])
                    except Exception as e:
                        self.stdout.write(self.style.ERROR("Error occured: %s" % e))

                self.stdout.write(self.style.SUCCESS('Data imported successfully'))
            except KeyboardInterrupt:
                self.stdout.write(self.style.ERROR("\n Process terminated by user"))
        else:
            self.stdout.write(self.style.ERROR("Directory is empty"))
