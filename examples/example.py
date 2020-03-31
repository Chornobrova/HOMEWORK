from InstagramAPI import InstagramAPI
 
username = '' #get the username for logging out
password = '' #get the password for logging out
 
api = InstagramAPI(username, password)
 
def get_last_liked_post(api=api):
    """
    Return a url for the last
    liked post of the user
    """
    api.login()
    api.getTotalLikedMedia()
    post = api.LastJson['items'][0]
    return post['carousel_media'][0]['image_versions2']['candidates'][0]['url']
 
print(get_last_liked_post())