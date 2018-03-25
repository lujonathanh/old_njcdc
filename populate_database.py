# a file that contains various code snippets for populating the heroku database

import pandas as pd

from zipcode_data.models import Zipcode

data = pd.read_table("data/zip_code_data.txt", dtype=str)

# column names
cols =  ['ZipCode', 'Population', 'PersonsPerHousehold', 'AverageHouseValue',
       'IncomePerHousehold', 'electricity (kWh)', 'Nat. Gas (cu.ft.)',
       'FUELOIL (gallons)', 'Vehicle miles traveled', 'Transport (tCO2e/yr)',
       'Housing (tCO2e/yr)', 'Food (tCO2e/yr)', 'Goods (tCO2e/yr)',
       'Services (tCO2e/yr)', 'Total Household Carbon Footprint (tCO2e/yr)',
       'HouseholdsPerZipCode', 'Total Zip Code Carbon Footprint (tCO2e/yr)']

for i in range(len(data.index)):
    z = Zipcode(zipcode=int(data[cols[0]][i].replace(',', '')),
                population=int(data[cols[1]][i].replace(',', '')),
                persons_per_household=int(data[cols[1]][i].replace(',', '')),
                average_house_value=int(data[cols[1]][i].replace(',', '')),
                income_per_household=int(data[cols[1]][i].replace(',', '')),
                electricity=int(data[cols[1]][i].replace(',', '')),
                nat_gas=int(data[cols[1]][i].replace(',', '')),
                fuel_oil=int(data[cols[1]][i].replace(',', '')),
                vehic_miles_traveled=int(data[cols[1]][i].replace(',', '')),
                transport=int(data[cols[1]][i].replace(',', '')),
                housing=int(data[cols[1]][i].replace(',', '')),
                food=int(data[cols[1]][i].replace(',', '')),
                goods=int(data[cols[1]][i].replace(',', '')),
                services=int(data[cols[1]][i].replace(',', '')),
                total_household_footprint=int(data[cols[1]][i].replace(',', '')),
                households_per_zipcode=int(data[cols[1]][i].replace(',', '')),
                total_zipcode_footprint=int(data[cols[1]][i].replace(',', '')),
                )
    z.save()


z = Zipcode(zipcode=1,
            population=2,
            persons_per_household=3,
            average_house_value=4,
            income_per_household=5,
            electricity=6,
            nat_gas=7,
            fuel_oil=8,
            vehic_miles_traveled=9,
            transport=10,
            housing=11,
            food=12,
            goods=13,
            services=14,
            total_household_footprint=15,
            households_per_zipcode=16,
            total_zipcode_footprint=17,
            )

# Zipcode.objects.get(zipcode=7017)

