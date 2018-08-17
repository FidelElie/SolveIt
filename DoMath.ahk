; Perliminary
DetectHiddenWindows, On  ; needed to control a hidden window
; ------------ Hotstring Used -----------
::solveit::

;  ------------- Autohotkey Front End Initial ------------
; takes user problem, creates the file, puts problem in the file, creates nul file
FileDelete, TextFiles\ProblemAndAnswer.txt
Input, OutputVariable, IV *, {esc}, eq  ; asks the user to enter their problem
LengthOfCalculation:= StrLen(OutputVariable) + 1  ; checks the string length
Send {ShiftDown} {Left %LengthOfCalculation%}{ShiftUp} {Backspace}
Sleep 5
Send Calculating ; just  show the script is working 
; adds the problem to the output file
FileAppend, %OutputVariable%  , TextFiles\ProblemAndAnswer.txt
; adds a nul file to be deleted later in the python file (important)
FileAppend, , TextFiles\Nulfile.txt

; ---------- Python Back End ---------
; runs python script in hidden command prompt, modifies output file with answer 
Run, cmd.exe, , Hide, pid2 ; opens a hidden comand prompt
Sleep 5  ; makes sure that the command prompt has come up 
; While loop so as long as the nulfile exists the python command can run its entiriety 
; without having to use sleep commands
While, FileExist("TextFiles\Nulfile.txt")
{
ControlSend, , python DoCalculations.py {enter}, ahk_pid %pid2% ; sends python command to hidden cmd
} ; only broken when the python command has run all the way through to the end
Process, Close, %pid2% ; closes the command prompt 
Process, WaitClose, %pid2%  ; waits for the command prompt to close

; ---------- Autohotkey Front End Final ---------
; reads the file with answer, and posts it in window
FileRead, OutputCalculation, TextFiles\ProblemAndAnswer.txt
Send {ShiftDown} {Left 12}{ShiftUp} {Backspace}  ; deletes the calculating string
Sleep 5 
Send, %OutputCalculation% ; Send the aswer of the problem back to the user 
return
