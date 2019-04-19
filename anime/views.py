import requests
from django.shortcuts import render
from .models import Show
from .forms import ShowForm
import random

def home(request):
    BASE = 'https://api.jikan.moe/v3/'

    if request.method == 'POST':
        try:
            if request.POST['action'] == 'Submit':
                request.session['rec'] = []
                user = request.POST.get('textbox').lower()
                url = BASE + 'user/{}/animelist/ptw'
                r = requests.get(url.format(user))

                nameurl = BASE + 'user/{}/profile'
                name = requests.get(nameurl.format(user))
                request.session['name'] = name.json()['username']
                assert user != None, "Invalid username"
                ptw = r.json()['anime']
                mal_id = []
                for show in ptw:
                    mal_id.append(show['mal_id'])
                request.session['ids'] = mal_id
                for _ in range(0,5):
                    getAnime(request)
            elif request.POST['action'] == 'more':
                for _ in range(0,5):
                    getAnime(request)

            context = {'rec' : request.session['rec'], 'name' : request.session['name']}
            return render(request, 'home.html', context)
        except:
            return render(request, 'home.html')
            
    return render(request, 'home.html')

def getAnime(request):
    BASE = 'https://api.jikan.moe/v3/'
    try:
        id = random.randint(0,len(request.session['ids'])-1)
        malid = request.session['ids'].pop(id)
        url = BASE + 'anime/{}'
        url = url.format(malid)
        r = requests.get(url).json()
        show_info = {
            'title'     : r['title'],
            'type'      : r['type'],
            'episodes'  : r['episodes'],
            'score'     : r['score'],
            'url'       : r['url'],
            'image_url' : r['image_url']
        }
        if r['title_english']:
            show_info['title_english'] = r['title_english']
            rec = request.session['rec']
            rec.append(show_info)
            request.session['rec'] = rec
    except:
        context = {'rec' : request.session['rec'], 'name' : request.session['name']}
        return render(request, 'home.html', context)