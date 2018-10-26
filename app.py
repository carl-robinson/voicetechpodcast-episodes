from flask import Flask
from flask_restful import Api, Resource
import os

# deployed here:
# https://dashboard.heroku.com/apps/voicetechpodcast-episodes/deploy/github

# links:
# https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3
# https://medium.freecodecamp.org/how-to-host-lightweight-apps-for-free-a29773e5f39e

# create objects
app = Flask(__name__)
api = Api(app)

# ######################################
# Update this list with your own episodes
# ######################################
# List of dictionaries of episodes with number, title and mp3 url, in the following format:
# {'num': '1', 'title': 'Speech to Text - Eric Bolo, Batvoice', 'mp3': 'https://www.buzzsprout.com/159584/691682-speech-to-text-eric-bolo-batvoice-voice-tech-podcast-ep-001.mp3'},
# escape any ' with \
# MUST remove any ampersands (&) or feed will break
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
    {'num': '11', 'title': 'Audio Branding and Sound Design - Sebastian Hanfland, Hanfland and Friends', 'mp3': 'https://www.buzzsprout.com/159584/817053-audio-branding-sound-design-sebastian-hanfland-hanfland-friends-voice-tech-podcast-ep-011.mp3'},
    {'num': '12', 'title': 'Fast Scalable Voice IoT Apps - Syed Ahmed, PubNub', 'mp3': 'https://www.buzzsprout.com/159584/829047-fast-scalable-voice-iot-apps-syed-ahmed-pubnub-voice-tech-podcast-ep-012.mp3'}
]
# ######################################


# build the episode string
episode_string = ''.join([''.join(['Episode ', ep['num'], ' - ', ep['title'], '. ']) for ep in reversed(episodes)])
episode_string = episode_string[:-2]  # remove final comma
episode_feed = {'topics': episode_string, 'min_episode': 1, 'max_episode': len(episodes)}

# class to process request for a specific episode
class Episode(Resource):
    def get(self, num):
        try:
            ep = episodes[int(num) - 1]
            return ep, 200
        # no element at this index
        except IndexError:
            return 'Episode not found', 404

# url endpoint for information on a specific episode
# For a specified episode e.g. episode 1:
    # debug: http://127.0.0.1:5000/ep/1
    # live: https://voicetechpodcast-episodes.herokuapp.com/ep/1
# For the latest episode:
    # debug: http://127.0.0.1:5000/ep/0
    # live: https://voicetechpodcast-episodes.herokuapp.com/ep/0
# sample output: {"num": "12", "title": "Fast Scalable Voice IoT Apps - Syed Ahmed, PubNub", "mp3": "https://www.buzzsprout.com/159584/829047-fast-scalable-voice-iot-apps-syed-ahmed-pubnub-voice-tech-podcast-ep-012.mp3"}
api.add_resource(Episode, '/ep/<string:num>')

# class to process request for list of all episodes
class Feed(Resource):
    def get(self):
        return episode_feed, 200

# url endpoint for list of all episodes
    # debug: hit http://127.0.0.1:5000/feed
    # live: hit https://voicetechpodcast-episodes.herokuapp.com/feed
# sample output: {"topics": "Episode 12 - Fast Scalable Voice IoT Apps - Syed Ahmed, PubNub. Episode 11 - Audio Branding and Sound Design - Sebastian Hanfland, Hanfland and Friends. Episode 10 - Podcasts of the Future - Bryan Colligan, AlphaVoice. Episode 9 - Hum a Fingerprint, Extract a Melody - Dogac Basaran, CNRS. Episode 8 - Signal Processing Basics for Audio - Dogac Basaran, CNRS. Episode 7 - Perception of Smiles in the Voice - Pablo Arias, IRCAM. Episode 6 - Deaf Person Calling - Benjamin Etienne, Rogervoice. Episode 5 - The Art of Sound in Motion - Greg Beller, IRCAM. Episode 4 - Building Knight Rider's KITT - Charles Cadbury, Champers Advisory. Episode 3 - Vivatech 2018 Voice Startup Summary. Episode 2 - Voice AI for eCommerce - John Fitzpatrick, Voysis. Episode 1 - Speech to Text - Eric Bolo, Batvoice", "min_episode": 1, "max_episode": 12}
api.add_resource(Feed, '/feed')

# uncomment this line and comment the main method to run debug locally
# app.run(debug=False)

# main method that runs on program start, and listens for incoming requests for episodes
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000)) #The port to be listening to — hence, the URL must be <hostname>:<port>/ inorder to send the request to this program
    app.run(host='0.0.0.0', port=port)  #Start listening
