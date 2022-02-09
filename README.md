# Hand-Gesture-Detection
Made with OpenCV and MediaPipe ML framework.

## Description
A simple **Python** Hand Gesture Detection(**Rock**, **Paper**, and **Scissors**) program 
made using MediaPipe's ML framework.

![alt text](https://github.com/arshkhans/Hand-Gesture-Detection/blob/main/runningImages/paper.png?raw=true)
![alt text](https://github.com/arshkhans/Hand-Gesture-Detection/blob/main/runningImages/rock.png?raw=true)
![alt text](https://github.com/arshkhans/Hand-Gesture-Detection/blob/main/runningImages/scissorLandmarks.png?raw=true)

## Getting Started

### Prerequisites

* Python 3.7.9
* OpenCV
* MediaPipe

### Installing

* Install OpenCV
```
pip install opencv-python
```
* And MediaPipe
```
pip install mediapipe
```
* Clone the repo
```
git clone https://github.com/arshkhans/Hand-Gesture-Detection.git
```

### Executing program

Once git clone had successfully finished, simply run the program.

## Usage

I'm using this to build a game of Rock, Paper, Scissor. but it can be used for different things not only for a game.
Simply by changing the logic of the landmarks almost any kind of hand gesture can be detected
```
if (hand_landmarks.landmark[8].y > hand_landmarks.landmark[5].y)\
          and (hand_landmarks.landmark[12].y > hand_landmarks.landmark[9].y)\
          and (hand_landmarks.landmark[16].y > hand_landmarks.landmark[13].y)\
          and (hand_landmarks.landmark[20].y > hand_landmarks.landmark[17].y):
          print("Rock")
```
![alt text](https://github.com/arshkhans/Hand-Gesture-Detection/blob/main/runningImages/hand_landmarks.png?raw=true)

![alt text](https://github.com/arshkhans/Hand-Gesture-Detection/blob/main/runningImages/paperLandmarks.png?raw=true)


