import sys
import json

input_string = sys.stdin.read()
scene = json.loads(input_string)

frames_col= scene["properties"]["interval"] / scene["properties"]["step"];


scene["frames"] = []

for frame_index in xrange(1, frames_col):
    frame = {}
    for entity in scene["entities"]:
	frame[entity] = {}
	frame[entity]["x"]=scene["entities"][entity]["x"]
	frame[entity]["y"]=scene["entities"][entity]["y"] + frame_index

    scene["frames"].append(frame)


sys.stdout.write(json.dumps(scene))