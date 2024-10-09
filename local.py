# Import the InferencePipeline object
from inference import InferencePipeline

# Import the built in render_boxes sink for visualizing results
from inference.core.interfaces.stream.sinks import render_boxes

# initialize a pipeline object
pipeline = InferencePipeline.init(
    model_id="fall-detection-v2-ihywg/6",
    # Path to video, device id (int, usually 0 for built in webcams), or RTSP stream url
    video_reference="./examples/fall_detection_1.mp4",
    on_prediction=render_boxes,
    api_key="rOZmS39JRmLDRuDaF8KE",
)
pipeline.start()
pipeline.join()
