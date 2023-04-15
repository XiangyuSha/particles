import mujoco
from mujoco import viewer

model = model = mujoco.MjModel.from_xml_path('./particle.xml')

viewer.launch(model=model)
