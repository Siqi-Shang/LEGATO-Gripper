import os, sys
import argparse

import yaml

import numpy as np
import cv2

cwd = os.getcwd()
sys.path.append(cwd)

from devices.t265 import T265
from devices.button import DemoButtonTest as DemoButton
from hardwares.gripper import Gripper


def test(key_interface=None, gripper=None, streaming=False):

    def quit():
        t265.stop()
        if streaming:
            cv2.destroyAllWindows()

    grasp = 0
    print("Press the fob button or 'b' key to start.")
    while not key_interface.enable and not key_interface.stop:
        pass

    done = False
    initialized = True

    read_time = 0

    t265 = T265()
    t265.start()

    while t265.left is None or t265.right is None:
        pass 

    while not done:

        if t265.time <= read_time + 0.1:
            continue

        trk_pos = t265.pos
        trk_rot = t265.rot
        left_img = np.copy(t265.left)
        right_img = np.copy(t265.right)
        read_time += 0.1

        if initialized:
            initialized = False
            print("Tracking camera initialized... Start now")
            print("Press the fob button more than twice, or press the 's' or 'd' key to quit.")

        if grasp != key_interface.click:
            grasp = key_interface.click
            if grasp:
                gripper.close_gripper()
            else:
                gripper.open_gripper()

        if streaming and not initialized:
            stereo_image = np.concatenate((left_img, right_img), axis=1)
            cv2.imshow("image", stereo_image)
            cv2.waitKey(1)

        done = key_interface.stop or not key_interface.enable

    quit()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--param_file", type=str, default="configs/gripper.yaml")
    parser.add_argument("--streaming", type=int, default=1, help="streaming stereo images")
    args = parser.parse_args()

    param_file = args.param_file
    streaming = args.streaming

    with open (param_file, 'r') as file:
        params = yaml.safe_load(file)

    gripper = Gripper(params)
    key_interface = DemoButton(mode="toggle")

    test(key_interface=key_interface, gripper=gripper, streaming=streaming)

