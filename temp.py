import datetime
import random

#input_file = 'spis-ulic-w-gdansku.csv'
#output_file = 'ulice.txt'

# Open the input CSV file and the output text file
#with open(input_file, 'r', encoding='utf-8') as input_csv, open(output_file, 'w') as output_txt:
    # Read each line in the CSV file and write the formatted data to the text file
#    for line in input_csv:
#        parts = line.split(';')
#        if len(parts) >= 8:
#            value = parts[7].strip()  # Extract the value and remove leading/trailing spaces
#            output_txt.write(value + '\n')

godziny_zdarzen = []
godzina = random.randint(0, 23)
minuty = random.randint(0, 59)
sekundy = random.randint(0, 59)
losowa_godzina = str(godzina)+':'+str(minuty)+':'+str(sekundy)
godziny_zdarzen.append(losowa_godzina)
print(godziny_zdarzen)