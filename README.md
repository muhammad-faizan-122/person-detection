# Detect the Person in Video
![demo video](config/demo.gif)
## Usage 
- Place input video in **data/input** directory.
- Set the input video path in **config/yolov8.yml**.
- Yolov8l Trained model is fine-tune on COCO dataset, which contain 128 and first class is for person. We are just using detecting person.
- Create the conda env using 
    ```
    conda create -n env_name python=3.10
    conda activate env_name
    ```
- Install requirements using following command.
    ```
    pip install -r requirements.txt
    ```
- python3 main.py