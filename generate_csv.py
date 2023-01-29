import csv
import random

with open('dist.csv', 'w', newline='') as S:
    csv_output = csv.writer(S)

    for i in range(200):
        numbers = random.randint(0, 100)
        csv_output.writerow([numbers])