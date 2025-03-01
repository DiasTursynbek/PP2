import os
path = str(input("Enter the directory path: "))   #input --> example.txt
print(os.access(path, os.F_OK)) # Existence
print(os.access(path, os.R_OK)) # Readability
print(os.access(path, os.W_OK)) # Writeability
print(os.access(path, os.X_OK)) # Executeability

































#   Код	        Мағынасы                    	Не істейді?
# os.F_OK	Файл бар ма?	        Файл немесе папка бар екенін тексереді
# os.R_OK	Оқыға бола ма?	        Файлды оқуға рұқсат бар ма?
# os.W_OK	Жазуға бола ма?	        Файлды өзгертуге рұқсат бар ма?
# os.X_OK	Орындауға бола ма?  	Файлды іске қосуға (execute) бола ма?