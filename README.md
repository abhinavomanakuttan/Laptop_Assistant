# Laptop_Assistant

<h4>SpeechRecognition</h4>
  # pip install SpeechRecognition <br>
      Library for performing speech recognition, with support for several engines and APIs, online and offline
      
      import speech_recognition as sr
      for index, name in enumerate(sr.Microphone.list_microphone_names()):
      print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

<h4>Open AI</h4>
    #pip install openai <br>
       The official Python library for the openai API
       <br><br>
       
       import os
       from openai import OpenAI

<h4>Wikipedia</h4>
    #pip install wikipedia <br>
    Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia.
    <br><br>
    
    import wikipedia
    print wikipedia.summary("Wikipedia")

<h4>PyAudio</h4>
    #pip install PyAudio<br>
    PyAudio provides Python bindings for PortAudio v19, the cross-platform audio I/O library. With PyAudio, you can easily use Python to play and record audio on a variety of platforms, such as GNU/Linux,         
    Microsoft Windows, and Apple macOS.
    <br><br>
    Windows
    
    python -m pip install pyaudio

<br>
This installs the precompiled PyAudio library with PortAudio v19 19.7.0 included. The library is compiled with support for Windows MME API, DirectSound, WASAPI, and WDM-KS. It does not include support for ASIO. If you require support for APIs not included, you will need to compile PortAudio and PyAudio.

  macOS<br>
  Use Homebrew to install the prerequisite portaudio library, then install PyAudio using pip:

    brew install portaudio
    pip install pyaudio


