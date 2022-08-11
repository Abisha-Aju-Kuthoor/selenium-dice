# Selenium Dice

This program was written to learn how to use the Selenium library with python. 
on running this program, a chrome window will open up https://www.google.com 
and search for "random number", The replace the min and max field with 1 and 6 resppectively. 
Run the random number generation and copy the output into the terminal window  

## Usage 

#### Prerequisites

##### Install python selenium package 

```
pip install selenium
```

##### Install stable version of chromium driver 

* install driver from https://chromedriver.chromium.org/home
* move driver to any location in $PATH
example: 
```
% cp ~/Downloads/chromedriver /usr/local/bin
%
```

#### Run Program

```
python RandomDiceRoll.py
```
##### example output 
```
% python RandomDiceRoll.py
2
%
```

