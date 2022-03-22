#Finding correspondences between descriptors
import cv2
import numpy as np
def video keypoints (matcher, cap=cv2.VideoCapture(".. /data/traffic.mp4,r) .

detector=cv2.ORB_create(40)):
cap.set(cv2.CAP_PROP_POS_FRAMES, 0) while True:
status_cap, frame = cap.read()
frame = cv2.resize(frame? (0, 0), if not status_cap:
break
if (cap.get(cv2.CAP_PROP_POS_FRAMES) - 1) % 40 == 0: key_frame = np.copy(frame)
key_points_l, descriptors_l = detector.detectAndCompute(frame, None) else:
key_points_2, descriptors_2 = detector.detectAndCompute(frameJ None) matches = matcher.match(descriptors_2, descriptors_l)
frame = cv2.drawMatches(frame, key_points_2, key_frame, key_points_l,
matches, None,
ria；,-; =cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTSind| ex_params = diet(algcrit
                                                                         cv2. DRAW_MATCHES_F LAGS_NOT_DRAW_SINGLE_POINTS)
cv2.imshow(* Keypoints match丄ng.，frame) if cv2.wa itKey(300) == 27:
break
cv2. destroyAHWindows ()

뇬t■文안똔드‘: 以
video_keypoints(bf_matcher)
flann__kd_matcher = cv2.FlannBasedMatcher() video_keypoints(flann_kd_matcher?
FLANN_INDEX_LSH = 6

index__params = dict( 
search_params = dict(
    
    flann_kd_matcher = cv2.FlannBasedMatcher(index_paramsJ search_params) video一 keypoints(flann一kd一matcher)
FLANN_INDEX_COMPOSITE = 3

nd| ex_params = diet(algcrit LANN_INDEX_COMPOSITE, rrees=16)

search_params = dict( iecks=10)
flann_kd_matcher = cv2.FlannBasedMatcher(index_params, search__params)

video_keypoints(flann_kd_matcherJ =cv2.xfeatures2d.SURF_create(20000))