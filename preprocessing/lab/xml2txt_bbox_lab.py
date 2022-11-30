# Importing the required libraries
import xml.etree.ElementTree as et
import pandas as pd
import os

cols = ["_frame", "_xtl", "_ytl", "_xbr", "_ybr"]


def convert(filename, directory):
    xmlparse = et.parse(filename)
    root = xmlparse.getroot()

    rows = []
    for track in root.iter('track'):
        last_index = len(track.findall('box'))
        print(last_index)
        for box_id, box in enumerate(track.iter('box')):
            frame = int(box.attrib["frame"])
            xtl = float(box.attrib["xtl"])
            ytl = float(box.attrib["ytl"])
            xbr = float(box.attrib["xbr"])
            ybr = float(box.attrib["ybr"])
            #if len(xtl)<2 or len(ytl)<2 or len(xbr)<2 or len(ybr)<2:
             #   print("skipped")
              #  continue

            if box_id == 0:
                command = "BB_CREATE"
                class_id = 0
            elif box_id == last_index-1:
                command = "BB_DELETE"
                class_id = 0
            else:
                command = "BB_MOVE_AND_RESIZE"
                class_id = ""
        
            rows.append({"timestamp": int(frame*1000000/30),
                         "object_id": 0,
                         "command": command,
                         "class_id": class_id,
                         "_xtl": xtl,
                         "_ytl": ytl,
                         "_xbr": abs(xbr-xtl),
                         "_ybr": abs(ybr-ytl),
                         "confidence": 1})

    df = pd.DataFrame.from_dict(rows)

    # Writing dataframe to txt
    df.to_csv(filename.replace('xml', 'txt'), sep='\t', header = None, index = False)

directory = '20210924_1'
for filename in os.listdir('xml/' + directory):
    f = os.path.join('xml/'+ directory, filename)
    # checking if it is a file
    print(f)
    if os.path.isfile(f):
        convert(f, directory)
