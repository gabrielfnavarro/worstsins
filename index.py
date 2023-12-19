from flask import Flask, render_template
app = Flask(__name__, static_folder='static', static_url_path='/static')
import requests
import os

token = os.getenv('TOKEN')
def get_user_info(user_id, token):
    headers = {
        'Authorization': f'Bot {token}'
    }
    url = f'https://discord.com/api/v10/users/{user_id}'
        
    response = requests.get(url, headers=headers)
        
    if response.status_code == 200:
        user_info = response.json()
        avatar = user_info['avatar']
        return avatar
    else:
        print('Failed to fetch user information.')
        return None



user_id = '981642842457927701'
avatar = get_user_info(user_id, token)
@app.route('/')
def hello_world():


    return render_template('index.html', avatar=f'https://cdn.discordapp.com/avatars/{user_id}/{avatar}.png')

@app.route('/amigos')
def amigos():
    return render_template('amigos.html', avatar=f'https://cdn.discordapp.com/avatars/{user_id}/{avatar}.png')

@app.route('/tempo')
def soso():
    return render_template('tempo.html')
