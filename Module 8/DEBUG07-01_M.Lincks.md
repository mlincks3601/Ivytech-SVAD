// Each time a salesperson sells a car at the
// Pardeeville New and Used Auto Dealership,
// a record is created containing the salesperson�s
// name and the amount of the sale.
// Sales of new and used cars are kept in separate files,
// sorted by salesperson ID number.
// Management has requested a merged file so that
// all of a salesperson�s sales (both new and used cars)
// are displayed together. The following code is intended
// to merge the files.
start
   Declarations
      string newSalesperson
      num newAmount
      string usedSalesperson
      num usedAmount
      string bothAtEof = "N"
      string HIGH_NAME = "ZZZZZ"
      InputFile newSales
      InputFile usedSales
      OutputFile allsales
   getReady()
   while bothAtEof = "Y"
      detailLoop()
   endwhile
   finish()
stop 

getReady()
   open newSales "NewSales.dat"
   open usedSales "UsedSales.dat"
   open allSales "AllSales.dat"

   input newSalesperson, newAmount from newSales
   if eof then
      usedSalesperson = HIGH_NAME
   endif

   input usedSalesperson, usedAmount from usedSales
   if eof then
      usedsalesPerson = HIGH_NAME
   endif

   if newSalesperson = HIGH_NAME AND usedSalesperson = HIGH_NAME then
      bothAtEof = "Y"
   endif
return

detailLoop()
   if newSalesperson > usedSalesperson then
      output usedSalesperson, usedAmount to allSales
      input newSalesperson, newAmount from newSales
      if eof then
         usedSalesperson = HIGH_NAME
      endif
   else
      output newSalesperson, newAmount to allSales
      input usedSalesperson, usedAmount from usedSales
      if eof then
         newSalesperson = HIGH_NAME
      endif
   endif
   if newSalesperson = HIGH_NAME AND usedSalesperson = HIGH_NAME then
      bothAtEof = "Y"
   endif
return

finish()
   close newSales
   close usedSales
   close allSales
return
--------------------------------------------------------------------------------------
Issues Identified:
//Loop condition in while bothAtEof = "Y" is wrong — it should continue the loop until both files reach EOF, so the condition should be while bothAtEof = "N".

//Incorrect file input order in detailLoop() — if newSalesperson > usedSalesperson, you're supposed to read used, but you're reading new instead.

//Misplaced EOF checks — after reading from a file, you're checking eof but not specifying which file, and you're setting the wrong variable in the if statements.

//Inconsistent naming — e.g., usedsalesPerson vs. usedSalesperson.

//Incorrect EOF logic — you're using HIGH_NAME to simulate end-of-file, but this must be consistently applied only after the respective file ends.

//String comparison with HIGH_NAME should be case-sensitive and used only to drive logic after file is fully read.
----------------------------------------------------------------------------------------
//Corrected pseudocode
start
    Declarations
        string newSalesperson
        num newAmount
        string usedSalesperson
        num usedAmount
        string bothAtEof = "N"
        string HIGH_NAME = "ZZZZZ"
        InputFile newSales
        InputFile usedSales
        OutputFile allSales

    getReady()

    while bothAtEof = "N"
        detailLoop()
    endwhile

    finish()
stop

getReady()
    open newSales "NewSales.dat"
    open usedSales "UsedSales.dat"
    open allSales "AllSales.dat"

    input newSalesperson, newAmount from newSales
    if eof(newSales) then
        newSalesperson = HIGH_NAME
    endif

    input usedSalesperson, usedAmount from usedSales
    if eof(usedSales) then
        usedSalesperson = HIGH_NAME
    endif

    if newSalesperson = HIGH_NAME AND usedSalesperson = HIGH_NAME then
        bothAtEof = "Y"
    endif
return

detailLoop()
    if newSalesperson < usedSalesperson then
        output newSalesperson, newAmount to allSales
        input newSalesperson, newAmount from newSales
        if eof(newSales) then
            newSalesperson = HIGH_NAME
        endif
    else
        output usedSalesperson, usedAmount to allSales
        input usedSalesperson, usedAmount from usedSales
        if eof(usedSales) then
            usedSalesperson = HIGH_NAME
        endif
    endif

    if newSalesperson = HIGH_NAME AND usedSalesperson = HIGH_NAME then
        bothAtEof = "Y"
    endif
return

finish()
    close newSales
    close usedSales
    close allSales
return
