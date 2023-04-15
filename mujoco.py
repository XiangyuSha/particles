import os
import pytest
import mujoco_py
from mujoco_py import load_model_from_path, MjSim
from mujoco_py.mjviewer import MjViewer
from os.path import dirname


@pytest.mark.requires_rendering
@pytest.mark.requires_glfw
def test_viewer():

    # xml_file = f'phantom3.xml'
    xml_file = f'particle.xml'
    path = os.getcwd()
    xml_path = os.path.join(path, "assets", xml_file)
    model = load_model_from_path(xml_path)
    sim = MjSim(model)
    viewer = MjViewer(sim)
    for _ in range(1000):
        sim.step()
        viewer.render()

test_viewer()


