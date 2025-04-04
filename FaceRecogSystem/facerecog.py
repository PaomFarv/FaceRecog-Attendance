import csv
import cv2
import face_recognition
import numpy as np
from datetime import datetime

video_capture = cv2.VideoCapture(0)

# Load known faces and their names
person1_image = face_recognition.load_image_file(r"FaceRecogSystem\Faces/messi.png")
person1_face_encoding = face_recognition.face_encodings(person1_image)[0]

person2_image = face_recognition.load_image_file(r"FaceRecogSystem\Faces/ronaldo.png")
person2_face_encoding = face_recognition.face_encodings(person2_image)[0]

known_face_encodings = [person1_face_encoding, person2_face_encoding]
known_face_names = ["Messi","Ronaldo"]

#list of expected names
students = known_face_names.copy()

# Initialize some variables
face_locations = []
face_encodings = []

#Get Current DateTime
now = datetime.now()
current_date = now.strftime("%d-%m-%Y")

report_file = open(f"Attendance_{current_date}.csv", "w+", newline="")
report_writer = csv.writer(report_file)

display_name = ""
display_counter = 0

while True:
    # Capture frame-by-frame
    _,frame = video_capture.read()
    small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    #Recognize faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings,face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings,face_encoding)
        best_match_index = np.argmin(face_distance)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            
        #Pop up a text if someone is recognized         
        name = "Unknown"
        if name in students:
                current_time = now.strftime("%H:%M:%S")
                report_writer.writerow([name, current_time])
                students.remove(name)

                display_name = name
                display_counter = 30

        if display_counter > 0:
            cv2.putText(frame, f"{display_name} Present", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            display_counter -= 1

    cv2.imshow("Attendance",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
report_file.close()
# End of the script