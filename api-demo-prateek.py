import flask

app = flask.Flask(__name__)

superhero = [
    {'id': 0,
     'name': 'Ironman',	
     'message': 'He is super cool but too futuristic so nahh he is not the one.'},
    {'id': 1,
     'name': 'Superman',
     'message': 'He is an alien and gets scared of a green stone so nahh he is not the one.'},
    {'id': 2,
     'name': 'Captain America',
     'message': 'Well he is the real gentleman and can weild Mjolnir but nope.'},
    {'id': 3,
     'name': 'Thor',
     'message': 'He is 1500 years old Norwian god which sounds cool but he is not the one.'},
    {'id': 4,
     'name': 'Green Lantern',
     'message': 'He can create cool hologram like stuff lol so no'},
    {'id': 5,
     'name': 'Hulk',
     'message': 'He is always angry and I do not like angry. Period.'},
    {'id': 6,
     'name': 'Aquaman',
     'message': 'He is so cool but deep oceans gives me goosebumps so nope.'},
    {'id': 7,
     'name': 'Batman',
     'message': 'Okay you found my favourite superhero. Here is your flag $FLAGFLAGFLAGFLAG$'},
    {'id': 8,
     'name': 'Wonder Woman',
     'message': 'She is awesome but she is so overpowered.'},
    {'id': 9,
     'name': 'Black Panther',
     'message': 'He is cool but has big nails.'},
    {'id': 10,
     'name': 'Flash',
     'message': 'He is a speedy and I am not.'}
]

@app.route('/')
def home():
    return '''<h1>Are you here for the flag?</h1>
<p>Guess my favourite superhero and get the flag<br>
Here are the IDs of respective superheroes you can think of right now:<br>
0. Ironman<br>
1. Superman<br>
2. Captain America<br>
3. Thor<br>
4. Green Lantern<br>
5. Hulk<br>
6. Aquama<br>
7. Batman<br>
8. Wonder Woman<br>
9. Black Panther<br>
10. Flash</p>'''

@app.route('/api/challenge/superhero/<int:superhero_id>', methods=['GET'])
def api_id(superhero_id):
    favsup=[favsup for favsup in superhero if favsup['id']==superhero_id]
    if len(favsup)==0:
        return ("You just went out of the track. You bored with guessing game, already?<br>Check homepage again for valid ID.")
    else:
        return {'favsup': favsup[0]}
if __name__ == '__main__':
    app.run()
	
    
	
