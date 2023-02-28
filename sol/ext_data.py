from bs4 import BeautifulSoup
import requests

from .models import Artist, Position

artists = Artist.objects.all()

def b200():
    for artist in artists:
        esc_name = artist.name.replace(' ', '-').lower()
        positions = Position.objects.filter(chart='Billboard 200')
        url = "https://www.billboard.com/artist/" + esc_name + "/chart-history/tlp/"

        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "lxml")

        b200 = []

        for div in soup.find_all("div", attrs={'class':'o-chart-results-list-row'}):
            obj = dict()
            obj['album'] = div.div.h3.text.strip()
            obj['peak_position'] = div.find_all("div")[1].find_all("div")[1].span.text.strip()
            obj['weeks_on_chart'] = div.find_all("div")[1].find_all("div")[3].span.text.strip()
            
            b200.append(obj)
        
        for ins in b200:
            try:
                position = positions.get(album=ins['album'])
                position.peak_position = ins['peak_position']
                position.weeks_on_chart = ins['weeks_on_chart']
                position.save()
            except Position.DoesNotExist:
                try:
                    position = positions.get(album=ins['album'].lower())
                    position.peak_position = ins['peak_position']
                    position.weeks_on_chart = ins['weeks_on_chart']
                    position.save()
                except Position.DoesNotExist:
                    try:
                        position = positions.get(album=ins['album'].upper())
                        position.peak_position = ins['peak_position']
                        position.weeks_on_chart = ins['weeks_on_chart']
                        position.save()
                    except Position.DoesNotExist:
                        try:
                            position = positions.get(album=ins['album'].capitalize())
                            position.peak_position = ins['peak_position']
                            position.weeks_on_chart = ins['weeks_on_chart']
                            position.save()
                        except Position.DoesNotExist:
                            try:
                                position = positions.get(album=' '.join(word.capitalize() for word in ins['album'].split()))
                                position.peak_position = ins['peak_position']
                                position.weeks_on_chart = ins['weeks_on_chart']
                                position.save()
                            except Position.DoesNotExist:
                                continue