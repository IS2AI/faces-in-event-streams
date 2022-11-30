# Importing the required libraries
import xml.etree.ElementTree as et
import pandas as pd
import os


def convert(filename, directory):
    xmlparse = et.parse(filename)
    root = xmlparse.getroot()

    rows = []
    for track in root.iter('track'):
        object_id = track.attrib["id"]
        last_index = len(track.findall('box'))
        print(last_index)
         
        for box_id, box in enumerate(track.iter('box')):
            if int(box.attrib["outside"]) == 0:
                frame = int(box.attrib["frame"])
                xtl = float(box.attrib["xtl"])
                ytl = float(box.attrib["ytl"])
                xbr = float(box.attrib["xbr"])
                ybr = float(box.attrib["ybr"])

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
                             "object_id": object_id,
                            "command": command,
                            "class_id": class_id,
                            "_xtl": xtl,
                            "_ytl": ytl,
                            "_xbr": abs(xbr-xtl),
                            "_ybr": abs(ybr-ytl),
                            "confidence": 1})

    df = pd.DataFrame.from_dict(rows)

    # Writing dataframe to txt
    df.to_csv(filename.replace('.xml', '.txt'), sep='\t', header = None, index = False)

directory = '../bbox/09/xml'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    print(f)
    if os.path.isfile(f):
        convert(f, directory)
