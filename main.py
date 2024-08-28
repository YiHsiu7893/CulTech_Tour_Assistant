"""
Ref:
https://arxiv.org/pdf/2208.10926
https://ieeexplore.ieee.org/abstract/document/7407826
"""
from audio import STT
from avatar import Avatar
import cv2


if __name__ == '__main__':
    avatar = Avatar()

    while True:
        key = cv2.waitKey(0)
        if key == ord('q'):  # End of conversation loop.
            break

        q = STT()
        a = avatar.thinking(q)

        avatar.simulation(a)