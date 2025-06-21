# 🤝 Friend Suggestion and Chat System

An interactive web application built with Flask that allows users to manage friend connections, get friend suggestions using graph algorithms, and engage in real-time (basic) chat conversations.

---

## 📑 Table of Contents

-   [About the Project](#about-the-project)
-   [Features](#features)
-   [Technology Stack](#technology-stack)
-   [File Structure](#file-structure)
-   [Getting Started](#getting-started)
    -   [Prerequisites](#prerequisites)
    -   [Installation](#installation)
-   [Usage](#usage)
    -   [Running the Application](#running-the-application)
    -   [User Login / Get Suggestions](#user-login--get-suggestions)
    -   [Adding/Removing Friends](#addingremoving-friends)
    -   [Chatting with Friends](#chatting-with-friends)
    -   [Unread Message Indicators](#unread-message-indicators)
-   [Data Persistence](#data-persistence)
-   [Contributing](#contributing)
-   [License](#license)
-   [Author](#author)

---

## 📌 About the Project

This project simulates a basic social network and chat application. It demonstrates how to build a Flask web application that manages user relationships as a graph, provides friend suggestions using Breadth-First Search (BFS), and enables simple peer-to-peer chat functionality with unread message tracking.

## 🚀 Features

* **User Management:** Enter a username to access the system.
* **Friend Connections:** Easily add and remove friends.
* **Friend Suggestions:** Get suggestions for new friends based on existing connections (uses BFS to find "friends of friends").
* **Private Chat:** Engage in direct messages with your friends.
* **Unread Message Indicators:** See at a glance which friends have sent you new messages.
* **Persistent Data:** Friend relationships and chat histories are saved to JSON files.
* **Dynamic UI:** Basic styling for an engaging user experience.

## 🛠️ Technology Stack

* **Backend:** Python 3.x, Flask
* **Graph Algorithm:** Breadth-First Search (BFS)
* **Data Storage:** JSON files (`friends.json`, `messages.json`)
* **Frontend:** HTML, CSS
* **Libraries:** `json`, `os`, `logging`, `collections.deque`

## 📁 File Structure

project_root/
├── app.py                     # Main Flask application with all routes (login, friends, chat)
├── bfs.py                     # Implementation of the Breadth-First Search algorithm
├── friends.json               # Stores the social graph data (who is friends with whom)
├── messages.json              # Stores all chat messages between users
├── templates/                 # HTML templates for the web interface
│   ├── index.html             # Homepage: user input, friend suggestions, add/remove friends
│   └── chat.html              # Chat interface for individual conversations
└── static/                    # Static assets (CSS, images)
├── styles.css             # Custom CSS for styling the application
└── cooky_and_friends.jpg  # Image used in the UI


## ⚙️ Getting Started

Follow these steps to set up and run the project locally.

### 📌 Prerequisites

* Python 3.x
* `pip` (Python package installer)

### 📥 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/Friend_Suggestion_Chat_System.git](https://github.com/your-username/Friend_Suggestion_Chat_System.git)
    cd Friend_Suggestion_Chat_System
    ```
    (Replace `your-username` with your actual GitHub username if you're forking).

2.  **Install Flask:**
    ```bash
    pip install Flask
    ```
    (No `requirements.txt` was provided in this set of files, so Flask is listed directly).

## 🧪 Usage

### Running the Application

1.  From the project's root directory, execute `app.py`:
    ```bash
    python app.py
    ```
2.  Open your web browser and navigate to:
    ```
    [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
    ```

### User Login / Get Suggestions

1.  On the homepage, enter a username in the "Enter User Name" field and click "Get Suggestions".
2.  If the user is new, they will be created. Existing users will see their friend network.
3.  The system will display suggested friends based on your current connections.

### Adding/Removing Friends

* Use the "Add Friend" form to establish a connection between two users.
* Click the "Remove Friend" button next to a friend's name to break the connection.

### Chatting with Friends

* From the suggested friends list, click the "Chat" button next to a friend's name to open a chat window.
* Type your message and click "Send".

### Unread Message Indicators

* On the main page, friends who have sent you new, unread messages will show an unread count next to their name.

## 🗄️ Data Persistence

Friend relationships are stored in `friends.json` and chat messages in `messages.json` within the project directory. This ensures that your data persists even after the application is restarted.

## 🤝 Contributing

Contributions are welcome! If you have any suggestions, bug reports, or want to contribute code, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add new feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## 👤 Author

SANU KUMAR DWIVEDI
