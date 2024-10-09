# Project Documentation

Welcome to my fall-detection-model documentation. Below, you can find two sections: "Without RTSP" and "With RTSP." Click to expand each section for further details.

<details>
  <summary><strong><span style="font-size: 24px;">Without RTSP (Easier to run)</span></strong></summary>

## 1.If on `python --version` <= 3.11, skip this step

> (Roboflow inference does not work on python 3.12)

If you're using **pyenv**:

```bash
pyenv install --list
```

then install any python version <= 3.11.4

```bash
pyenv install <Python_Version>
pyenv local <Python_Version>
```

If you're using **conda**:

```bash
conda activate my_env
conda install python=3.11.4
```

## 2. Install dependencies and run rtsp.py

```bash
pip install -r ./requirements.txt
python local.py
```

**Notes**

> If you encounter "dll load failed while importing \_cext the specified module could not be found", run the following command:
> `pip install msvc-runtime`

</details>

<details>
  <summary><strong><span style="font-size: 24px;">With RTSP</span></strong></summary>

## 1. Run MediaMtx depending on your system

```bash
cd mediamtx_linux
or
cd mediamtx_mac
or
cd mediamtx_windows

./mediamtx
```

## 2. If you have ffmpeg in your system, skip this step

> I provided the ffmpeg installation files for each system

Mac

```bash
brew install ffmpeg
```

Windows

```
https://www.wikihow.com/Install-FFmpeg-on-Windows
```

## 3. (New Terminal) Run ffmpeg command (Required ffmpeg to be installed)

```bash
ffmpeg -re -stream_loop -1 -i "./examples/fall_detection_1.mp4" -c copy -f rtsp rtsp://localhost:8554/mystream
```

## 4. (New Terminal) If on `python --version` <= 3.11, skip this step

> (Roboflow inference does not work on python 3.12)

If you're using **pyenv**:

```bash
pyenv install --list
```

then install any python version <= 3.11.4

```bash
pyenv install <Python_Version>
pyenv local <Python_Version>
```

## 4. Install dependencies and run rtsp.py

```bash
pip install -r ./requirements.txt
python rtsp.py
```

</details>
