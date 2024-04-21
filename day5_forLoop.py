import requests

movie_ids = [
    238, 680, 550, 185, 641, 515042, 152532, 120467, 872585, 906126, 840430
]

movie_api_url = 'https://nomad-movies.nomadcoders.workers.dev/movies/'

for movie_id in movie_ids:
    url = f'{movie_api_url}{movie_id}'
    response = requests.get(url)
    data = response.json()
    title = data['title']
    overview = data['overview']
    vote_average = data['vote_average']
    print(f'Title: {title}\nOverview: {overview}\nVote Average: {vote_average}\n')
