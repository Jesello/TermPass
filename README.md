# Welcome to TermPass

term pass is a gnupg-based password manageryou should therefore install your gnupg package according to your operating system

#  installation

## for window users:

firstly you need to install gnupg package in your computer
go to [gpg4win](https://www.gpg4win.org/) and install package

    git clone https://github.com/Jesello/TermPass
    cd TermPass
    pip install -r requirements.txt

## for linux users:

package names may be different in linux distributions, search for the gnupg package in your distribution and install it on your computer then run commands

    git clone https://github.com/Jesello/TermPass
    cd TermPass
    pip install -r requirements.txt



## for android users:
you can also run the app on android, for this you need to install termux. once the app is installed, run the following commands

    apt update
    apt upgrade
    apt install gnupg
    git clone https://github.com/Jesello/TermPass
    cd TermPass
    pip install -r requirements.txt


## Setup

the setup function runs when you first run the app, you can also run the setup function within the app

### question 1:

    Where you want to store passwords:

enter passwords folder

### question 2:

    Where is the main gnupg directory:

If you have modified the main gnupg folder, enter the folder path, if not, leave it empty

### question 3,4,5:

    Select <> color:

choose the colors you like

## New

     > new <filename>


you need a gpg key to run this command
paste the following command into the command line of your computer and then edit it as you wish

    gpg --full-generate-key

Enter which components you want to encrypt, for example

Email
username
password
website

press exit or q to stop the loop.

## rm

    > rm <filename>

delete files

## ls

    > ls

list the files inside the password folder

## keys

    > keys

list avaible gnupg keys

## conf

    > conf

view your configuration

## color

    > color

change colors
