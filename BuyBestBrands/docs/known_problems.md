# Known Problems

## Virtual Environment

### Problem Description
Sometimes creating the python virtual environment results in an error.  

### Solution
Open a terminal is vscode.  Execute the command
`pip3 install -r requirements` in the terminal.  This should manually install the missing libraries.

## Flask runs but doesn't work

### Problem Description
There has been one instance where the flask application ran without error but trying to use the application triggered lots of binary data to be logged to the terminal. 

### Solution
The error was only seen when calling the application from chromium on a Windows machine.
Using a tab in an alternative browser allowed normal access.

## VSCode LiveCode

### Problem Description
If live view (URL `http://127.0.0.1:3000`) is viewed it will render the HTML elements of a page but not the template components.  This makes the pages look broken and causes confusion.

### Solution
USe the correct flask URL in the browser `http://127.0.0.1:5000`
