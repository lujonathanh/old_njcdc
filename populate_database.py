import pandas as pd

from calc.models import Zipcode

data = pd.read_table("zip_code_data.txt")

pop = data[' Population ']
miles = data[' Vehicle miles traveled ']

for i in range(len(data.index)):
	z = Zipcode(number=int(pop[i].replace(',', '')), vehicle_miles = int(miles[i].replace(',', '')))
	z.save()