# Controlling Electronic Devices using Gestures and Voice

This project allows you to control electronic devices using gestures and voice commands. It is a DIY project developed for a college assignment at IIT Kharagpur. The project utilizes various components such as Arduino Uno, a relay, a laptop, and software for communication and control.

## Project Overview

The objective of this project is to connect electronic devices to a relay, which is then connected to an Arduino Uno board. The Arduino board is controlled by software running on a laptop. The project employs gesture recognition using OpenCV and voice control using the SpeechRecognition library in Python.

The following steps outline the setup and usage of the project.

## Demo
Watch the demo of the project at [https://drive.google.com/file/d/1EzSOKNrK4aPMgv6tB15oqI0dE_KaXGso/view?usp=drivesdk]

## Setup Instructions

1. Ensure that Python is installed on your computer. If not, download and install Python from the official Python website (https://www.python.org).

2. Open a command prompt or terminal and navigate to the project directory.

3. Install the required Python libraries by running the following command:

```bash
pip install -r requirements.txt
```

This command will install the necessary dependencies specified in the `requirements.txt` file.

4. Upload the standard Firmata firmware to the Arduino Uno. This firmware allows communication between the Arduino and the Python software. You can find the Firmata firmware in the Arduino IDE by navigating to **File > Examples > Firmata > StandardFirmata**. Upload this firmware to the Arduino board using the Arduino IDE.

5. Ensure that all the hardware connections are made correctly. Connect the electronic devices you want to control to the relay, and make sure the relay is receiving AC power from a reliable source.

## Usage

To control the electronic devices using gestures, follow these steps:

1. Open a command prompt or terminal and navigate to the project directory.

2. Run the following command to start gesture detection:

```bash
python FingerCounter.py
```
4. Then in another terminal type the command
```bash
python voice_recoginition.py
```

This command will execute the Python script responsible for voice recognition using the SpeechRecognition library. Make sure your microphone is connected and configured correctly. The script will listen for your voice commands and trigger actions accordingly to control the electronic devices connected to the relay.

Note: It is important to ensure that all connections are made correctly, and the relay is properly receiving AC power from the source. Any misconfiguration or faulty connections may lead to unexpected behavior or potential risks. Exercise caution and follow electrical safety protocols.



## Acknowledgments

We would like to express our gratitude to the faculty and staff at IIT Kharagpur for their guidance and support throughout this project.

## Contact Information

For any inquiries or assistance regarding this project, please contact:

Name: Shashank Singhania

Email: shashanksinghania120@gmail.com
