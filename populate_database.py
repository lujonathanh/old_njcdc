import pandas as pd

from zipcode_data.models import Zipcode

data = pd.read_table("data/zip_code_data.txt", dtype=str)

zipcode, pop, p_per_house, aver_house_val, income_per_house, electric, nat_gas, fueloil, \
    miles_traveled, transport, housing, food, goods, services, total_house_footprint, \
    num_houses, total_zip_footprint = pd.read_table("data/zip_code_data.txt", dtype=str)

# column_names =  ['ZipCode', 'Population', 'PersonsPerHousehold', 'AverageHouseValue',
#        'IncomePerHousehold', 'electricity (kWh)', 'Nat. Gas (cu.ft.)',
#        'FUELOIL (gallons)', 'Vehicle miles traveled', 'Transport (tCO2e/yr)',
#        'Housing (tCO2e/yr)', 'Food (tCO2e/yr)', 'Goods (tCO2e/yr)',
#        'Services (tCO2e/yr)', 'Total Household Carbon Footprint (tCO2e/yr)',
#        'HouseholdsPerZipCode', 'Total Zip Code Carbon Footprint (tCO2e/yr)']

miles = data['Vehicle miles traveled']

for i in range(len(data.index)):
    z = Zipcode(number=int(pop[i].replace(',', '')), vehicle_miles = int(miles[i].replace(',', '')))
    z.save()