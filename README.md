# TCEX Playground

*Package for running/testing [TCEX](https://github.com/ThreatConnect-Inc/tcex) locally.*

There are three steps to getting started with TCEX:

- [installation](#installation)
- [setup](#setup)
- [usage](#usage)

## Installation

### Assumptions

This guide assumes that you already have [python](https://www.python.org/downloads/) installed (ideally python3). To 

This guide assumes you have [**pip**](https://pip.pypa.io/en/stable/installing/) installed. Pip lets you install python packages.

This guide assumes that you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed.

This guide assumes you know a little bit about how to use a command-line/command-prompt.

### Installing Packages

1. Clone this repository: `git clone https://gitlab.com/fhightower-tc/tcex-playground.git` (this will create a directory named `tcex-playground` in the current directory)
2. Navigate into the `tcex-playground` you just cloned (on a unix system: `cd tcex-playground`)
3. Install the [TCEX](https://github.com/ThreatConnect-Inc/tcex) package: `pip install tcex --user --upgrade` (if you have two different versions of python on your system, it may be best to use: `python3 -m pip install tcex --user --upgrade` )

Wonderful! You're done installing all of the necessary packages... now we can start setting up your system to use TCEX.

## Setup

In the `tcex-playground` directory, open `tcex.json`. You don't have to worry about most of the stuff in there for now, but notice there are some values which start with `$env.`. This tells tcex to pull that information from your computer's [environment variables](https://en.wikipedia.org/wiki/Environment_variable). Long story short: it means that you don't have to enter your API credentials into that file (which would be a security concern if that file accidentally got shared). So, to get setup we need to set the environment variables on your computer.

### Unix-based OS (Linux/MAC)

To setup environment variables for TCEX on a unix-based system do the following:

1. Edit the following information with your credentials:

    export API_ACCESS_ID="01234567899876543210"
    export API_SECRET_KEY="adfsdfafafsfsfasdfasfadsasdafdsf"
    export TC_API_PATH="https://sandbox.threatconnect.com/api"
    export API_DEFAULT_ORG='My Organization'

2. Open `~/.bash_profile` () in a text editor and paste the content you just edited.
3. Save `~/.bash_profile` and close the terminal.
4. Open a new terminal and you should be good to go!

### Windows

I'm not entirely sure how to set environment variables on windows, but [this](https://www.techjunkie.com/environment-variables-windows-10/) may help. If you get this working on windows, please [let me know](https://hightower.space/contact/) so I can update this documentation.

## Usage

Now, we're ready to go! Navigate to the directory where you cloned this project (go into the `tcex-playground` directory). Try running: `tclib` (this is the TCEX function to install all of the packages you will need for testing the code in the tcex-playground). Once this finishes, run: `tcrun` (if this throws an error which says something like `IndexError: list index out of range`, try running: `tcrun --0`). This should work! If it doesn't, feel free to raise an [issue](https://gitlab.com/fhightower-tc/tcex-playground/issues/new) or [contact me](https://hightower.space/contact/).
