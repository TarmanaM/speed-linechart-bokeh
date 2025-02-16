import re
import pandas as pd

regex_timestamp = re.compile(r"Timestamp: (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})")

regex_data = re.compile(r"\[\s*\d+\]\s+([\d.]+)-([\d.]+)\s+sec\s+([\d.]+)\s+(\w+)Bytes\s+([\d.]+)\s+(\w+)bits/sec")

data_list = []

# Membaca file log
with open("soal_chart_bokeh.txt", "r") as file:
    lines = file.readlines()

current_timestamp = None
for line in lines:
    line = line.strip()

    
    match_time = regex_timestamp.match(line)
    if match_time:
        current_timestamp = match_time.group(1)
        continue


    match_data = regex_data.match(line)
    if match_data:
        start_time = float(match_data.group(1))
        end_time = float(match_data.group(2))
        transfer = float(match_data.group(3))
        unit_transfer = match_data.group(4)
        bitrate = float(match_data.group(5))
        unit_bitrate = match_data.group(6)

        if unit_bitrate == "K":
            bitrate /= 1000
        elif unit_bitrate == "G":
            bitrate *= 1000  # Jika ada Gbps
        

        data_list.append([current_timestamp, (start_time + end_time) / 2, bitrate])

df = pd.DataFrame(data_list, columns=["Timestamp", "Interval", "Speed (Mbps)"])

df["Timestamp"] = pd.to_datetime(df["Timestamp"])

df["Hour"] = df["Timestamp"].dt.floor("h")  


df = df.groupby("Hour").agg({"Speed (Mbps)": "mean"}).reset_index()

print(df)

from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, LabelSet, CustomJSTickFormatter
import pandas as pd

output_file("line_chart.html")
p = figure(
    x_axis_type="datetime", 
    title="Test Jaringan",
    x_axis_label="datetime", 
    y_axis_label="Speed (Mbps)",
    width=800, 
    height=400
)

p.line(df["Hour"], df["Speed (Mbps)"], line_width=2, color="blue", legend_label="Data")
p.xaxis.formatter = CustomJSTickFormatter(code="""
    var date = new Date(tick);
    var formatted_date = ("0" + (date.getMonth() + 1)).slice(-2) + "/" +
                         ("0" + date.getDate()).slice(-2)+ "/" + date.getFullYear();
    var formatted_time = ("0" + date.getHours()).slice(-2) + ":" +
                         ("0" + date.getMinutes()).slice(-2) + ":" +
                         ("0" + date.getSeconds()).slice(-2);
    return formatted_date + "\\n" + formatted_time;
""")

p.xgrid.grid_line_color = "gray"  # Warna garis vertikal (sumbu X)
p.xgrid.grid_line_alpha = 0.5  # Transparansi garis (0 = transparan, 1 = solid)
p.ygrid.grid_line_color = "gray"  # Warna garis horizontal (sumbu Y)
p.ygrid.grid_line_alpha = 0.5  # Transparansi garis

show(p)
