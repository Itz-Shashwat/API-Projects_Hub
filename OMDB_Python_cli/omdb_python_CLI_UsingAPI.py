import requests
import click
import configparser

con = configparser.ConfigParser()
con.read('omdb.conf')

key = con['OMDB']['API_KEY']

@click.command()
@click.option('--movie', help='Search by title.')
@click.option('--actor', help='Search by actor.')
def search(movie, actor):
    if not movie and not actor:
        click.echo('Please provide either --movie or --actor .')
        return
    if movie:
        response = requests.get(f'http://www.omdbapi.com/?apikey={key}&t={movie}&type=movie')
    elif actor:
        response = requests.get(f'http://www.omdbapi.com/?apikey={key}&s={actor}&type=movie')
    if response.status_code == 401:
        click.echo('Invalid API Key.')
        return
    data = response.json()
    if movie:
        printing(data,1)
    elif actor:
        printing(data,2)

#Printing Data
def printing(data,set):
    if set==1:
        if data.get('Response') == 'True':
            click.echo(f"{'Movie':<20}{'Release date':<15}")
            click.echo(f"{data['Title']:<20}{data.get('Released', 'N/A'):<15}")
        else:
            click.echo('Movie not found.')
    else:
        if data.get('Response') == 'True':
            movies = data.get('Search', [])
            click.echo(f"{'Movie':<30}{'Year':<10}")
            for movie in movies:
                click.echo(f"{movie['Title']:<30}{movie.get('Year', 'N/A'):<10}")
        else:
            click.echo('No movie found for the actor.')

# Driver
if __name__ == '__main__':
    search()
