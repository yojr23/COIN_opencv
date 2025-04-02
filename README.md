# 🪙 COIN_opencv - Beginner OpenCV Project

This is one of my **first OpenCV projects**, developed while learning **computer vision and image processing**. It’s a simple **automated coin counter** that detects and counts coins in an image using OpenCV. While basic, it showcases fundamental image processing techniques.

## 🚀 Features
✅ **Basic coin detection** using OpenCV contour analysis  
✅ **Edge detection** with the Canny algorithm  
✅ **Morphological transformations** for improved accuracy  
✅ **Real-time visualization** of detected coins  
✅ **Lightweight & easy to use**  

## 🏗️ Installation
### 1️⃣ Clone the repository
```bash
git clone https://github.com/yojr23/COIN_opencv.git
cd COIN_opencv
```

### 2️⃣ Install dependencies
Make sure you have **Python 3** installed, then run:
```bash
pip install opencv-python numpy
```

### 3️⃣ Run the script
Save an image of coins as `monedas.jpg` in the project folder and execute:
```bash
python coin_counter.py
```

## 🔬 How It Works
This script processes an image step by step:
1️⃣ Loads the image using `cv2.imread()`  
2️⃣ Converts it to **grayscale** for better processing  
3️⃣ Applies **Gaussian Blur** to reduce noise  
4️⃣ Uses **Canny Edge Detection** to highlight contours  
5️⃣ Performs **morphological transformations** for better contour detection  
6️⃣ Finds and counts the coins using `cv2.findContours()`  
7️⃣ Draws detected coins and displays the final result  

## 📸 Example Output
*(Add an image here for better engagement!)*

## 🏆 Why This Project Matters
While this is an **early learning project**, it helped me understand fundamental image processing techniques in OpenCV. It serves as a great **starting point** for those new to computer vision and looking to experiment with object detection.

## 📜 License
This project is open-source—feel free to use and improve it!

---
If you find this project useful, ⭐ **Star this repository** and check out my other projects on GitHub!
