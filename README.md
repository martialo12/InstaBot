# [InstaBot]()

This instagram bot was made using `instapy`library

<br />

## Build from sources

1- Clone the repo
  ```
  $ git clone https://github.com/martialo12/InstaBot.git
  $ cd InstaBot
  ```

2- Initialize and activate a virtualenv:
  ```
    For linux or mac users:
  $ virtualenv --no-site-packages env
  $ source env/bin/activate

    For linux or mac users:
  $ virtualenv --no-site-packages env
  $ env\scripts\activate
  ```

3- Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

4- Set the database by editing your configuration file
  ```
  $ flask shell
  $ >>> from app import db
  $ >>> db.create_all()
  ```

5- Runnning the bot:
  ```
   python instaBot.py
  ```

## Features

- Login to instagram account
- like target post
- comment target post
- follow/unfollow target people

<br />

## Support

For issues and features request, please feel free to reach me at this address: **martialo218@gmail.com**
<br />
