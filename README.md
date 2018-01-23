# FancyPaper

FancyPaper is a little script that changes your wallpaper to a hot submission from chosen subreddits.

## Requirments:

  1. `Python 3.6`
  2. `pip`
  3. `feh`  ---  `sudo apt install feh`
  4. Reddit account

## Instalation:

  1. Clone the repo:
  `git clone https://github.com/rokn/FancyPaper.git`
  2. Create a new virtual environment(or don't, I don't care)
  
  Example with conda: 
  
  `conda create -n fancypaper python=3.6`
  
  Or with venv: 
  
  `python3 -m venv /path/to/new/virtual/environment`
  
  3. Activate the environment:
  
  `source activate fancypaper`

  4. Install the requirments(You should be in the repo's folder):

  `pip install -r requirments`
  
  5. And finnaly run:

  `sudo ./install.sh`
  
## Using your reddit account:
For the script to work it needs to be authenticated with a reddit account.

To do this go to [your account's apps page](https://www.reddit.com/prefs/apps)

Go to the bottom and click Add new app (or something simmilar).

Set a name and some random redirect url (https://google.com).

Set the type to script.

Then there should be a client id and secret (the id is the one below the name)

Go to your shell's config file (`.bashrc` | `.zshrc` etc..) and add these lines:

    #PRAW CONFIG
    export praw_client_id='Your client id'
    export praw_client_secret='Your client secret'

Finnaly you can execute:

`fancypaper`
