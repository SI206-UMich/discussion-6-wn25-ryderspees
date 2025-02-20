import unittest
import os
import csv


def load_csv(f):
    '''
    Params: 
        f, name or path or CSV file: string

    Returns:
        nested dict structure from csv
        outer keys are (str) years, values are dicts
        inner keys are (str) months, values are (str) integers
    
    Note: Don't strip or otherwise modify strings. Don't change datatypes from strings. 
    '''

    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, f)
    nested_dict = {}
    
    with open(full_path, newline="") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        years = header[1:]
        
        for year in years:
            nested_dict[year] = {}
            
        for row in reader:
            if not row:
                continue
            month = row[0]
            for i, year in enumerate(years):
                nested_dict[year][month] = row[i+1]
                
    return nested_dict

def get_annual_max(d):
    '''
    Params:
        d, dict created by load_csv above

    Returns:
        list of tuples, each with 3 items: year (str), month (str), and max (int) 
        max is the maximum value for a month in that year, month is the corresponding month

    Note: Don't strip or otherwise modify strings. Do not change datatypes except where necessary.
        You'll have to change vals to int to compare them. 
    '''
    result = []
    for year in sorted(d.keys()):
        max_val = None
        max_month = None
        for month, val in d[year].items():
            int_val = int(val)
            if max_val is None or int_val > max_val:
                max_val = int_val
                max_month = month
        result.append((year, max_month, max_val))
    return result

def get_month_avg(d):
    '''
    Params: 
        d, dict created by load_csv above

    Returns:
        dict where keys are years and vals are floats rounded to nearest whole num or int
        vals are the average vals for months in the year

    Note: Don't strip or otherwise modify strings. Do not change datatypes except where necessary. 
        You'll have to make the vals int or float here and round the avg to pass tests.
    '''
    averages = {}
    for year in d:
        total = 0
        count = 0
        for month, value in d[year].items():
            total += int(value)
            count += 1
        avg = round(total / count) if count > 0 else 0
        averages[year] = avg
    return averages

class dis7_test(unittest.TestCase):
    '''
    you should not change these test cases!
    '''
    def setUp(self):
        self.flight_dict = load_csv('daily_visitors.csv')
        self.max_tup_list = get_annual_max(self.flight_dict)
        self.month_avg_dict = get_month_avg(self.flight_dict)

    def test_load_csv(self):
        self.assertIsInstance(self.flight_dict['2021'], dict)
        self.assertEqual(self.flight_dict['2020']['JUN'], '435')

    def test_get_annual_max(self):
        self.assertEqual(self.max_tup_list[2], ('2022', 'AUG', 628))

    def test_month_avg_list(self):
        self.assertAlmostEqual(self.month_avg_dict['2020'], 398, 0)

def main():
    print("----------------------------------------------------------------------")
    flight_dict = load_csv('daily_visitors.csv')
    print("Output of load_csv:", flight_dict, "\n")
    print("Output of get_annual_max:", get_annual_max(flight_dict), "\n")
    print("Output of get_month_avg:", get_month_avg(flight_dict), "\n")
    unittest.main(verbosity=2)



if __name__ == '__main__':
    main()
