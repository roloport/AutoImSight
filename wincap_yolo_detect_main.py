import numpy as np
import cv2 as cv 
import os 
from posixpath import abspath 
from time import time
from windowcapture import WindowCapture
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator 
# plotting doc: https://docs.ultralytics.com/reference/utils/plotting/#ultralytics.utils.plotting.Annotator.save
# results doc: https://docs.ultralytics.com/reference/engine/results/#ultralytics.engine.results.BaseTensor.to


os.chdir(os.path.dirname(os.path.abspath(__file__)))

# show the list of window names to select from 
# can call static function without declare an object 
# WindowCapture.list_window_names()
# exit()

# inirialize the WindowCapture class 
wincap = WindowCapture(None) # name of window to capture, None = desktop 

# load YOLO pre-trained model
# weights trained from YOLOv8s.pt
model = YOLO('C:\\Users\\user\\Desktop\\Auto\\YOLOv8\\YOLOv8-detect_trained25_binary-6yxdb-4\\detect\\train\\weights\\best.pt') 


# define color for each class
class_color = {
    0: (255, 255, 0), # class: bit-dot
    1: (255, 0, 255), # class: loose-protein
    2: (0, 255, 0), # class: origami
}

# define confidence threshold for each class
class_conf_threshold = {
    0: 0.15, # class: bit-dot
    1: 0.15, # class: loose-protein
    2: 0.6, # class: origami
}

loop_time = time() 
while(True):
    # get an updated image of screenshot
    screenshot = wincap.get_screenshot()

    # perform object detection with YOLO
    results = model.predict(screenshot, stream=True)

    for r in results:
        # Create an Annotator object
        annotator = Annotator(screenshot, line_width=2, font_size=0.5)
        
        boxes = r.boxes
        for box in boxes:
            c = int(box.cls) # convert class to integer
            if c in class_conf_threshold and box.conf.item() >= class_conf_threshold[c]:
                b = box.xyxy[0] # Access the first bounding box in results
                p = box.conf.item() # Convert Tensor to Python float  

                # draw boxes with class specified color
                color = class_color.get(c, (0,0,0)) #Get color for class, default to black if not found         
                annotator.box_label(b, f"{model.names[int(c)]} {p:.2f}", 
                                    color=color, txt_color=(0,0,0))

    annotator_frame = annotator.result()
    
    # display the annotated image
    if annotator_frame is not None: # Check if annotator_frame is defined
        cv.imshow('Origami Detecting', annotator_frame)
    else:
        cv.imshow('Origami Detecting', screenshot)

    # debug the loop rate 
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()


    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')



