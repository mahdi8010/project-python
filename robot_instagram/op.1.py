from instapy import InstaPy

#login credentials
insta_username = ''
#insta_username = ''
insta_password = ''

#login session
session = InstaPy(username=insta_username, password=insta_password)
session.login()

session.follow_by_tags([''], amount=10)
