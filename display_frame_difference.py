# Please navigate to original display_frame.py and add the following code after line 63 of the original file
     if isinstance(box_events,float):		
        return frame

# Delete lines [70-94] inclusive on both sides of the original(!) file, and insert the following instead
    if np.any(box_events['class_id']==2):		    
        topleft_y = np.clip(box_events["y"], 0, height - 1).astype('int')
        events1=box_events[box_events['class_id']==2]		    
        botright_x = np.clip(box_events["x"] + box_events["w"], 0, width - 1).astype('int')
        topleft_x11 = np.clip(events1["x"], 0, width - 1).astype('int')		    
        botright_y = np.clip(box_events["y"] + box_events["h"], 0, height - 1).astype('int')
        topleft_y11 = np.clip(events1["y"], 0, height - 1).astype('int')		
        botright_x11 = np.clip(events1["x"] + events1["w"], 0, width - 1).astype('int')		
        botright_y11 = np.clip(events1["y"] + events1["h"], 0, height - 1).astype('int')		
        if np.all(box_events['class_confidence']==1):		
            color=(0,255,0)		
        elif np.any(box_events['class_confidence']==1):		
            color=(0,0,255)		
        else:		
            color=(255,0,255)		
        #colors = choose_color(box_events, color_from, force_color=force_color)		
        for i, (tlx, tly, brx, bry) in enumerate(zip(topleft_x11, topleft_y11, botright_x11, botright_y11)):		
            #color = colors[i].tolist()		
            cv2.circle(frame, (int((tlx + ((brx-tlx) / 2))), int((tly + ((bry-tly) / 2)))), 0, color, 5)		
    if np.any(box_events['class_id']==3):		
        events2=box_events[box_events['class_id']==3]		
        topleft_x12 = np.clip(events2["x"], 0, width - 1).astype('int')		
        topleft_y12 = np.clip(events2["y"], 0, height - 1).astype('int')		
        botright_x12 = np.clip(events2["x"] + events2["w"], 0, width - 1).astype('int')		
        botright_y12 = np.clip(events2["y"] + events2["h"], 0, height - 1).astype('int')		
        if np.all(box_events['class_confidence']==1):		
            color=(0,255,0)		
        elif np.any(box_events['class_confidence']==1):		
            color=(0,0,255)		
        else:		
            color=(255,0,255)		
        #colors = choose_color(box_events, color_from, force_color=force_color)		
        for i, (tlx, tly, brx, bry) in enumerate(zip(topleft_x12, topleft_y12, botright_x12, botright_y12)):		
            #color = colors[i].tolist()		
            cv2.circle(frame, (int((tlx + ((brx-tlx) / 2))), int((tly + ((bry-tly) / 2)))), 0, color, 5)		
    if np.any(box_events['class_id']==4):		
        events3=box_events[box_events['class_id']==4]		
        topleft_x13 = np.clip(events3["x"], 0, width - 1).astype('int')		
        topleft_y13 = np.clip(events3["y"], 0, height - 1).astype('int')		
        botright_x13 = np.clip(events3["x"] + events3["w"], 0, width - 1).astype('int')		
        botright_y13 = np.clip(events3["y"] + events3["h"], 0, height - 1).astype('int')		
        #colors = choose_color(box_events, color_from, force_color=force_color)		
        if np.all(box_events['class_confidence']==1):		
            color=(0,255,0)		
        elif np.any(box_events['class_confidence']==1):		
            color=(0,0,255)		
        else:		
            color=(255,0,255)		
        for i, (tlx, tly, brx, bry) in enumerate(zip(topleft_x13, topleft_y13, botright_x13, botright_y13)):		
            #color = colors[i].tolist()		
            cv2.circle(frame, (int((tlx + ((brx-tlx) / 2))), int((tly + ((bry-tly) / 2)))), 0, color, 5)		
    if np.any(box_events['class_id']==5):		
        events5=box_events[box_events['class_id']==5]		
        topleft_x15 = np.clip(events5["x"], 0, width - 1).astype('int')		
        topleft_y15 = np.clip(events5["y"], 0, height - 1).astype('int')		
        botright_x15 = np.clip(events5["x"] + events5["w"], 0, width - 1).astype('int')		
        botright_y15 = np.clip(events5["y"] + events5["h"], 0, height - 1).astype('int')		
        #colors = choose_color(box_events, color_from, force_color=force_color)		
        if np.all(box_events['class_confidence']==1):		
            color=(0,255,0)		
        elif np.any(box_events['class_confidence']==1):		
            color=(0,0,255)		
        else:		
            color=(255,0,255)		
        for i, (tlx, tly, brx, bry) in enumerate(zip(topleft_x15, topleft_y15, botright_x15, botright_y15)):		
            #color = colors[i].tolist()		
            cv2.circle(frame, (int((tlx + ((brx-tlx) / 2))), int((tly + ((bry-tly) / 2)))), 0, color, 5)		
    if np.any(box_events['class_id']==6):		
        events4=box_events[box_events['class_id']==6]		
        topleft_x14 = np.clip(events4["x"], 0, width - 1).astype('int')		
        topleft_y14 = np.clip(events4["y"], 0, height - 1).astype('int')		
        botright_x14 = np.clip(events4["x"] + events4["w"], 0, width - 1).astype('int')		
        botright_y14 = np.clip(events4["y"] + events4["h"], 0, height - 1).astype('int')		
        #colors = choose_color(box_events, color_from, force_color=force_color)		
        if np.all(box_events['class_confidence']==1):		
            color=(0,255,0)		
        elif np.any(box_events['class_confidence']==1):		
            color=(0,0,255)		
        else:		
            color=(255,0,255)		
        for i, (tlx, tly, brx, bry) in enumerate(zip(topleft_x14, topleft_y14, botright_x14, botright_y14)):		
            #color = colors[i].tolist()		
            cv2.circle(frame, (int((tlx + ((brx-tlx) / 2))), int((tly + ((bry-tly) / 2)))), 0, color, 5)		
    if np.any(box_events['class_id']==1):      		    
        colors = choose_color(box_events, color_from, force_color=force_color)
	events0=box_events[box_events['class_id']==1]		
        num_box=len(events0)		
        print(events0)		
        topleft_x0 = np.clip(events0["x"], 0, width - 1).astype('int')		
        topleft_y0 = np.clip(events0["y"], 0, height - 1).astype('int')		
        botright_x0 = np.clip(events0["x"] + events0["w"], 0, width - 1).astype('int')		
        botright_y0 = np.clip(events0["y"] + events0["h"], 0, height - 1).astype('int') 		
        if np.all(box_events['class_confidence']==1):		
            color=(0,255,0)		
        elif np.any(box_events['class_confidence']==1):		
            color=(0,0,255)		
        else:		
            color=(255,0,255)		
        #colors = choose_color(box_events, color_from, force_color=force_color)		
        for i, (tlx, tly, brx, bry) in enumerate(zip(topleft_x0, topleft_y0, botright_x0, botright_y0)):		  
            color = colors[i].tolist()	        
            cv2.rectangle(frame, (tlx, tly), (brx, bry), color, thickness)		        
