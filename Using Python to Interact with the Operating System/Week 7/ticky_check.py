#!/usr/bin/env python3

import re
import csv
import sys
import operator

error_dic = {}
user_stat_dic = {} 					#{username: ["INFO", "ERROR"]}
error_header = ("Error", "Count")
user_header = ("Username", "INFO", "ERROR")
csv_filename_for_error = "error_message.csv"
csv_filename_for_usr_info = "user_statistics.csv"


#sys_log_file = sys.argv[1]

#######################################################################################################################

#4 generate csv file
def csv_file_generator(required_file_name, list_to_generate_csv):
	with open(required_file_name, "w", newline='') as file:
		write = csv.writer(file)
		write.writerows(list_to_generate_csv)


def unpack_and_format_usr_list(sorted_usr_list):
	formated_usr_list = [(usr_tuple[0], usr_tuple[1][0], usr_tuple[1][1]) for usr_tuple in sorted_usr_list]
	return formated_usr_list
	
	
#1 a list of all error messages logged and how many times each error was found,

# add and count all error messages to error_dic
def add_count_errors(log_disc):
	if log_disc in error_dic:
		error_dic[log_disc] = error_dic[log_disc] + 1
	else:
		error_dic[log_disc] = 1


#2 A list of all users that have used the system, including how many info & error messages

#COUNT USER "INFO" & "ERROR" FUNCTION
def count_usr_stat(list_of_all_logs):
	for log in list_of_all_logs:
		log_info = re.search(r"([A-Z]*): ([\w ]*) .* \(([\w.]*)\)", log)     #(INFO or ERROR): (disc) (username)
		
		log_status = log_info.group(1)
		log_disc = log_info.group(2)
		user_name = log_info.group(3)
		
		#if log_status == "INFO":
		if "INFO" in log_disc:
			if user_name in user_stat_dic:
				user_stat_dic[user_name][0] = user_stat_dic[user_name][0] + 1
			else:
				user_stat_dic[user_name] = [0, 0]
				user_stat_dic[user_name][0] = 1
		
		#elif log_status == "ERROR":
		elif "ERROR" in log_disc:
			if user_name in user_stat_dic:
				user_stat_dic[user_name][1] = user_stat_dic[user_name][1] + 1
			else:
				user_stat_dic[user_name] = [0, 0]
				user_stat_dic[user_name][1] = 1
			
			add_count_errors(log_disc)

#######################################################################################################################





#READ SYS_LOG FILE
with open("syslog.log", "r") as file:
#with open(sys_log_file, "r") as file:
	all_info_error_list = [line.strip() for line in file.readlines() if "INFO" or "ERROR" in line]
	#all_error_list = [line.strip() for line in file.readlines() if "ERROR" in line]
	
	count_usr_stat(all_info_error_list)
	

#3 convert both dic into csv files namely error_message.csv & user_statistics.csv

#3.1 sort error_dic
sorted_error_list = sorted(error_dic.items(), key = operator.itemgetter(1), reverse=True)
sorted_error_list.insert(0, error_header)   #insert header

#3.2 sorted usr_stat_dic
sorted_usr_list = sorted(user_stat_dic.items())   #[("username", [2,5]), ("username", [3,6])]
#3.2.1 unpack list inside a tupple to have it in required format [("username", 2, 5), ("username", 3, 6)]
new_formated_usr_list = unpack_and_format_usr_list(sorted_usr_list)
new_formated_usr_list.insert(0, user_header)

#GENERATE CSV FILE
csv_file_generator(csv_filename_for_error, sorted_error_list)				#error_message.csv
csv_file_generator(csv_filename_for_usr_info, new_formated_usr_list) 		#user_statistics.csv

