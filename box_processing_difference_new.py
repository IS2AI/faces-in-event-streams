#Replace original load_box_events function with new:

def load_box_events(metadata, batch_start_time, duration):
    """Fetches box events from FileMetadata object, batch_start_time & duration.

    Args:
        metadata (object): Record details.
        batch_start_time (int): (us) Where to seek in the file to load corresponding bounding boxes
        duration (int): (us) How long to load events from bounding box file

    Returns:
        box_events (structured np.ndarray): Nx1 of dtype EventBbox
    """
    def sortone(val):

        return val[0]

    ending = metadata.get_ending()
    box_path = '_bbox.npy'.join(metadata.path.rsplit(ending, 1))

    box_video = EventNpyReader(box_path)
    box_video.seek_time(batch_start_time + 1)
    box_events = box_video.load_delta_t(duration)

    out = np.zeros((len(box_events),), dtype=EventBbox)
    lip=np.zeros((len(box_events),), dtype=EventBbox)
    eye1=np.zeros((len(box_events),), dtype=EventBbox)
    eye2=np.zeros((len(box_events),), dtype=EventBbox)
    nose=np.zeros((len(box_events),), dtype=EventBbox)
    lips=np.zeros((len(box_events),), dtype=EventBbox)
    for k in box_events.dtype.names:
        if k=="x0":
            x0 = box_events["x0"]-w/2
        elif k=="y0":
            y0 = box_events["y0"]-h/2
        elif k=="x1":
            x1= box_events["x1"]-w/2
        elif k=="y1":
            y1 = box_events["y1"]-h/2
        elif k=="x2":
            x2= box_events["x2"]-w/2
        elif k=="y2":
            y2 = box_events["y2"]-h/2
        elif k=="x3":
            x3= box_events["x3"]-w/2
        elif k=="y3":
            y3 = box_events["y3"]-h/2
        elif k=="x4":
            x4= box_events["x4"]-w/2
        elif k=="y4":
            y4 = box_events["y4"]-h/2
        elif k == 'class_confidence':
            out['class_confidence'] = box_events['class_confidence']
            confid=out['class_confidence']

            eye1['t']=t
            eye1['x']=x0
            eye1['y']=y0
            eye1['w']=w
            eye1['h']=h
            eye1['class_id']=id+1
            id0=eye1['class_id']
            eye1['track_id']=tid
            eye1['class_confidence'] =confid
            out=np.append(out,eye1,axis=0)

            eye2['t']=t
            eye2['x']=x1
            eye2['y']=y1
            eye2['w']=w
            eye2['h']=h
            eye2['class_id']=id0+1
            id1=eye2['class_id']
            eye2['track_id']=tid
            eye2['class_confidence'] =confid
            out=np.append(out,eye2,axis=0)

            nose['t']=t
            nose['x']=x2
            nose['y']=y2
            nose['w']=w
            nose['h']=h
            nose['class_id']=id1+1
            id2=nose['class_id']
            nose['track_id']=tid
            nose['class_confidence'] =confid
            out=np.append(out,nose,axis=0)            
            lip['t']=t
            lip['x']=x3
            lip['y']=y3
            lip['w']=w
            lip['h']=h
            lip['class_id']=id2+1
            id3=lip['class_id']
            lip['track_id']=tid
            lip['class_confidence'] =confid
            out=np.append(out,lip,axis=0)

            lips['t']=t
            lips['x']=x4
            lips['y']=y4
            lips['w']=w
            lips['h']=h
            lips['class_id']=id3+1
            id4=eye2['class_id']
            lips['track_id']=tid
            lips['class_confidence'] =confid
            out=np.append(out,lips,axis=0)
            #out=out.sort(key=sortone)
        elif k== "x":
            out['x'] = box_events["x"]
            xor=box_events["x"]
        elif k=="y":
            out['y'] = box_events["y"]
            yor=box_events["y"]
        elif k=="w":
            out['w'] = box_events["w"]
            w=box_events["w"]/3
        elif k=="h":
            out['h'] = box_events["h"]
            h=box_events["h"]/4
        elif k=='class_id':
            out['class_id'] = box_events['class_id']
            id=out['class_id']        
        else:
            out[k] = box_events[k]
            if k=='track_id':
                tid=box_events['track_id']
            if k=="t":
                t=box_events['t']

    return out