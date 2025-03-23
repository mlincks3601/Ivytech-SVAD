Assignment 1 Pseudocode Statements: Maddie Lincks
Below is the first problem:

// This pseudocode is intended to compute the number
// of miles per gallon you get with your automobile
 
Our instructions provide the items that we need to collect so that we can calculate the miles per gallon.  
 
•	The miles traveled 
•	The number of gallons of gas used
 
We know that to calculate the miles per gallon we need to divide the miles traveled by the gallons or gas used.

We need to establish variables to hold our information we will collect

milesTraveled       // Miles traveled
gallonsOfGasUsed    // Number of gallons of gas used
milesPerGallon      // Miles per gallon
 
// Remember in our sample we will begin with start.
 
##start
 
// In the sample we need information from the user, // so we use the pseudocode reference of input.
// and we will indent lines of code so that we know // that the code align will process together.
 
   input milesTraveled
   input gallonsOfGasUsed
 
// We must calculate the miles per gallon.

   milesPerGallon = milesTraveled / gallonsOfGasUsed

// We need to display to the user the results 

   output milesPerGallon

// We have completed our process, so we need to stop.

stop	

Congratulations on completing your pseudocode assignment. If you used this to submit your assignment, when you submit your code, advised your instructor.  You will still receive credit for the assignment example.

Our Pseudocode Assignment result are:

start
    input milesTraveled
    input gallonsOfGasUsed
    milesPerGallon = milesTraveled / gallonsOfGasUsed
    output milesPerGallon

stop
-----------------------------------------------------------------------------------------------------------------------------
Exercise #2 Below:
//Problem: This pseudocode is intended to describe computing the daily cost of your rent in a 30-day month

//We know that to calculate your daily cost of rent in a 30 day time frame, we need to divide the full rent by the amount of days in the chosen month.

//We need to establish variables to hold our information we will collect

Total_rent_amount_per_month       // Full rent amount in a given month 
days_in_month_total    // Number of days in the month 
daily_cost_of_rent      // total daily cost of rent 


##Start
// we need information from the user,
   input days_in_month_total    
   input Total_rent_amount_per_month       
 
// We must calculate the total daily cost of rent I will need to put back every day to make the total months rent..

   daily_cost_of_rent = Total_rent_amount_per_month / days_in_month_total    
// We need to display to the user the results of our // calculation.

Print the output daily_cost_of_rent

// We have completed our process, so we need to stop.

#stop	
-------------------------------------------------------------------------------------------------------------------------------

Exercise 3: 
Problem:
 // This program accepts a user's monthly pay and rent, utilities, and grocery bills
// and displays the amount available for discretionary spending (which might be negative)
// Your program should output the pay and the total bills as well as the remaining discretionary amount

//We know that to calculate the users utilities and we need the user to input them. Then we will calculate the total utility expenses.
// Next we will need the user to input their total monthly income to calculate from. Lastly we will subtract the total monthly utility costs from the users monthly income. 
//The resulted output will be shown as the available spending amount for the user.

//We need to establish variables to hold our information we will collect

Monthly_income // User inputs monthly income
Total_rent_amount_per_month  // We will pull a variable created in exercise #2 to give the user a more realistic answer, we need to includethe users total monthly rent amount
Monthly_utility_cost    // users total cost of a months’ worth of utility expenses
Spending_money      // output variable for users available income after utilities
 
##start
// we need information from the user, // so we use the pseudocode reference of input.
   input Monthly_income
   input Total_rent_amount_per_month  
   input Monthly_utility_cost    
 
// We must calculate the total expenses in a given month, this will make it more organized to calculate the final output 
   Total_months_expenses  = Total_rent_amount_per_month  + Monthly_utility_cost    


// We need to display to the user the results of our // calculation.
   output Total_months_expenses  

// We must do the final calculation to show the users remaining spending money taken from subtracting the total months expenses from users total monthly income
Spending_money = Monthly_income - Total_months_expenses

// display the output for the user 
Print Spending_money

// We have completed our process, so we need to stop.

##stop	
-------------------------------------------------------------------------------------------------------------------------------

