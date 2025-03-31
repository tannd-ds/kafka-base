from flask import Flask, Response, render_template
import cv2
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Get video configuration from environment variables
VIDEO_PATH = os.getenv('VIDEO_PATH', 'videos/camera1.mp4')
VIDEO_FPS = int(os.getenv('VIDEO_FPS', 30))
VIDEO_RESOLUTION_WIDTH = int(os.getenv('VIDEO_RESOLUTION_WIDTH', 1920))
VIDEO_RESOLUTION_HEIGHT = int(os.getenv('VIDEO_RESOLUTION_HEIGHT', 1080))
VIDEO_LOOP = os.getenv('VIDEO_LOOP', 'true').lower() == 'true'

def generate_frames():
    cap = cv2.VideoCapture(VIDEO_PATH)
    
    while True:
        success, frame = cap.read()
        if not success:
            if VIDEO_LOOP:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue
            break
            
        # Resize frame if needed
        if frame.shape[1] != VIDEO_RESOLUTION_WIDTH or frame.shape[0] != VIDEO_RESOLUTION_HEIGHT:
            frame = cv2.resize(frame, (VIDEO_RESOLUTION_WIDTH, VIDEO_RESOLUTION_HEIGHT))
            
        # Encode frame to JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    
    cap.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                   mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 