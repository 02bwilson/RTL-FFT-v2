# RTL-FFT-v2
## Overview

RTL-FFT-v2 is a real-time Fast Fourier Transform (FFT) display program designed specifically for RTL-SDR (Software Defined Radio) devices. 

It provides a user-friendly interface to configure settings on the SDR and observe their immediate effects on the FFT display. This tool is particularly useful for radio enthusiasts, hobbyists, and professionals who want to visualize and analyze radio frequency signals in real-time.

## Features

    - Real-time FFT display: Observe frequency spectrum changes in real-time.
    - RTL-SDR compatibility: Supports RTL-SDR devices for capturing and processing radio signals.
    - Configurable settings: Adjust various settings such as center frequency, sample rate, gain, and FFT resolution.
    - User-friendly interface: Intuitive interface for easy control and monitoring of SDR parameters.
    - Cross-platform: Compatible with Windows and Linux operating systems.

## Installation
### Prerequisites

Before installing RTL-FFT-v2, ensure you have the following prerequisites installed:

    Python 3.x
    RTL-SDR drivers

Installation Steps

Clone the RTL-FFTv2 repository to your local machine:
```
git clone https://github.com/02bwilson/RTL-FFT-v2.git
```
Navigate to the RTL-FFTv2 directory:

```
cd RTL-FFTv2
```

Install the required dependencies:

```
pip install -r requirements.txt
```
## Usage

Connect your RTL-SDR device to your computer.

Open a terminal or command prompt and navigate to the RTL-FFT-v2 directory.

Run the RTL-FFT-v2 program
```
python RTLFFT.py
```
Use the graphical interface to configure RTL-SDR settings such as center frequency, sample rate, gain, and FFT resolution.

Observe the real-time FFT display to visualize radio frequency signals and their changes.

## Contributing

Contributions to RTL-FFT-v2 are welcome! If you have any ideas for improvements, feature requests, or bug reports, please submit them through GitHub issues or create a pull request.
