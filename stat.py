#import matplotlib
import csv
#import seaborn as sns
#import pandas as pd
import numpy as np

# Python code to sort the tuples using second element  
# of sublist Inplace way to sort using sort() 
def Sort(sub_li): 
  
    # reverse = None (Sorts in Ascending order) 
    # key is set to sort using second element of  
    # sublist lambda has been used 
    sub_li.sort(key = lambda x: x[1]) 
    return sub_li 

def run_hfi():
    countries = []
    human_freedom = []
    with open('hfi_2017.csv') as hfi_file:
        hfi = csv.reader(hfi_file, delimiter = ',')
        line = 0
        for row in hfi:
            if line: #skip if line = 0, execute otherwise
                countries.append(row[2]) #country name
                human_freedom.append(row[4]) #human freedom out of 10
            line += 1
            if line == 163:
                break
    
    for index in range(len(human_freedom)):
        if human_freedom[index] == '-':
            human_freedom[index] = 0
        else:
            human_freedom[index] = float(human_freedom[index])

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
            information.append(str(human_freedom[i]))
            information.append(str(ppm[i]))
            writer.writerow(information)


def run_pfi():
    countries = []
    personal_freedom = []
    with open('hfi_2017.csv') as hfi_file:
        hfi = csv.reader(hfi_file, delimiter = ',')
        line = 0
        for row in hfi:
            if line: #skip if line = 0, execute otherwise
                countries.append(row[2]) #country name
                personal_freedom.append(row[60]) #personal freedom out of 10
            line += 1
            if line == 163:
                break
    
    for index in range(len(personal_freedom)):
        if personal_freedom[index] == '-':
            personal_freedom[index] = 0
        else:
            personal_freedom[index] = float(personal_freedom[index])

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

        ppm = [0]*len(countries)
        for index in range(len(countries)):
            c = countries[index]
            for i in range(len(unordered_countries)):
                if unordered_countries[i] == c:
                    ppm[index] = unordered_ppm[i]


    writee = open('pfi_v_covid.csv', 'w', newline='')
    writer = csv.writer(writee, delimiter = ',')
    writer.writerow(['Country','PFI','PPM'])
    for i in range(len(countries)):
        if ppm[i] != 0:
            information = []
            information.append(countries[i])
            information.append(str(personal_freedom[i]))
            information.append(str(ppm[i]))
            writer.writerow(information)

def run_efi():
    countries = []
    economic_freedom = []
    with open('hfi_2017.csv') as hfi_file:
        hfi = csv.reader(hfi_file, delimiter = ',')
        line = 0
        for row in hfi:
            if line: #skip if line = 0, execute otherwise
                countries.append(row[2]) #country name
                economic_freedom.append(row[118]) #economic freedom out of 10
            line += 1
            if line == 163:
                break
    
    for index in range(len(economic_freedom)):
        if economic_freedom[index] == '-':
            economic_freedom[index] = 0
        else:
            economic_freedom[index] = float(economic_freedom[index])

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
        
        ppm = [0]*len(countries)
        for index in range(len(countries)):
            c = countries[index]
            for i in range(len(unordered_countries)):
                if unordered_countries[i] == c:
                    ppm[index] = unordered_ppm[i]


    writee = open('efi_v_covid.csv', 'w', newline='')
    writer = csv.writer(writee, delimiter = ',')
    writer.writerow(['Country','EFI','PPM'])
    for i in range(len(countries)):
        if ppm[i] != 0:
            information = []
            information.append(countries[i])
            information.append(str(economic_freedom[i]))
            information.append(str(ppm[i]))
            writer.writerow(information)

def evaluate_best_fit():

    rvaluelist = []

    for indexi in range(7,120):
        hfi_file = open('hfi_2017.csv')
        hfi = csv.reader(hfi_file, delimiter = ',')
        acc = 0
        for row in hfi:
            name = row[indexi]
            acc += 1
            if acc == 1:
                break
        hfi_file = open('hfi_2017.csv')
        hfi = csv.reader(hfi_file, delimiter = ',')

        print(str(indexi), end = '/120  |  ')
        countries = []
        category_vals = []
        line = 0
        for row in hfi:
            if line != 0: #skip if line = 0, execute otherwise
                countries.append(row[2]) #country name
                category_vals.append(row[indexi]) #category value
            line += 1
            if line == 163:
                break
    

        for index in range(len(category_vals)):
            if category_vals[index] == '-':
                category_vals[index] = 1.0
            else:
                category_vals[index] = float(category_vals[index])

        
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
            
            ppm = [0]*len(countries)
            for index in range(len(countries)):
                c = countries[index]
                for i in range(len(unordered_countries)):
                    if unordered_countries[i] == c:
                        ppm[index] = unordered_ppm[i]
            
            x = category_vals
            y = ppm
            r_squared = (np.corrcoef(x, y)[0,1])**2
            if not np.isfinite(r_squared):
                r_squared = 0.0
            rvaluelist.append([indexi,r_squared,name])
            print([indexi,r_squared,name])

    rvaluelist = Sort(rvaluelist)
    rvaluelist.reverse()
    
    writee = open('category_ranking.csv', 'w', newline='')
    writer = csv.writer(writee, delimiter = ',')
    writer.writerow(['Column number','R-squared', "Column Name"])
    for i in rvaluelist:
        writer.writerow(i)



run_hfi()
run_pfi()
run_efi()
evaluate_best_fit()