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

    
    df.to_csv(r'../lab/bbox_fl_txt/'+dirname+'/'+dirname+'_'+str(i)+'.txt', header=None, index=None, sep='\t')


# For one folder
# bbox = '../lab/bbox/20211123_1/19/annotations.txt'
# fl = '../lab/fld/20211123_1/19/annotations.txt'
# merge(bbox, fl, 19, '20211123_1')

dirs = ['20210923_0', '20210927_1', '20211002_0', '20211004_0', '20211006_0', '20211007_1',
        '20211008_1', '20211015_2', '20211019_2', '20211021_0', '20211025_0', '20211028_1', '20211031_0',
        '20211102_0', '20211104_0', '20211110_0', '20211113_1', '20211118_0', '20211123_0', '20211124_0',
        '20211125_1', '20211211_0', '20210924_0', '20210928_0', '20211002_1', '20211005_0', '20211006_1',
        '20211007_2', '20211015_0', '20211019_0', '20211019_3', '20211022_0', '20211025_1', '20211029_0',
        '20211101_0', '20211102_1', '20211104_1', '20211110_1', '20211116_0', '20211118_1', '20211123_1',
        '20211124_1', '20211210_0', '20210924_1', '20210930_0', '20211002_2', '20211005_1', '20211007_0',
        '20211008_0', '20211015_1', '20211019_1', '20211020_0', '20211023_0', '20211028_0', '20211029_1',
        '20211101_1', '20211102_2', '20211106_0', '20211113_0', '20211117_0', '20211120_0', '20211123_2',
        '20211125_0', '20211210_1']

for dirname in dirs:
    for i in range(60):
        bbox = '../lab/bbox/'+dirname+'/'+str(i)+'/annotations.txt'
        fl = '../lab/fld/'+dirname+'/'+str(i)+'/annotations.txt'
        merge(bbox, fl, i, dirname)
