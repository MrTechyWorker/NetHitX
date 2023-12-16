# NetHitX

Author:  R Shashank Kanna

![boot](https://github.com/MrTechyWorker/NetHitX/assets/75602943/0dff85f5-cf99-44f9-9c08-31673ac1486a)


NetHitX is an ethical hacking tool crafted for educational purposes, empowering users to perform responsible security assessments and tests on WiFi networks WITHOUT ANY ADDITIONAL HARDWARE. Always ensure explicit permission to use this script on target networks and adhere to all applicable laws and ethical guidelines.

## Table of Contents

- [Introduction](#introduction)
- [Key Features](#key-features)
- [How to Use](#how-to-use)
- [Getting Started](#getting-started)
  - [Cloning Repository](#clone-repo)
  - [Installation](#installing-requirements)
  - [Running](#running-script)
- [Contribute](#contribute)
- [License](#license)
- [Disclaimer](#disclaimer)

## Introduction

NetHitX, implemented in Python, serves as an ethical hacking tool designed to assist in security assessments of WiFi networks. It provides valuable insights into potential vulnerabilities, fostering a deeper understanding of network security principles.

## Key Features

- Scans networks around and provides info on each network's BSSID, channel, name, and also MacId of each station connected to Networks.
- Helps to turn your network interfaces to monitor and managed mode easily.
- Deauths Networks selected with various tools like Aircrack-ng and mdk4.
- Performs handshake capture and uses dictionary attack to crack it.
- Provides a seperate option to crack previously captured handshakes.

## How to use
The script provides a menu driven programme for a simple and easy use, and also this has number of error handling statements to make it easy.

## Getting started
### Clone repo
```bash
#clone this repository 
git clone https://github.com/MrTechyWorker/NetHitX.git
cd NetHitX
```

### Installing requirements
```bash
# Install Dependencies
pip install -r requirements.txt
```
### Running script
```bash
# Use python to run script
# Make sure you run it with sudo
sudo python NetHitX.py
```

## Contribute

We welcome contributions from the community! To contribute to NetHitX, please follow these guidelines:

### Contribution Guidelines

- Fork the repository and create your branch from `main`.
- Make sure your code follows our coding standards.
- Submit a pull request with a clear description of your changes.

### Reporting Issues

If you encounter any issues or bugs, please [create a new issue](https://github.com/MrTechyWorker/NetHitX/issues) with the following details:
- Steps to reproduce the issue.
- Expected behavior.
- Actual behavior.
- System/environment details.

### Feature Requests

We're open to new ideas! If you have a feature request, [submit an issue](https://github.com/MrTechyWorker/NetHitX/issues) with a detailed description of the proposed feature.

### Code of Conduct

Please adhere to our [Code of Conduct](CODE_OF_CONDUCT.md) to ensure a welcoming and inclusive community.

Happy contributing!

## License
NetHitX is released under the [MIT] license.

## Disclaimer

NetHitX is an ethical hacking tool intended for educational purposes only. Utilize this script responsibly and ensure proper authorization before conducting security assessments on any network.
