"""
File: webcrawler.py
Name: Wei
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        sum_male = 0
        sum_female = 0

        num_data = soup.find('tbody')
        # print(num_data)
        lst = str(num_data).split('<tr>')
        for i in range(len(lst)):
            data = lst[i]
            data_split = str(data).split()
            # print(data_split) For testing

            if 0 < i < len(lst)-1:

                # print(data_split[2]) For testing
                male_number = str((data_split[2]).strip('<>/td'))
                male_number_nocomma = male_number.replace(",", "")  # comma could not be 'strip' but 'replace'!!!
                male_number_int = int(male_number_nocomma)  # The string could not be made as int or float with ','

                # print(data_split[4]) For testing
                female_number = str((data_split[4]).strip('</td></tr>'))
                female_number_nocomma = female_number.replace(",", "")
                female_number_int = int(female_number_nocomma)
                sum_male += male_number_int
                sum_female += female_number_int
        print('Male Number: '+str(sum_male))
        print('Female Number: '+str(sum_female))



if __name__ == '__main__':
    main()
