import sys
import json

input_string = sys.stdin.read()
scene = json.loads(input_string)

frames_col= scene["duration"] / scene["interval"];

scene["frames"] = []

for frame_index in xrange(1, frames_col):
    frame = {}
    for j in range(len(scene["entities"])):
	frame[j] = {}
	frame[j]["x"]=scene["entities"][j]["x"]
	frame[j]["y"]=scene["entities"][j]["y"] + frame_index

    scene["frames"].append(frame)


sys.stdout.write(json.dumps(scene))