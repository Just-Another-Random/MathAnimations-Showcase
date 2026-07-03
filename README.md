# Math Animations Showcase

This repository contains a collection of animations created using [Manim](https://www.manim.community/), an animation engine for explanatory math videos.

## ⚙️ Installation & Setup

To run the code and render these animations on your local machine, you will need to install Python and the Manim library.

**1. System Prerequisites**
Manim requires a few background system tools to render video files (specifically **FFmpeg**) and compile text. Because the setup varies slightly between Windows, Mac, and Linux, it is highly recommended to follow the official, step-by-step installation guide for your operating system:
* [Official Manim Installation Guide](https://docs.manim.community/en/stable/installation.html)

**2. Install the Python Library**
Once FFmpeg and Python are installed on your system, open your terminal and install the Manim package:
```bash
pip install manim
```

---

## 🎬 How to Render an Animation

To generate a video from any of the Python scripts in this repository, open your terminal, navigate to the folder containing the specific script, and use the following command structure:

```bash
manim -pql filename.py SceneClassName
```

### Command Flag Breakdown:
* `manim`: Calls the animation engine.
* `-p`: (Preview) Automatically opens the video player as soon as the rendering is complete.
* `-q`: (Quality) Sets the render resolution and framerate. You must append a letter after it:
  * `l`: Low quality, 480p 15fps (Fastest, best for quick testing)
  * `m`: Medium quality, 720p 30fps
  * `h`: High quality, 1080p 60fps (Recommended for final output)
  * `k`: 4k quality, 2160p 60fps (Very slow)

### An Example Run:
If you are looking at a file named `algorithms.py` and you want to render a scene class inside it called `Dijkstra` in high quality, you would run:

```bash
manim -pqh algorithms.py Dijkstra
```

The finished `.mp4` video will be automatically generated and saved into a local `media/videos/` directory that Manim creates next to the script.