# Cloud Vault - A Demo Project for CSE 325 @ BUET

Cloud Vault is a web application that lets users store files in the cloud. It is a simple
application written in Django to demonstrate web application architecture to students of
CSE 325.

## Setting Up The Project

### Install Python 3

You need to make sure Python 3.10 or later is installed in your system. If you are using
Linux, use your distros package manager. If on Mac, use homebrew. If you are on Windows,
consider installing a better OS like Linux :)

### Set Up Project Repo

Clone the repo and create a python virtual environment to store our dependencies.

```shell
git clone git@github.com:unixdev/cloud-vault.git
cd cloud-vault
python3 -m venv ENV               # creates the virtual environment
source ./ENV/bin/activate         # activate the virtual environment
pip install --upgrade pip         # upgrade pip, it's a good thing to do
pip install -r requirements.txt   # install our dependencies in the virtual environment
```

### Install PostgreSQL

Install PostgreSQL. 