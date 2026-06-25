# Linus Commands

## 1. pwd
Command         : pwd
Use             : Tells which directory we are cuurently in
Output          : /d/Aditya/COLLEGE/Coding/Synergy_StudentProject/Synergy_TP/task_1

## 2. ls
Command         : ls
Use             : It returns the all the files and folders present in the directory
Output          : README.md  data/  linux_commands.md  myenv/  requirements.txt  setup.log.md  src/

## 3. ls -la
Command         : ls -la
Use             : Returns hidden files along with the other files with more details than the ls command
Output          : total 6
                  drwxr-xr-x 1 ADITYA 197609   0 Jun 25 01:18 ./
                  drwxr-xr-x 1 ADITYA 197609   0 Jun 25 01:31 ../
                  -rw-r--r-- 1 ADITYA 197609  30 Jun 25 01:22 .gitignore
                  -rw-r--r-- 1 ADITYA 197609   0 Jun 25 01:05 README.md
                  drwxr-xr-x 1 ADITYA 197609   0 Jun 25 01:06 data/
                  -rw-r--r-- 1 ADITYA 197609   0 Jun 25 01:06 linux_commands.md
                  drwxr-xr-x 1 ADITYA 197609   0 Jun 25 01:02 myenv/
                  -rw-r--r-- 1 ADITYA 197609 248 Jun 25 01:31 requirements.txt
                  -rw-r--r-- 1 ADITYA 197609   0 Jun 25 01:06 setup.log.md
                  drwxr-xr-x 1 ADITYA 197609   0 Jun 25 01:06 src/

## 4. cd
Command         : cd src
Use             : Changes directory
Output          : Now shows the src directory in the path

## 5. mkdir
Command         : mkdir test
Use             : Useful for making a new directory
Output          : It makes a new directory without any output

## 6. touch
Command         : touch test_1.txt
Use             : Creates a file
Output          : Doesn't show any output, just makes the file in the directory

## 7. cat
Command         : cat src/hello.py
Use             : Shows the contents of a file
Output          : print ('Hello')

## 8. echo
Command         : echo "Aditya Gupta"
Use             : Simply prints the text back as the output in the terminal
Output          : Aditya Gupta

## 9. cp
Command         : cp test_1.txt test_2.txt
Use             : Copies the file
Output          : No output

## 10. mv
Command         : mv test_2.txt test_3.txt
Use             : Moves the file or renames it
Output          : No output

## 11. rm
Command         : rm test_3.txt
Use             : Deletes the file
Output          : No output

## 12. grep
Command         : grep "He" src/hello.py
Use             : Finds patterns in files
Output          : print ('Hello')

## 13. find
Command         : find src
Use             : Used to search for files and folders
Output          : src
                  src/hello.py


## 14. head
Command         : head requirements.txt
Use             : For displaying first few lines of a file
Output          : contourpy==1.3.3
                  cycler==0.12.1
                  fonttools==4.63.0
                  kiwisolver==1.5.0
                  matplotlib==3.11.0
                  numpy==2.5.0
                  packaging==26.2
                  pandas==3.0.3
                  pillow==12.2.0
                  pyparsing==3.3.2


## 15. tail
Command         : tail requirements.txt
Use             : For displaying last few lines of a file
Output          : matplotlib==3.11.0
                  numpy==2.5.0
                  packaging==26.2
                  pandas==3.0.3
                  pillow==12.2.0
                  pyparsing==3.3.2
                  python-dateutil==2.9.0.post0
                  seaborn==0.13.2
                  six==1.17.0
                  tzdata==2026.2

## 16. wc
Command         : wc requirements.txt
Use             : Gives a count of the lines, words and characters
Output          : 14  14 248 requirements.txt

## 17. chmod
Command         : chmod -w data/sample.txt
Use             : Used to change permissions of a file
Output          : No output
