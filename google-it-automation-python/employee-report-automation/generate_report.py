#!/usr/bin/env python3
import csv

def read_employees(csv_file_location):
        csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
        employee_list= []       
        with open(csv_file_location, "r") as file:
                employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
                for data in employee_file:
                        employee_list.append(dict(data))
        return employee_list

employee_list = read_employees('employees.csv')

def process_data(employee_list):
        department_list = []
        for employee_data in employee_list:
                department_list.append(employee_data['Department'])
        department_data = {}
        for department_name in set(department_list):
                department_data[department_name] = department_list.count(department_name)
        return department_data

dictionary = process_data(employee_list)

def write_report(dictionary, report_file):
        with open(report_file, "w+") as f:
                for k in sorted(dictionary):
                        f.write(str(k) + ':' + str(dictionary[k]) + '\n')         
                f.close()

write_report(dictionary, 'report.txt')
