import cv2

def rotate_image(image, angle):
    h, w = image.shape[:2]
    center = (w // 2, h // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))
    return rotated_image

def display_video(video_path = 'video.mp4'):
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    rotate_angle = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        frame = rotate_image(frame, rotate_angle)

        cv2.imshow('Video', frame)

        key = cv2.waitKey(fps)
        if key == ord('q'):
            break
        elif key == ord(u"\u0020") :
            rotate_angle += 5
        

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    display_video()