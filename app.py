from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os
import logging
from bfs import bfs  

app = Flask(__name__)

FRIENDS_FILE = 'friends.json'
MESSAGES_FILE = 'messages.json'

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def load_data(filename, default):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    else:
        return default


def save_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)


graph = load_data(FRIENDS_FILE, {})
messages = load_data(MESSAGES_FILE, {})


def get_unread_status(user):
    unread_status = {}
    for convo_key_str, convo in messages.items():
        parts = convo_key_str.split('_')
        other_user = None
        if parts[0] == user:
            other_user = parts[1]
        elif parts[1] == user:
            other_user = parts[0]

        if other_user:
            unread_count = 0
            for msg in convo:
                if msg.get('sender') == other_user and not msg.get('read', False) and msg.get('receiver') == user:
                    unread_count += 1
            unread_status[other_user] = {"has_unread": unread_count > 0, "unread_count": unread_count}
    return unread_status


@app.route('/', methods=['GET', 'POST'])
def home():
    suggestions = []
    username = None
    unread_info = {}
    direct_friends = set()
    error_message = None  

    if request.method == 'POST' and 'user' in request.form:
        username = request.form['user'].lower()
        if username not in graph:
            error_message = f"User '{username}' not found in the network."
        else:
            all_connections = bfs(graph, username)
            direct_friends = set(graph.get(username, []))
            suggestions = [friend for friend in all_connections if friend != username]
            unread_info = get_unread_status(username)
            logging.debug(f"Unread info for {username}: {unread_info}")

    return render_template(
        'index.html',
        suggestions=suggestions,
        user=username,
        unread_info=unread_info,
        direct_friends=direct_friends,
        error_message=error_message  
    )


@app.route('/add_friend', methods=['POST'])
def add_friend():
    user1 = request.form['user1'].lower()
    user2 = request.form['user2'].lower()

    if user1 and user2:
        graph.setdefault(user1, [])
        graph.setdefault(user2, [])
        if user2 not in graph[user1]:
            graph[user1].append(user2)
        if user1 not in graph[user2]:
            graph[user2].append(user1)
        save_data(FRIENDS_FILE, graph)
        logging.info(f"Added friend: {user1} and {user2}")
    return redirect(url_for('home'))


@app.route('/remove_friend', methods=['POST'])
def remove_friend():
    user1 = request.form['user1'].lower()
    user2 = request.form['user2'].lower()

    if user1 in graph and user2 in graph:
        if user2 in graph[user1]:
            graph[user1].remove(user2)
        if user1 in graph[user2]:
            graph[user2].remove(user1)
        save_data(FRIENDS_FILE, graph)
        logging.info(f"Removed friend: {user1} and {user2}")
    return redirect(url_for('home'))


@app.route('/chat/<user>/<friend>', methods=['GET', 'POST'])
def chat(user, friend):
    convo_key = tuple(sorted([user, friend]))
    convo_key_str = f"{convo_key[0]}_{convo_key[1]}"

    if request.method == 'POST':
        message = request.form['message']
        if convo_key_str not in messages:
            messages[convo_key_str] = []
        messages[convo_key_str].append({"sender": user, "text": message, "receiver": friend, "read": False})
        save_data(MESSAGES_FILE, messages)
        logging.info(f"Message sent: {user} to {friend}: {message}")
        return redirect(url_for('chat', user=user, friend=friend))

    chat_history = messages.get(convo_key_str, [])
    for msg in chat_history:
        if msg.get('sender') == friend and not msg.get('read', False) and msg.get('receiver') == user:
            msg['read'] = True
            logging.debug(f"Marked message as read: {msg}")
    save_data(MESSAGES_FILE, messages)

    return render_template('chat.html', user=user, friend=friend, messages=chat_history, current_user=user)


@app.route('/api/users/unread')
def get_unread_status_api():
    username = request.args.get('user')
    if username:
        unread_info = get_unread_status(username.lower())
        return jsonify(unread_info)
    return jsonify({})


if __name__ == "__main__":
    app.run(debug=True)
