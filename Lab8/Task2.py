import requests
import json
import random
from episode import Episode
from character import Character



# 2.1 Random Character Request
random_character_id = random.randint(1, 826)
character_url = f"https://rickandmortyapi.com/api/character/{random_character_id}"

response_character = requests.get(character_url).json()

# 2.2 Response Output
print("2.2 Response Output:")
print(json.dumps(response_character, indent=2))

# 2.3 Save to File
filename_character = f"info_character_{random_character_id}.json"
with open(filename_character, 'w') as file_character:
    json.dump(response_character, file_character, indent=2)

# 2.4 Episode List
episode_urls = response_character['episode']
episode_ids = [int(url.split("/")[-1]) for url in episode_urls]

filename_episodes = f"all_episodes_with_character_{random_character_id}.txt"
with open(filename_episodes, 'a') as file_episodes:
    for episode_id in episode_ids:
        file_episodes.write(f"https://rickandmortyapi.com/api/episode/{episode_id}\n")

# 2.5 Episode Response Structure
episode_example_url = "https://rickandmortyapi.com/api/episode/1"
response_episode_structure = requests.get(episode_example_url).json()
print("\n2.5 Episode Response Structure:")
print(json.dumps(response_episode_structure, indent=2))

# 2.6 Episode Class Creation
# Assuming attributes are 'id', 'name', etc.
class Episode:
    def __init__(self, id, name, air_date, episode, characters, url, created):
        self.id = id
        self.name = name
        self.air_date = air_date
        self.episode = episode
        self.characters = characters
        self.url = url
        self.created = created

# 2.7 Episode Data Retrieval
episode_objects = []
for episode_id in episode_ids:
    episode_url = f"https://rickandmortyapi.com/api/episode/{1}"
    response_episode = requests.get(episode_url).json()
    episode_objects.append(Episode(**response_episode))

# 2.8 Class Methods
# Add methods to the Episode class if needed

# 2.9 Character Response Structure
character_example_url = "https://rickandmortyapi.com/api/character/1"
response_character_structure = requests.get(character_example_url).json()
print("\n2.9 Character Response Structure:")
print(json.dumps(response_character_structure, indent=2))

# 2.10 Character Class Creation
# Assuming attributes are 'id', 'name', 'status', etc.
class Character:
    def __init__(self, id, name, status, species, gender, origin, location, image, episode, url, created):
        self.id = id
        self.name = name
        self.status = status
        self.species = species
        self.gender = gender
        self.origin = origin
        self.location = location
        self.image = image
        self.episode = episode
        self.url = url
        self.created = created

# 2.11 Character Object Creation
random_character_object = Character(**response_character)

# 2.12 Character Class Methods
# Add methods to the Character class if needed

# 2.13 Result
print("\n2.13 Result:")
print(f"Random Character ID: {random_character_id}")
print(f"Character Object: {random_character_object.__dict__}")
print(f"Episode Objects:")
for episode_object in episode_objects:
    print(episode_object.__dict__)
