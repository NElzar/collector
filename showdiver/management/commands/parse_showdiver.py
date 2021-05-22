import requests
import time
from django.core.management.base import BaseCommand
from showdiver.models import Event, Ticket


class Command(BaseCommand):
    help = 'Сохранение данных о мероприятий с сайта showdiver.com'

    def handle(self, *args, **options):
        a = 0
        num = 1
        while num < 2:
            a += 1
            url = 'https://api.showdiver.com/events/?page='+str(a)+'&page_size=16&search=&period_start=&period_end='
            response = requests.get(url)
            if response.json().get('detail') == "Неправильная страница":
                print('больше страниц нет')
                break
            data = response.json()['results']
            for link in data:
                uuid = link['uuid']
                if Event.objects.filter(uuid=uuid).exists():
                    continue
                url_2 = 'https://api.showdiver.com/events/'+uuid+'/'
                response = requests.get(url_2)
                data_post = response.json()
                print(data_post)
                title = data_post['title']
                description = data_post['description'] or ''
                start = data_post['start_at']
                poster = data_post['poster']
                event = Event.objects.create(uuid=uuid, title=title, description=description, start=start, poster=poster)
                for place in data_post['price_categories']:
                    sector = place['title']
                    price = place['price']
                    Ticket.objects.create(sector=sector, site=sector, price=price, event=event)
                time.sleep(2)
