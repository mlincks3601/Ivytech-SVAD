// One customer – show all data and total bills

//Start

Input area_code
Input phone_number
Input total_messages

Set base_bill = 5
Set extra = 0

//start an if else for calculating total messages and set parameters
If total_messages > 100 and total_messages <= 300 Then
    extra = (total_messages - 100) * 0.03
Else If total_messages > 300 Then
    extra = (200 * 0.03) + ((total_messages - 300) * 0.02)
End If

//set tax variables and calculations
Set before_tax_total = base_bill + extra
Set after_tax_total = before_tax_total * 1.14

//display results
Print "Area Code: ", area_code
Print "Phone Number: ", phone_number
Print "Messages Sent: ", total_messages
Print "Total Before Tax: $", before_tax_total
Print "Total After Tax: $", after_tax_total

//End


-------------------------------------------
//Keep asking for customer data until sentinel value is entered to stop the loop 

//Start
// start a loop for requesting customer data
Loop
    Input area_code
    If area_code == 000 Then
        Exit Loop
    End If

//pull variables from top program
    Input phone_number
    Input total_messages

//set base bill and extra same as the top program
    Set base_bill = 5
    Set extra = 0
//using the same parameters for the if-else on the top program, set them again here
    If total_messages > 100 and total_messages <= 300 Then
        extra = (total_messages - 100) * 0.03
    Else If total_messages > 300 Then
        extra = (200 * 0.03) + ((total_messages - 300) * 0.02)
    End If

//using the same variables in the top program, replace them here for calculating tax
    Set before_tax_total = base_bill + extra
    Set after_tax_total = before_tax_total * 1.14
//display results 
    Print "Area Code: ", areaCode
    Print "Phone Number: ", phone_number
    Print "Messages Sent: ", numMessages
    Print "Total Before Tax: $", before_tax_total
    Print "Total After Tax: $", after_tax_total

End Loop

//End
-----------------------------------------

//Same as above but only show if messages > 100

//Start

//re use the loop parameters from above program
Loop
    Input area_code
    If area_code == 000 Then
        Exit Loop
    End If

    //use the same input variables
    Input phone_number
    Input total_messages

    If total_messages > 100 Then
        Set base_bill = 5
        Set extra = 0
        Set before_tax_total = base_bill + extra
        Set after_tax_total = before_tax_total * 1.14
    //display results
        Print "Area Code: ", area_code
        Print "Phone Number: ", phone_number
        Print "Messages Sent: ", total_messages
        Print "Total Before Tax: $", before_tax_total
        Print "Total After Tax: $", after_tax_total
    End If

End Loop

//End
-------------------------------------------

Start

Loop
    Input area_code
    If area_code == 000 Then
        Exit Loop
    End If

    Input phone_number
    Input total_messages

    Set base_bill = 5
    Set extra = 0

    If total_messages > 100 and total_messages <= 300 Then
        extra = (total_messages - 100) * 0.03
    Else If total_messages > 300 Then
        extra = (200 * 0.03) + ((total_messages - 300) * 0.02)
    End If

    Set before_tax_total = base_bill + extra
    Set after_tax_total = before_tax_total * 1.14
    
    //start the if fnction for tax totals more than $10 and display results 
    If after_tax_total > 10 Then
        Print "Area Code: ", area_code
        Print "Phone Number: ", phone_number
        Print "Messages Sent: ", total_messages
        Print "Total Before Tax: $", before_tax_total
        Print "Total After Tax: $", after_tax_total
    End If

End Loop

//End
-------------------------------------------

//Show only messages from a specific area code

//Start

Input chosen_area_code

Loop
    Input area_code
    If area_code == 000 Then
        Exit Loop
    End If

    Input phone_number
    Input total_messages

   //set the IF paraemters to look for the chosen area code when an area code is inputted by user
    If area_code == chosen_area_code Then
        Set base_bill = 5
        Set extra = 0

    //re use parameters from first code porgram
        If total_messages > 100 and total_messages <= 300 Then
            extra = (total_messages - 100) * 0.03
        Else If total_messages > 300 Then
            extra = (200 * 0.03) + ((total_messages - 300) * 0.02)
        End If

        Set before_tax_total = base_bill + extra
        Set after_tax_total = before_tax_total * 1.14

        Print "Area Code: ", area_code
        Print "Phone Number: ", phone_number
        Print "Messages Sent: ", total_messages
        Print "Total Before Tax: $", before_tax_total
        Print "Total After Tax: $", after_tax_total
    End If

End Loop

End
