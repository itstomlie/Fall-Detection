# Project Documentation

Welcome to my fall-detection-model documentation. Below, you can find two sections: "Without RTSP" and "With RTSP." Click to expand each section for further details.

<details>
  <summary><strong><span style="font-size: 24px;">Without RTSP (Easier to run)</span></strong></summary>

## 1. Switch to python version <= 3.11.4 (Roboflow inference does not work on python 3.12) & Run local.py

If you're using pyenv:

```bash
pyenv install 3.11.4
pyenv local 3.11.4
eval "$(pyenv init -)"

pip install -r ./requirements.txt
python local.py
```

</details>

<details>
  <summary><strong><span style="font-size: 24px;">With RTSP</span></strong></summary>

## 1. Run MediaMtx

```bash
cd mediamtx
./mediamtx
```

## 2. (New Terminal) Run ffmpeg command (Required ffmpeg to be installed)

```bash
ffmpeg -re -stream_loop -1 -i "./examples/fall_detection_1.mp4" -c copy -f rtsp rtsp://localhost:8554/mystream
```

## 3. (New Terminal) Switch to python version <= 3.11.4 (Roboflow inference does not work on python 3.12) & Run local.py

If you're using pyenv:

```bash
pyenv install 3.11.4
pyenv local 3.11.4
eval "$(pyenv init -)"

pip install -r ./requirements.txt
python rtsp.py
```

</details>
