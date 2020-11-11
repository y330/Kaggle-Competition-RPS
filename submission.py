# File name: submission.py
# Authors: avivy
# Date created: 2020-11-05
# Modified: 6:31 p.m.
def copy_opponent_agent (observation, configuration):
    if observation.step > 0:
        return observation.lastOpponentAction
    else:
        return 0
