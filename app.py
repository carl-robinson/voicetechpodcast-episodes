from flask import Flask
from flask_restful import Api, Resource
import os

# deployed here:
# https://dashboard.heroku.com/apps/voicetechpodcast-episodes/deploy/github

# links:
# https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3
# https://medium.freecodecamp.org/how-to-host-lightweight-apps-for-free-a29773e5f39e


app = Flask(__name__)
api = Api(app)

# escape any ' or \
# need ?download=true at end of mp3 link?
episodes = [
    {'num': '1', 'title': 'Speech to Text - Eric Bolo, Batvoice', 'mp3': 'https://www.buzzsprout.com/159584/691682-speech-to-text-eric-bolo-batvoice-voice-tech-podcast-ep-001.mp3'},
    {'num': '2', 'title': 'Voice AI for eCommerce - John Fitzpatrick, Voysis', 'mp3': 'https://www.buzzsprout.com/159584/706405-voice-ai-for-ecommerce-john-fitzpatrick-voysis-voice-tech-podcast-ep-002.mp3'},
    {'num': '3', 'title': 'Vivatech 2018 Voice Startup Summary', 'mp3': 'https://www.buzzsprout.com/159584/713152-vivatech-2018-voice-startup-summary-voice-tech-podcast-ep-003.mp3'},
    {'num': '4', 'title': 'Building Knight Rider\'s KITT - Charles Cadbury, Champers Advisory', 'mp3': 'https://www.buzzsprout.com/159584/727981-building-knight-rider-s-kitt-charles-cadbury-champers-advisory-voice-tech-podcast-ep-004.mp3'},
    {'num': '5', 'title': 'The Art of Sound in Motion - Greg Beller, IRCAM', 'mp3': 'https://www.buzzsprout.com/159584/745293-the-art-of-sound-in-motion-greg-beller-ircam-voice-tech-podcast-ep-005.mp3'},
    {'num': '6', 'title': 'Deaf Person Calling - Benjamin Etienne, Rogervoice', 'mp3': 'https://www.buzzsprout.com/159584/756593-deaf-person-calling-benjamin-etienne-rogervoice-voice-tech-podcast-ep-006.mp3'},
    {'num': '7', 'title': 'Perception of Smiles in the Voice - Pablo Arias, IRCAM', 'mp3': 'https://www.buzzsprout.com/159584/768073-perception-of-smiles-in-the-voice-pablo-arias-ircam-voice-tech-podcast-ep-007.mp3'},
    {'num': '8', 'title': 'Signal Processing Basics for Audio - Dogac Basaran, CNRS', 'mp3': 'https://www.buzzsprout.com/159584/779373-signal-processing-basics-for-audio-dogac-basaran-cnrs-voice-tech-podcast-ep-008.mp3'},
    {'num': '9', 'title': 'Hum a Fingerprint, Extract a Melody - Dogac Basaran, CNRS', 'mp3': 'https://www.buzzsprout.com/159584/791569-hum-a-fingerprint-extract-a-melody-dogac-basaran-cnrs-voice-tech-podcast-ep-009.mp3'},
    {'num': '10', 'title': 'Podcasts of the Future - Bryan Colligan, AlphaVoice', 'mp3': 'https://www.buzzsprout.com/159584/804581-podcasts-of-the-future-bryan-colligan-alphavoice-voice-tech-podcast-ep-010.mp3'},
    {'num': '11', 'title': 'Audio Branding & Sound Design - Sebastian Hanfland, Hanfland & Friends', 'mp3': 'https://www.buzzsprout.com/159584/817053-audio-branding-sound-design-sebastian-hanfland-hanfland-friends-voice-tech-podcast-ep-011.mp3'},
    {'num': '12', 'title': 'Fast Scalable Voice IoT Apps - Syed Ahmed, PubNub', 'mp3': 'https://www.buzzsprout.com/159584/829047-fast-scalable-voice-iot-apps-syed-ahmed-pubnub-voice-tech-podcast-ep-012.mp3'}
]

episode_string = "Episode 12 - Fast Scalable Voice IoT Apps - Syed Ahmed, PubNub, Episode 11 - Audio Branding & Sound Design - Sebastian Hanfland, Hanfland & Friends"
# episode_string = ''.join([''.join(['Episode ', ep['num'], ' - ', ep['title'], ', ']) for ep in reversed(episodes)])
# episode_string = episode_string[:-2]  # remove final comma
# episode_string = 'hello hello hello'
episode_feed = {'topics': episode_string, 'min_episode': 1, 'max_episode': len(episodes)}

class Episode(Resource):
    def get(self, num):
        try:
            ep = episodes[int(num) - 1]
            return ep, 200
        # no element at this index
        except IndexError:
            return 'Episode not found', 404

# hit http://127.0.0.1:5000/ep/1 for episode 1
# hit http://127.0.0.1:5000/ep/0 for last episode
api.add_resource(Episode, '/ep/<string:num>')

class Feed(Resource):
    def get(self):
        return episode_feed, 200

# hit http://127.0.0.1:5000/feed
api.add_resource(Feed, '/feed')

# {"topics":"Here are the available episodes. When you know what episode to play, you can interrupt me anytime by saying, 'Alexa, play Episode 7, or whatever episode number it is'. Here you go: Episode 20 - Jeanine\u2019s Spanish Siesta, Episode 19 - Underrated Travel Locations: Guatemala, Episode 18 - Big Lovin\u2019 Utah\u2019s National Parks, Episode 17 - Packing Light, Light-ish\u2026, Episode 16 - Pod Q&amp;A \u2013 Unlimited Data Abroad?, Episode 15 - A Little Bit of Work Travel &amp; A Lot A Bit of Soccer, Episode 14 - South Africa Travel Tips &amp; World Cup 2010, Episode 13 - Thank you, Anthony Bourdain, Episode 12 - Iceland &amp; Panama; Let\u2019s Explore the World Cup Newbies, Episode 11 - Korean Spa Day\u2026 kinda, Episode 10 - Back to Life, Back from the Philippines, Episode 9 - Tips for Travel Beginners, Episode 8 - Some of Our Favorite Places, Episode 7 - Solo Dolo Traveling, Episode 6 - Road Trip Tips &amp; Gas Station Snacks, Episode 5 - Pod Q&amp;A \u2013 Strangers?, Episode 4 - 2018 Travel Plan, Planning, Episode 3 - Packing For Hiking Trips; Don\u2019t Forget Your Poop Shovel!, Episode 2 - How to Get the Cheapest Airfare; Bc We\u2019re Poor, Episode 1 - Intro to Podcast","min_episode":1,"max_episode":20}

# app.run(debug=False)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000)) #The port to be listening to — hence, the URL must be <hostname>:<port>/ inorder to send the request to this program
    app.run(host='0.0.0.0', port=port)  #Start listening