#!/usr/bin/python
import glob
import json

class Positions:
    def __init__(self, positions):
        self.positions = positions

if __name__ == "__main__":
    for f in glob.glob("*.txt"):
        positions = []
        mapName = f.split(".")[0][:-len("_cameras")]
        with open(f, 'r') as camera_file:
            for line in camera_file:
                if line.startswith("//") or line.startswith("\"Cameras\"") \
                or line.startswith("{") or line.startswith("}") or len(line) == 0:
                    continue
                line = line.strip()
                line = line[1 : len(line) - 1]
                line = line.split("\"")
                if (len(line) == 3):
                    positions.append({"name": line[0], "position": line[2]})

        print(positions)
        p = Positions(positions)
        s = json.dumps(p.__dict__)
        with open(f.split(".")[0] + ".json", 'w') as camera_file_output:
            camera_file_output.write(s)

