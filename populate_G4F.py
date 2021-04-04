import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'Glasgow4Freshers.settings')

import django

django.setup()
from G4F_APP.models import Category,Place,Review

def populate():
    Entertainment_places = [{'name':'Jungle Rumble Adventure Golf','description':'Themed mini golf.'},
    {'name':'Ashton Lane','description':'Street dedicated to eating and drinking.'},
    {'name':'Winter fair at George Square','description':'The annual Christmas market in the city center.'}]
    Historical_places = [{'name':'Necropolis','description':'A Victorian cemetery in Glasgow.'},
    {'name':'University of Glasgow','description':'The University of Glasgow is a public research university in Glasgow, Scotland. Founded by papal bull in 1451, it is the fourth-oldest university in the English-speaking world.'},
    {'name':'Glasgow Cathedral','description':'Is the oldest cathedral in mainland Scotland and is the oldest building in Glasgow.'}]
    Educational_places = [{'name':'University of Glasgow Library','description':'The University of Glasgow Library in Scotland is one of the oldest and largest university libraries in Europe.'},
    {'name':'Glasgow Science Centre','description':'It is a center for the popularization of science, where, through simple experiments, you can understand how scientific laws work.'},
    {'name':'Kelvingrove Art Gallery and Museum','description':'The museum has 22 galleries, housing a range of exhibits, including Renaissance art, taxidermy, and artifacts from ancient Egypt.'}]
    Parks_places = [{'name':'Kelvingrove Park','description':'Public park located on the River Kelvin in the West End.'},
    {'name':'Glasgow Green','description':'Park in the east end of Glasgow. Established in the 15th century, it is the oldest park in the city.'},
    {'name':'Glasgow Botanic Gardens','description':'Glasgow Botanic Gardens, located in the West End of Glasgow and managed by Glasgow City Council is arguably the finest Garden in Glasgow, and is dominated by the recently restored Kibble Palace.'}]

    cats = {'Entertainment':{'place':Entertainment_places},'Historical':{'place':Historical_places},'Educational':{'place':Educational_places},'Parks':{'place':Parks_places}}

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data['place']:
            add_place(c, p['name'], p['description'])
            
    for c in Category.objects.all():
        for p in Place.objects.filter(category=c):
            print(f'- {c}: {p}')
            
def add_place(cat, name, description):
    p = Place.objects.get_or_create(category=cat, name=name)[0]
    p.description=description
    p.save()
    return p
    
def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c
    
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
						  
						  