##############################################################################
Bot Agent (iOS)
##############################################################################

==============================================================================
Feature
==============================================================================

- Screen capturing
- Action response


==============================================================================
How it runs
==============================================================================

Prequsites

- WebDriverAgent
- libimobiledevice
- Python 3

WebDriverAgent

::

    $ git clone https://github.com/facebook/WebDriverAgent && cd WebDriverAgent
    $ brew install carthage
    $ ./Scripts/bootstrap.sh
    # open WebDriverAgent.xcodeproj with Xcode
    # Xcode:
    # - code sign (general and build_settings): WebDriverAgentLib/WebDriverAgentRunner 
    # - Product -> Destination -> <your device>
    # - Product -> Scheme -> WebDriverAgentRunner
    # - Product -> Test

libimobiledevice (iproxy)

::

    $ brew install libimobiledevice
    $ iproxy 8100 8100
    # browse: http://localhost:8100/status 
    # browse: http://localhost:8100/inspector

Bot Agent (iOS)

::

    $ git clone https://github.com/alpesis-ai/bot-agent-ios.git
    $ cd bot-agent-ios

    $ pip3 install --pre facebook-wda
    $ pip3 install -r requirements.txt
    $ make run


==============================================================================
Developement
==============================================================================

Process

::


    Server                                                iOS
       
    Xcode (WebServerAgent)     -------------------->  WebServerAgent
    libimobiledevice (iproxy)  <--------------------
          |
          |
    Capturing the screen 
          |
    Do some actions            ---------------------> Receiving the actions
                                                            |
    Capturing the screen       <--------------------- Responding to the actions
          |
    Do some actions


Class

::

    run.py <- Agent <-- Connector
