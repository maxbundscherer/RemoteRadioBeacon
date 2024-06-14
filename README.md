# RemoteRadioBeacon

An application to remotely rotate the antenna, set transmission parameters and transmit.

Tested on ... (Kenwood TS-2000, HyGain DCU3, Raspberry Pi 4)

## Features

- Control and display of antenna rotor parameters
- Control and display of parameters of a radio
- Calculate the antenna rotor parameters (azimuth and distance) based on GPS coordinates or the Maidenhead locator.
- Web interface for remote control (flask)
- Multiple antenna rotors and radios supported (based on hamlib)
- Remote transmission of a wav file
- Https and authentication supported

## Preview

<table>
    <tr>
        <td><img src="images/prev1.png" style="max-height:300px"></td>
        <td><img src="images/prev2.png" style="max-height:300px"></td>
        <td><img src="images/prev3.png" style="max-height:300px"></td>
    </tr>
</table>

## Config

- Edit `radioresources/config.json` to match your setup
- Add your own transmission file `radioresources/transmit.wav`

## Install

### Development/Conda

- Run `conda create --name py311RemoteRadioBeacon python=3.11`
- Run `conda activate py311RemoteRadioBeacon`
- Run `pip install -r requirements.txt`

### Raspberry Pi 4

- `cd ..`
- `mkdir MBPythonEnv`
- `python -m venv MBPythonEnv/`
- `source MBPythonEnv/bin/activate`
- `cd RemoteRadioBeacon`
- `pip install -r requirements.txt`

## Start

### Development/Conda

- `conda activate py311RemoteRadioBeacon`
- `./start.sh`

### Raspberry Pi 4

- `cd ..`
- `source MBPythonEnv/bin/activate`
- `cd RemoteRadioBeacon`
- `./start.sh`