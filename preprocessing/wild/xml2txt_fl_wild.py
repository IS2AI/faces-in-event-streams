# Importing the required libraries
import xml.etree.ElementTree as et
import pandas as pd
import os
import re

def convert(filename, directory):
    print(filename)
    xmlparse = et.parse(filename)
    root = xmlparse.getroot()

    rows = []
    for track in root.iter('track'):
        last_index = len(track.findall('points'))
        print(last_index)
        for points_id, points in enumerate(track.iter('points')):
            object_id = track.attrib["id"]
            if int(points.attrib["outside"]) == 0:
                frame = int(points.attrib["frame"])
                _points = re.sub("[,;]", " ", points.attrib["points"]).split(" ")

                if points_id == 0:
                    command = "BB_CREATE"
                    class_id = 0
                elif points_id == last_index-1:
                    command = "BB_DELETE"
                    class_id = 0
                else:
                    command = "BB_MOVE_AND_RESIZE"
                    class_id = ""
        
                rows.append({"timestamp": int(frame*1000000/30),
                            "object_id": object_id,
                            "command": command,
                            "class_id": class_id,
                            "x0": _points[0],
                            "y0": _points[1],
                            "x1": _points[2],
                            "y1": _points[3],
                            "x2": _points[4],
                            "y2": _points[5],
                            "x3": _points[6],
                            "y3": _points[7],
                            "x4": _points[8],
                            "y4": _points[9],
                            "confidence": 1})

    df = pd.DataFrame.from_dict(rows)
    df.to_csv(filename.replace('.xml', '.txt'), sep='\t', header = None, index = False)

directory = '../fl/09/xml'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    print(f)
    if os.path.isfile(f):
        convert(f, directory)
