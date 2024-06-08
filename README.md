# RemoteBeacon

An application to remotely rotate the antenna, set transmission parameters and transmit.

Tested on ... (Kenwood TS-2000, HyGain DCU3, Raspberry Pi 4)

## Features

- Control and display of antenna rotor parameters
- Control and display of parameters of a radio
- Calculate the antenna parameters (azimuth and distance) based on GPS coordinates or the Maidenhead locator.
- Web interface for remote control (Flask)
- Multiple antenna rotors and radios supported (based on hamlib)
- Remote transmission of a wav file

## Preview

<table>
    <tr>
        <td><img src="images/prev1.png" style="max-height:300px"></td>
        <td><img src="images/prev2.png" style="max-height:300px"></td>
        <td><img src="images/prev3.png" style="max-height:300px"></td>
    </tr>
</table>

## Installation

- Run `conda create --name py311RemoteBeacon python=3.11`
- Run `conda activate py311RemoteBeacon`
- Run `pip install -r requirements.txt`
- Edit `config.json` to match your setup
- Add your own transmission file `transmit.wav`

## Start

- `conda activate py311RemoteBeacon`
- `./start.sh`