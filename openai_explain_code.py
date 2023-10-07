import openai
import dotenv

config = dotenv.dotenv_values(".env")
openai.api_key = config['API_KEY']

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "You will be provided with a piece of code, and your task is to explain it in a concise way."
    },
    {
      "role": "user",
      "content": "class Log:\n    def __init__(self, path):\n        dirname = os.path.dirname(path)\n        os.makedirs(dirname, exist_ok=True)\n        f = open(path, \"a+\")\n\n        # Check that the file is newline-terminated\n        size = os.path.getsize(path)\n        if size > 0:\n            f.seek(size - 1)\n            end = f.read(1)\n            if end != \"\\n\":\n                f.write(\"\\n\")\n        self.f = f\n        self.path = path\n\n    def log(self, event):\n        event[\"_event_id\"] = str(uuid.uuid4())\n        json.dump(event, self.f)\n        self.f.write(\"\\n\")\n\n    def state(self):\n        state = {\"complete\": set(), \"last\": None}\n        for line in open(self.path):\n            event = json.loads(line)\n            if event[\"type\"] == \"submit\" and event[\"success\"]:\n                state[\"complete\"].add(event[\"id\"])\n                state[\"last\"] = event\n        return state"
    },
    {
      "role": "assistant",
      "content": "This code defines a Log class that is used to log events to a file and retrieve the state of the log.\n\nThe `__init__` method initializes the Log object by creating the necessary directory for the log file and opening the file in \"a+\" mode (append and read). It also checks if the file is newline-terminated and adds a newline if it is not.\n\nThe `log` method takes an event as input, adds a unique event ID to the event, and writes the event as a JSON object to the log file. It also adds a newline after each event.\n\nThe `state` method reads the log file line by line, parses each line as a JSON object, and checks if the event is of type \"submit\" and was successful. It keeps track of the set of completed event IDs and the last event in the log. It returns a dictionary containing the set of completed event IDs and the last event."
    }
  ],
  temperature=0,
  max_tokens=1024,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)