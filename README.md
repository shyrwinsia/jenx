# Jenx

Tool to decrypt Hudson/Jenkins usernames and passwords

## Why?

Why not?

## Install

This script needs Python 3.x. Get it here: [Python website](https://www.python.org/downloads/). Alternatively, you can use Conda (it's much cooler): [Anaconda website](https://docs.conda.io/en/latest/)

### Install Dependencies

`pip install -r requirements.txt`

## Usage

1. Take the necessary files from your Hudson/Jenkins installation.

   You need three files:

   - `credentials.xml`
   - `hudson.util.Secret`
   - `master.key`

   You can find the file `credentials.xml` in $JENKINS_HOME and `hudson.util.Secret` and `master.key` in $JENKINS_HOME/secrets

2. Place the files in a folder

3. Execute script

   `python jenx.py /path/to/your/folder`

   or

   `python jenx.py`

   The second one assumes the files are in the same directory with the script.

4. Read the output. It should contain the usernames and passwords.

## What's in the name?

It's a portmanteau of Jenkins and jinx (curse).

## Disclaimer

I'm not liable for any damages/loss of information/privacy breach attributed to this or anything that happens to you, esp. if you are breaking laws in your country.

## License

MIT
