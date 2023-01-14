# WEEK 6:
### Interacting with the Command Line Shell:
			Note:
				touch filename.txt    #to create new file called fileName.txt
				cp ../fileName.txt .    #here cp (copy) fileName.txt file from parent folder (../) to current folder (.)
				mv my_file.txt new_file.txt     #mv move or rename my_file.txt to new_file.txt
				rm  fieldname.txt  #remove/delete file.
				rmdir  folderName    #remove empty folder
				
			Note:
				Redirection: The process of sending a stream (I/O stream like stdin, stdout,stderr) to different destination.
								This is provided by operating system.
								This can be very useful when we want to create a file of the output insted of just viewing the result on the screen.
								We can achieve this using the symbol ">".  Output redirection
									>    overwrite to file
									>>    append to the file
									
								Ex:
									ls -la > list_of_all_files.txt    #if file name list_of_all_files.txt exists then it will overwrite its content with new one if file not exists the it will create one and write its content to that file.
									
								Input redirection using "<". Redirects standard input from file
								
				Pipes (|): Connect the output of one program to the input of another in order to pass data between programs.
				
				Signals: Are tokens delivered to running processes to indicate a desired action.
							Ctrl-c: This sends a SIGINT signal to the program to stop processing cleanly.
							Ctrl-z: This sends a SIGSTOP signal to the program to stop without finishing cleanly.
							fg: restart the program again.
							kill <PID>: will send a signal called SIGTERM that tells the program to terminate.
				
				Note: 
					ps ax   list all the process running in current computer.
					fg: causes a job that was stopped or in the background to return to the foreground
					bg: causes a job that was stopped to go to the background
					jobs: lists the jobs currently running or stopped
					top: shows the processes currently using the most CPU time (press "q" to quit)  
				
				Note:
					Which of the following commands will redirect errors in a script to a file?
						user@ubuntu:~$ ./calculator.py 2> error_file.txt
							The "2>" sign will redirect errors to a file.
							
					What is required in order to read from standard input using Python?
						Stdin file object from sys module
							Using sys.stdin, we can read from standard input in Python.
							
				
### Bash Scripting:
			Note: Bash is scripting language.
			Note: A bash script is run with the .sh file extension.
			
			Ex:
				#! /usr/bin/bash
				
				echo "Starting time: $(date)"
				echo
				
				Note: We can write 2 commands in the same line with ";" after each command.
						echo "Hello"; echo "World!"
							Output:
								Hello
								World!
								
			Note: Define variable and using them using "$"
				Ex:
				my_variable="New variable"
				echo $my_variable
				
			Note: globs ("*" and "?")
					* match any characters and returns list of files with matching vakue. Ex: *.py list all files with ending with .py
					? match exact one character Ex: ???.py  will match new.py, cat.py and so on.
					
			Note: Conditional execution in bash:
				Ex:
					if condition_is_true; then
						echo "When condition is true"
					else
						echo "When condition is false"
					fi  
				
				Note: conditional statement start with "if"  and end with "fi"
				
			R: https://ryanstutorials.net/bash-scripting-tutorial/
			R: https://linuxconfig.org/bash-scripting-tutorial-for-beginners
			R: https://www.shellscript.sh	
			
			Note:
				Which of the following commands will output a list of all files in the current directory?
					echo *
						The star [*] globe will echo or output all files in the current directory.
						
				Which module can you load in a Python script to take advantage of star [*] like in BASH?
					Glob
						The glob module must be imported into a Python script to utilize star [*] like in BASH. 
				
				Conditional execution is based on the _____ of commands.
					exit status
						 In Bash scripting, the condition used in conditional execution is based on the exit status of commands.
						 
				What command evaluates the conditions received on exit to verify that there is an exit status of 0 when the conditions are true, and 1 when they are false?
					test
						 test is a command that evaluates the conditions received and exits with zero when they’re true and with one when they’re false.
						 
				The opening square bracket ([), when combined with the closing square bracket (]), is an alias for which command?
					test
						The test command can be called with square brackets ([]).
						

### Advanced Bash Concepts:
			While loop in bash:
				Ex:
					n=1
					while [ $n -le 5 ]; do
						echo "Hello $n"
						((n+=1))
					done
					
			For loop in bash:
				Ex:1
					for fruit in apple mango orange; do
						echo "I like $fruit"
					done
				
				Ex:2 Convert file names from .HTM to .html
					for file in *.HTM; do
						name=$(basename "$file" .HTM)
						mv "$file" "$file.html"
					done
					
					Note: basename index.htm .htm     #returns index removing .htm
					Note: "$file"      #correctly include file name with space.
				
			Note: The cut command lets us take only bits of each line using a field delimiter.
				echo "Welcome to world of programming" | cut -d" " -f3-
					#retuns "world"
					
					
		
		
		
		Module Review
