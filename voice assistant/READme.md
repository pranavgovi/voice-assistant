# Voice Assistant bot
## I developed this bot before Gen AI came into play.
###
My python script fetches and stores cricket World Cup winners' data from ParseHub API.
I use Speech recognition module to listen to user queries and convert them to text.
Regex is used to match the patterns. 
I have defined different patterns and corresponding functions . The answer is then converted to audio using pyttx3.

## Installation

### Prerequisites
Make sure you have **Python 3.7+** installed.

### Required Libraries
Install the dependencies using:

```bash
pip install requests pyaudio pyttsx3 SpeechRecognition
To use Parsehub set up
API_KEY=''
PROJECT TOKEN=''
