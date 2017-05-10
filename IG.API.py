from instagram.client import InstagramAPI
access_token = "https://instagram.com/oauth/authorize/?client_id=[0885d61a8f4734bd6ee22a6a3b7953]&redirect_uri=http://localhost&response_type=token&scope=public_content"
client_secret = "8f74e864a4c54ac5ae1bf7bc9f382b1c"

api = InstagramAPI(access_token=access_token, client_secret=client_secret,)
user_id = api.user_search('user_id')[0].id
recent_media, next_ = api.user_recent_media(user_id=user_id, count=5)

for media in recent_media:
   print media.caption.text
   print ('<img src="%s"/>' % media.images['thumbnail'].url)
