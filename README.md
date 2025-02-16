# Network Speed Test Visualization

## Overview
This Python script reads a network speed log file (`soal_chart_bokeh.txt`), extracts relevant data, and visualizes it using Bokeh. The output is an interactive HTML chart showing the network speed over time.

## Requirements
Make sure you have the following dependencies installed:

```sh
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
pip install -r requirements.txt
```

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/TarmanaM/speed-linechart-bokeh.git
   
   ```

2. Activate the virtual environment:
   ```sh
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. Ensure the log file `soal_chart_bokeh.txt` is in the project directory.
2. Run the script:
   ```sh
   python plot_network.py
   ```
3. The script will generate `line_chart.html`. Open this file in a web browser to view the visualization.

## Dependencies
The required Python packages are:
- `pandas`
- `bokeh`

Install them using:
```sh
pip install pandas bokeh
```

## Notes
- The script assumes the log file follows a specific format. Ensure the format is consistent.
- Modify `soal_chart_bokeh.txt` as needed to test different datasets.
