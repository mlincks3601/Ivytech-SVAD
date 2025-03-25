Group project module 3 draft 
Pseudocode taken from chatgpt then modified and added notes for further explanation

Notes for loop usage: The statement "FOR i FROM 1 TO 10 DO" is a loop in pseudocode that is used to repeat a block of code 10 times, once for each value of i from 1 to 10.
Breakdown:
•	FOR → This initiates a loop.
•	i → This is a loop variable (or counter), which keeps track of the number of iterations.
•	FROM 1 TO 10 → This means i starts at 1 and increases by 1 each time (by default), stopping at 10.
•	DO → Indicates the beginning of the loop's code block.
•	END FOR → Marks the end of the loop.
Example Execution:
If i starts at 1, the loop executes the statements inside it, then i increases to 2, and the loop runs again. This continues until i = 10, at which point the loop stops.

BEGIN VARIABLES

    // Define variables for employee input (info we need from the user to calculate)
    // Employee variables 
        ID
        Name
        HourlyRate
        HoursWorked
        GrossPay
        TaxDeduction
        NetPay
    END VARIABLES

    // Declare a list of 10 employees
    DECLARE Employees[10] AS ARRAY OF Employee

    //Start a loop for user to input employee details and then use our variables from above to help calculate payroll
    FOR i FROM 1 TO 10 DO
        DISPLAY "Enter Employee ID: "
        INPUT Employees[i].ID
        DISPLAY "Enter Employee Name: "
        INPUT Employees[i].Name
        DISPLAY "Enter Hourly Rate: "
        INPUT Employees[i].HourlyRate
        DISPLAY "Enter Hours Worked: "
        INPUT Employees[i].HoursWorked

        // After user has inputted the needed info, make sure to call [i] to continue to go through the loop, then calculate payroll
       //NOTES: [i] is used to reference a specific employee in the Employees array (aka a list) at index i during each iteration of the loop.
      //NOTES: Employees[i] → This accesses the i-th employee in the Employees array (aka a list) during each loop iteration.
        Employees[i].GrossPay = Employees[i].HourlyRate * Employees[i].HoursWorked
        Employees[i].TaxDeduction = Employees[i].GrossPay * 0.2  // Assume 20% tax
        Employees[i].NetPay = Employees[i].GrossPay - Employees[i].TaxDeduction
//end the loop     
END FOR

    // Display calculated payroll info to the user when finished
    DISPLAY "Payroll Summary"
    DISPLAY "-------------------------------------------"
  //Start a loop to display the above info for every employee   
 FOR i FROM 1 TO 10 DO
        DISPLAY "Employee ID: ", Employees[i].ID
        DISPLAY "Employee Name: ", Employees[i].Name
        DISPLAY "Gross Pay: $", Employees[i].GrossPay
        DISPLAY "Tax Deduction: $", Employees[i].TaxDeduction
        DISPLAY "Net Pay: $", Employees[i].NetPay
        DISPLAY "-------------------------------------------"
    //end the loop 
    END FOR

END
