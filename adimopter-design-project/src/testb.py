#!/usr/bin/env python3
import rospy
import cv2
import cv2.aruco as aruco
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import CompressedImage

class ArucoDetector:
    def __init__(self):
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/raspicam_node/image/compressed", CompressedImage, self.image_callback)
        self.aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)
        self.parameters = aruco.DetectorParameters_create()
        self.detected_ids = []

        self.parameters.adaptiveThreshConstant = 7
        self.parameters.minMarkerPerimeterRate = 0.01

    def image_callback(self, msg):
        try:
            np_arr = np.frombuffer(msg.data, np.uint8)
            frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            corners, ids, _ = aruco.detectMarkers(gray, self.aruco_dict, parameters=self.parameters)

            if ids is not None:
                self.detected_ids = ids.flatten().tolist()
                rospy.loginfo("Bulunan ArUco ID'leri: %s"%str(self.detected_ids))
            else:
                self.detected_ids = []
                rospy.loginfo("ArUco marker bulunamadi.")
        except Exception as e:
            rospy.logerr("Goruntu isleme hatasi: %s"%str(e))
            pass
    def get_detected_ids(self):
        return self.detected_ids

if __name__ == "__main__":
    rospy.init_node("aruco_detector_node", anonymous=True)
    detector = ArucoDetector()

    rate = rospy.Rate(10)  # 10 Hz
    while not rospy.is_shutdown():
        ids = detector.get_detected_ids()
        rate.sleep()

