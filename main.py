# Run `python main.py` in the terminal

# Note: Python is lazy loaded so the first run will take a moment,
# But after cached, subsequent loads are super fast! ⚡️

import platform
print(f"Hello Python v{platform.python_version()}!")/* Styles généraux */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f9;
    color: #333;
}

header {
    background-color: #2c3e50;
    color: white;
    padding: 20px;
    text-align: center;
}

.balance {
    margin-top: 10px;
    font-size: 20px;
}

main {
    display: flex;
    justify-content: center;
    margin-top: 50px;
}

.machines {
    display: flex;
    justify-content: space-between;
    width: 80%;
}

.machine {
    background-color: white;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    text-align: center;
    width: 30%;
}

.reels {
    display: flex;
    justify-content: space-between;
    margin-top: 20px;
}

.reel {
    width: 60px;
    height: 100px;
    background-color: #34495e;
    color: white;
    font-size: 2rem;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 5px;
}

button {
    background-color: #3498db;
    color: white;
    padding: 10px 20px;
    font-size: 18px;
    border: none;
    border-radius: 5px;
    margin-top: 20px;
    cursor: pointer;
}

button:hover {
    background-color: #2980b9;
}

footer {
    text-align: center;
    margin-top: 50px;
    padding: 20px;
    background-color: #2c3e50;
    color: white;
}
