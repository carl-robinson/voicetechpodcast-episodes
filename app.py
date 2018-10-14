from flask import Flask
from flask_restful import Api, Resource

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

app.run(debug=False)