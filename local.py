import time
from inference import InferencePipeline
from functools import partial
from typing import Union, List, Optional
from inference.core.interfaces.camera.entities import VideoFrame
from inference.core.interfaces.stream.sinks import render_boxes, multi_sink

fall_detected_start_time = None
fall_detection_duration = 3


def custom_alert(
    predictions: Union[any, List[Optional[dict]]],
    video_frame: Union[VideoFrame, List[Optional[VideoFrame]]],
) -> None:
    global fall_detected_start_time
    if not issubclass(type(predictions), list):
        predictions = [predictions]
        video_frame = [video_frame]

    for prediction in predictions:
        if prediction is None:
            continue

        detected_class = prediction["predictions"][0]["class"]
        if detected_class == 'Fall':
            if fall_detected_start_time is None:
                fall_detected_start_time = time.time()
            elif time.time() - fall_detected_start_time >= fall_detection_duration:
                print("Someone fell!!! HELPPP!")
        else:
            fall_detected_start_time = None


on_prediction = partial(multi_sink, sinks=[custom_alert, render_boxes])

pipeline = InferencePipeline.init(
    model_id="fall-detection-v2-ihywg/6",
    video_reference="./examples/fall_detection_1.mp4",
    on_prediction=on_prediction,
    api_key="rOZmS39JRmLDRuDaF8KE",
)
pipeline.start()
pipeline.join()
