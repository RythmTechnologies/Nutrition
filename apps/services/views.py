from django.shortcuts import render
import requests

# Create your views here.
def services(request):
    return render(request, 'pages/services.html',)


def get_instagram_posts(access_token):
    url = f"https://graph.instagram.com/me/media?fields=id,caption,media_type,media_url&access_token={access_token}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None