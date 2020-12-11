#import matplotlib
import csv
#import seaborn as sns
#import pandas as pd

def run():
    countries = []
    personal_freedom = []
    with open('hfi_2017.csv') as hfi_file:
        hfi = csv.reader(hfi_file, delimiter = ',')
        line = 0
        for row in hfi:
            if line: #skip if line = 0, execute otherwise
                countries.append(row[2]) #country name
                personal_freedom.append(row[4]) #personal freedom out of 10
            line += 1
            if line == 163:
                break
    
    for index in range(len(personal_freedom)):
        if personal_freedom[index] == '-':
            personal_freedom[index] = 0
        else:
            personal_freedom[index] = float(personal_freedom[index])

    print(countries)
    print(personal_freedom) #tests


    ppm_averages = [0] * len(countries) #parts per million
    with open('covid_data.csv') as covid_file:
        covid = csv.reader(covid_file, delimiter = ',')

        unordered_countries = []
        unordered_ppm = []

        line = 0
        current_country = ''
        ppm_accumulator = 0.0
        for row in covid:
            if line:
                if current_country != row[2]:
                    unordered_countries.append(current_country)
                    unordered_ppm.append(ppm_accumulator/322.0)

                    current_country = row[2]
                    if row[10] == '':
                        ppm_accumulator = 0.0
                    else:
                        ppm_accumulator = float(row[10])
                else:
                    if row[10] != '':
                        ppm_accumulator += float(row[10])
            line += 1
        
        print(unordered_countries)
        print(unordered_ppm)

        ppm = [0]*len(countries)
        for index in range(len(countries)):
            c = countries[index]
            for i in range(len(unordered_countries)):
                if unordered_countries[i] == c:
                    ppm[index] = unordered_ppm[i]


    writee = open('hfi_v_covid.csv', 'w', newline='')
    writer = csv.writer(writee, delimiter = ',')
    writer.writerow(['Country','HFI','PPM'])
    for i in range(len(countries)):
        if ppm[i] != 0:
            information = []
            information.append(countries[i])
            information.append(str(personal_freedom[i]))
            information.append(str(ppm[i]))
            writer.writerow(information)


    

    #sns.set_theme()

    #df = pd.read_csv('hfi_v_covid.csv', sep = ',', header=0)
    #print(df.head())
    #data = sns.load_dataset(df)
    #sns.relplot(data = data)
        



run()