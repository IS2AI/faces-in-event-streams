# Please navigate to original display_frame.py and add the following code after line 63 of the original file
     if isinstance(box_events, float) or len(box_events) == 0:
        return frame

# Delete lines [70-94] inclusive on both sides of the original(!) file, and insert the following instead
     def get_color(class_id, class_confidence):
        # Define colors for each class ID
        class_colors = {
            1: (255, 0, 0),     # Red for face bbox
            2: (0, 255, 0),     # Green for x1
            3: (0, 0, 255),       # Blue for x2
            4: (255, 255, 0),     # Yellow for x3
            5: (255, 0, 255),       # Magenta for x4
            6: (0, 255, 255)      # Cyan for x5
        }

        if np.all(class_confidence == 1):
            color = (0, 255, 0) # Green for GT
        elif np.any(class_confidence == 1):
            color = (0, 0, 255) # Res
        else:
            color = (255, 0, 255)
        
        # If the class_id exists in the color map, use that, otherwise default to the confidence-based color
        return class_colors.get(class_id, color)


     for class_id in np.unique(box_events['class_id']):
        events = box_events[box_events['class_id'] == class_id]
        topleft_x = np.clip(events["x"], 0, width - 1).astype('int')
        topleft_y = np.clip(events["y"], 0, height - 1).astype('int')
        botright_x = np.clip(events["x"] + events["w"], 0, width - 1).astype('int')
        botright_y = np.clip(events["y"] + events["h"], 0, height - 1).astype('int')

        color = get_color(class_id, events['class_confidence'])

        # For class_id = 1, draw rectangles, for others, draw circles
        if class_id == 1:
            for tlx, tly, brx, bry in zip(topleft_x, topleft_y, botright_x, botright_y):
                cv2.rectangle(frame, (tlx, tly), (brx, bry), color, 1)
        else:
            for tlx, tly, brx, bry in zip(topleft_x, topleft_y, botright_x, botright_y):
                center_x, center_y = (int((tlx + brx) / 2), int((tly + bry) / 2))
                cv2.circle(frame, (center_x, center_y), 0, color, 5)
    
    return frame    		        
