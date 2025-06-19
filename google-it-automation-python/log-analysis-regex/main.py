#!/usr/bin/env python3

import re
import sys
import operator
import csv

errorMessage = {}
userEntries = {}

with open("syslog.log") as file:
        lines = file.readlines()
        for line in lines:
                match = re.search(r"ticky: ([\w+]*):? ([\w' ]*)[\[[#0-9]*\]?]? ?\((.*)\)$", line)
                code, error_msg, user = match.group(1), match.group(2), match.group(3)
                
                if error_msg not in errorMessage.keys():
                        errorMessage[error_msg] = 1
                else:
                        errorMessage[error_msg] += 1

                if user not in userEntries.keys():
                        userEntries[user] = {}
                        userEntries[user]['INFO'] = 0
                        userEntries[user]['ERROR'] = 0
                
                if code == "INFO":
                        if user not in userEntries.keys():
                                userEntries[user] = {}
                                userEntries[user]['INFO'] = 0
                                userEntries[user]['ERROR'] = 0
                        else:
                                userEntries[user][code] += 1
                elif code == "ERROR":
                        if user not in userEntries.keys():
                                userEntries[user] = {}
                                userEntries[user]['INFO'] = 0
                        else:
                                userEntries[user]['ERROR'] += 1

# Sorted by value
errors_list = sorted(errorMessage.items(), key=operator.itemgetter(1), reverse=True)

# Sorted by username
per_user_list = sorted(userEntries.items(), key=operator.itemgetter(0))

file.close()

errors_list.insert(0, ('Error', 'Count'))
# per_user_list.insert(0, ('Username', 'INFO', 'ERROR'))

with open('user_statistics.csv', 'w', newline='') as user_csv:
        for key, value in per_user_list:
                user_csv.write(str(key) + ',' + str(value['INFO']) + ',' + str(value['ERROR'])+'\n')

with open('error_message.csv', 'w', newline='') as error_csv:
        for key, value in errors_list:
                error_csv.write(str(key) + ' ' + str(value))
