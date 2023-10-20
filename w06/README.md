# Team Activity - Human Resources System
Team Activity Overview
For this assignment you need to meet with your team and work together to help each person on the team understand the concepts.

Overview
Consider the scenario of a Human Resources (HR) system. It contains various information about the employees of a company, such as their names, ID numbers, job titles, salaries, etc. From this data you may need to run a payroll process to generate paychecks, generate information for tax purposes, or produce any number of reports of various kinds.

The data for these HR systems is stored on servers. In a real system, this data would be stored in a database, but for our purposes, we will practice by using data stored in a single text file.

Instructions
Download the file hr_system.txt. This file contains information for a set of employees. The first few lines look as follows:


Alexia 1913 Engineer 84000
Herman 4266 Manager 106000
Jay 5849 Engineer 93000
Ahmad 1326 Tester 85000
The format of each line is:


name id_number job_title salary
There is a single space between each field of data.

Your assignment is to write a program to iterate through each line of this file, gather the information from each field and display or take certain actions depending on the data.

Core Requirements
Work through these core requirements step-by-step to complete the program. Please don't skip ahead and do the whole thing at once, because others on your team may benefit from building the program up slowly.

Download the file and save it to your computer. In VS Code, open the folder that contains this file. Then, create a new Python script in that folder.

Have your program open the HR System file, read through it line by line, and at this point, simply display the line to the screen.

Split the line into parts and change your display, so that it shows only the names (instead of the whole line).

For each line, get the name and the job title for each person, and display those to the screen.

At this point, your output should look like the following:


Name: Alexia, Title: Engineer
Name: Herman, Title: Manager
Name: Jay, Title: Engineer
Name: Ahmad, Title: Tester
Name: Ciaran, Title: Engineer
Name: Callum, Title: Engineer
Name: Samantha, Title: Tester
Name: Antonio, Title: Tester
Name: May, Title: CFO
Name: Sebastian, Title: Scientist
Name: Kaitlyn, Title: Support
Name: William, Title: Tester
Name: Sophie, Title: Engineer
Name: Isaiah, Title: Designer
Name: Aimee, Title: CEO
Name: Patrick, Title: Sales
Name: Gloria, Title: Designer
Name: Joseph, Title: Sales
Name: Barbara, Title: Engineer
Stretch Challenge
Strip off any leading and trailing whitespace from each line.

In addition to the name and the job title, also access the salary and the ID number and save them into variables. Display all four values in this format: name (ID: id_number), job_title - $salary. Don't forget to convert the salary to a number and display it with two decimals.

The following shows the first few lines of expected output at this point.


Alexia (ID: 1913), Engineer - $84000.00
Herman (ID: 4266), Manager - $106000.00
Jay (ID: 5849), Engineer - $93000.00
Ahmad (ID: 1326), Tester - $85000.00
Instead of displaying the salary information, calculate and display a paycheck amount for the employee. Assume that they are paid twice a month.

Change the program so that it generates bonuses for anyone who is an engineer. For each of these employees, add $1000 to their paycheck amount.

The following shows sample output at the end of the stretch challenges:


Alexia (ID: 1913), Engineer - $4500.00
Herman (ID: 4266), Manager - $4416.67
Jay (ID: 5849), Engineer - $4875.00
Ahmad (ID: 1326), Tester - $3541.67
Ciaran (ID: 2019), Engineer - $3583.33
Callum (ID: 8005), Engineer - $4041.67
Samantha (ID: 4802), Tester - $3333.33
Antonio (ID: 1423), Tester - $2125.00
May (ID: 5575), CFO - $4666.67
Sebastian (ID: 7378), Scientist - $4250.00
Kaitlyn (ID: 4542), Support - $2625.00
William (ID: 7364), Tester - $3083.33
Sophie (ID: 3437), Engineer - $5541.67
Isaiah (ID: 1518), Designer - $2416.67
Aimee (ID: 8093), CEO - $5208.33
Patrick (ID: 2214), Sales - $3625.00
Gloria (ID: 4414), Designer - $3291.67
Joseph (ID: 9427), Sales - $3791.67
Barbara (ID: 5967), Engineer - $5333.33

Sample Solution
When your program is finished, please view the sample solution for this program to compare it to your approach.

You should work to complete this team activity for the one hour period first, without looking at the sample solution. However, if you have worked on it for at least an hour and are still having problems, you may feel free to use the sample solution to help you finish your program.

Sample solution (Core requirements)

Sample solution (Stretch challenges)

Submission
When you have finished your team meeting, you are welcome to continue working on your own. Feel free to include that additional work when you report on your progress in I-Learn.

When you are finished:

Return to I-Learn to take the quiz.
Up Next
Project Milestone: Data Analysis
Other Links:

Return to: Week Overview | Course Home