# WEEK 1:
### Course Introduction:
			R: Automate the Boring Stuff with Python https://automatetheboringstuff.com/
			R: Hitchhiker’s Guide to Python https://docs.python-guide.org/
			
### Getting Familiar with the Operating System:
			Operating System: The software that manages everything that goes on the computer.
				There are 2 main parts in OS, Kernel and Userspace.
				Kernel is the main core of OS. It talks directly to harware and manages system resources.
				Userspace: As a user we dont interact with kernel directly,insted we interact userspace.
					Userspace are user interface (UI) and system programs.
					
			Note: Comman linux distributions are Ubuntu, Debian, ReadHat
			Note: Chrome OS, Android are based on Linux kernel.
			
			Note: Python is a cross-platform language.
					As a result we can use the same Python code to get to our goal on any operating system,
					whether the goal is opening files, processing text, or managing running processes.
					
			Note: We can find pre build python modules on pypi (python packageindex).
				  We use pip command to install, update, remove any external python modules.
				  
			Note: Package management tool for Debian Ubuntu and Linux Mint is apt, yum on ReadHat,dnf on Fedora. 
			
			Note: Technical Support Fundamentals course  https://www.coursera.org/lecture/technical-support-fundamentals/module-introduction-I3n9l
			Note: How to install python https://realpython.com/installing-python/
			
### Running Python Locally:
			Note: Source code --> software called complier (Translated to machine level language) --> Machine exicutes this code
					Some examples of commonly use compiled programming languages are C, C++, Go and Rust.
					Compiled language programming language is read and converted to machine code before runtime, allowing for more efficient code.
					A compiled language is translated into code readable by the target machine during development using a compiler.
			Note: Source code --> Interpretater --> Machine exicutes code
					Python, Ruby, JavaScript, Bash, and PowerShell are all examples of interpreted programming languages.
					An interpreted programming language is read and executed as written directly on the target machine by an interpreter.
			Note: Source code --> Complied --> Intermediate Code (created exicutable code which can run on different OS)--> Machine exicute this code
					Java and c# use mixed approch.Code need to be complied first, but it gets compiled into intermediate code. 
			
			Note: What is the purpose of shebang?
					Inserting a shebang line (such as #!/usr/bin/env python3) as the first line tells the operating system what command we want to use to execute the script.
			Note: To launch python interpreter in terminal
					$ python3   #then press enter
						>>
						
			Note: To run python file in terminal
					$ python3 fileName.py   #press enter
					
			Note: Insted of writting python3 and file name, we can use shebang followed by a path for os to find exicutable (such as #!/usr/bin/env python3)
					at the starting of the fileName.py and giving exicutable permission to that file. And finally running using ./fileName.py
					
### Automating Tasks Through Programming:
			Scalability means that when more work is added to a system, the system can do whatever it needs to complete the work.
			Centralizing mistakes means finding an error and fixing it once and for all.
			
			Note: When to automate certain task?
					when automating certain task takes less time than actual manual task * number of times manual task is performed.
					[time_to_automate < (time_to_perform * amount_of_times_done)] 
			
			Note: Pareto Principle states that 20% of the system administration tasks that you perform are responsible for 80% of your work.
			
			Note: Bit-rot: The process of software falling out of step with the environment.
					Ex: suppose evryday backup needs to be performed of the disk name disk1 and if name of tha disk is changed from disk1 ro disk2.
							then automated process of backing up that disk wont perform.
							
			Note: It is always best to send/flag an alert/notification to human when automation fails.
			Note: System log/forensic value.
			
			Note: shutil module is used to check disk usage using disk_usage() function and passing argument "/"
					Ex: shutil.disk_usage("/") #return usage(total=....,used=...., free=...)
					
				  psutil module is used to check cpu usage at a given interval using cpu_percent() function
					Ex: psutil.cpu_percent(0.1)
			
			Note: Program to do a system health check,
				
					import shutil
					import psutil
					
					def check_disk_usage(disk):
						du = shutil.disk_usage(disk)
						free = du.free /du.total * 100
						return free > 20  #return True if more than 20% is free and False if not
						
					def check_cpu_usage():
						usage = psutil.cpu_percent(1)
						return usage < 75  #return True if usage is less than 75%
						
					if not check_disk_usage("/") or not check_cpu_usage:
						print("ERROR!")
					else:
						print("EVERYTHONG IS OK!")
			
			Note: R: Is it worth the time? https://xkcd.com/1205/	
