
## MCP SimpleServer
A simple example of an MCP Server that can be used to test MCP clients.



### Usage
1. Clone the repository:
    ```git clone```

2. Navigate to the project directory:
    ```cd simpleserver```
3. Install the required dependencies:
    ```uv sync``` if you have `uv` installed, or
    ```pip install -r requirements.txt``` if you're using pip. I strongly recommend using `uv` as it is faster and more efficient, and it's required for the commands below.
4. Create a .env file in the root of the project and add the following Keys:
```plaintext
WEATHER_API_KEY=xxx
OPENAI_API_KEY=sk-
```

You can get a free OpenWeatherMap API key from https://openweathermap.org/api and an OpenAI API key from https://platform.openai.com/signup.

## Testing a Weather MCP Server (main.py)
1. Run the server:
```uv run mcp dev main.py```
This will start the server, and you can browse to it at localhost (default port is 6274)
2. Open a browser to http://127.0.0.1:6274
3. Click "Connect"
4. Click "Tools" in the top menu
5. Click "List Tools"

You should now see two methods, "add" and "get_weather".

6. Click "get_weather", and enter the name of a city (e.g., "London") in the input field.
7. Click "Run Tool". If you've got a Weather API key set up, you should see the weather for that city.

### Testing a Note Keeper (simplenote.py)
1. Run the server:
```uv run mcp dev simplenote.py```
This will start the server, and you can browse to it at localhost (default port is 6274)
2. Open a browser to http://localhost:6274
3. Click "Connect"
4. Click "Tools" in the top menu
5. Click "List Tools"
You should now see two methods, "add_note", "get_notes" and "get_last_note".

You can use these commands to Add a note, Get all Notes, or get just the last note. Entries will persist, as they're saved to a local file.

### Testing the MCP Server with an OpenAI Agent (aiagent.py)
MCP really shines when it's used with an OpenAI Agent. You can chat with an OpenAI Model, and have it call the MCP Server to get information and perform custom actions.
Run the app: ```uv run aiagent.py```

Chat away! It will call the MCP Server when you ask it to perform actions that are defined in the MCP Server:
    - Add a note
    - Get all notes
    - Get the last note
