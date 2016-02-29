##S***post Generator

A random post generator for Tumblr.
(by Jack Michaud)

#####Requirements:
    - pip install pytumblr

####To get it working:
You must initialize the Tumblr REST client at the beginning of tumblr.py. 
Go to https://www.tumblr.com/developers for instructions on how to get the necessary credentials.

```
client = pytumblr.TumblrRestClient(
  ‘<consumer_key>’,
  ‘<consumer_secret>’,
  ‘<oauth_token>’,
  ‘<oauth_secret>’,
)
```
####To use:
Run the python file with:
```
python tumblr.py
```
...and follow the prompts!