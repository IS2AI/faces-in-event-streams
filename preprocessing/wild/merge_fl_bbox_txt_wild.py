import pandas as pd
import os

# This fucntion merges bounding box and facial landmarks txt data
def merge(bbox, fl, i, dirname):
    bbox_df = pd.read_csv(bbox, sep='\t', header=None)
    bbox_df.columns = ["timestamp", "object_id", "command", "class_id", "x", "y", "w", "h", "confidence"]

    fl_df = pd.read_csv(fl, sep='\t', header=None)
    fl_df.columns = ["timestamp", "object_id", "command_fl", "class_id_fl", "x0", "y0", "x1", "y1", "x2", "y2", "x3", "y3", "x4", "y4", "confidence_fl"]
    
    data = pd.merge(bbox_df, fl_df, on=['timestamp', 'object_id'], how = 'inner')
    data = data[["timestamp", "object_id", "command", "class_id", "x", "y", "w", "h", "x0", "y0", "x1", "y1", "x2", "y2", "x3", "y3", "x4", "y4", "confidence"]]
    
    data = data.sort_values(['object_id', 'timestamp'])
    obj_count = len(data['object_id'].unique())
    all_boxes = dict((obj_id, []) for obj_id in range(obj_count))

    for obj_id in range(obj_count):
        all_boxes[obj_id] = data.loc[data['object_id'] == obj_id]
        all_boxes[obj_id] = all_boxes[obj_id].sort_values(['object_id', 'timestamp'])
        if len(all_boxes[obj_id])>0:
            all_boxes[obj_id].iloc[0, 2] = 'BB_CREATE'
            all_boxes[obj_id].iloc[len(all_boxes[obj_id])-1, 2] = 'BB_DELETE'
            all_boxes[obj_id].iloc[1:len(all_boxes[obj_id])-2, 2] = 'BB_MOVE_AND_RESIZE'
            all_boxes[obj_id].iloc[0, 3] = 0
            all_boxes[obj_id].iloc[1:, 3] = None
    df = all_boxes[0]
    for obj_id in range(1, obj_count, 1):
        df = pd.concat([df, all_boxes[obj_id]])

    
    df.to_csv(r'../bbox_fl_txt/' + dirname + '/' + dirname + '_' + str(i) + '.txt', header=None, index=None, sep='\t')

dirname = '01'
for i in range(5):
    bbox = '../bbox/'+ dirname + '/txt/' + dirname + '_' + str(i) + '.txt'
    fl = '../fl/' + dirname + '/txt/' + dirname + '_' + str(i) + '.txt'
    merge(bbox, fl, i, dirname)

