# SolveIt
This project allows you to do quick inline calculations while writing. By using autohotkey to look for a hostring and python to calculate it. 

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing puposes. 

### Prerequisites
* The latest version of autohotkey if you are planning to just run the raw script.
* The lastest distribution of Python 2.7 whether you are running the Autohotkey executable or the raw script.

### Installation and Use
1. Place the folder whether you like and either run the executable file or run the raw .ahk script for the script to run. 
2. Type the hotsring "solveit" to activate the input process.
3. Type your mathematics problem with spaces between each number and operation.
4. When you are finished entering your desired problem leave a space and type "eq" (for equals).
5. And your problem will be calculate and outputted back to your window/
6. Enjoy

### Supported Operations
The operations follow BIDMAS order of calculation without the B as brackets are not supported yet (IDMAS)
* Indices can be calculated with inputting either a " ^ " or " ** " between two numbers.
* Division can be calculated by inputting a " / " between two numbers
* Multiplication can be calculated with inputting either a " x " or " * " between two numbers
* Addition can be calculated by inputting a " + " between two numbers
* Subtraction can be calculated by inputting a "-" between two numbers
You are able to put two operations next to eachother, the program will resolve to one operation upon calculation 
e.g if you input "11 - - 11 eq" the program will resolve the two negatives to "11 + 11 eq"  

## Built With
* Autohotkey
* Python 2.7 

### Things To Improve
Other than optimisations to the python code, I want to find an easier way for Autohotkey and python to communicate with eachother 
effectively. Right now i am using a Run command for the cmd and sending the python command to it for them to communicate with 
eachother. It works surpringly well but it is not ideal. This process is outlined in DoMath.ahk file. 

Also I want to find a way to make the calculation happen in real-time. So the programme will recognize without the use of a hotkey or hotstring 
that you are typing a problem and automatically solve it for you. 

### License
This project is licensed under the GNU General Public License v3.0 - see the LICENSE.md file for details
