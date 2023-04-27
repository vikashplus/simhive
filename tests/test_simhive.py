import unittest
import os
import glob

try:
    import mujoco_py
    from mujoco_py import load_model_from_path, MjSim, load_model_from_xml
except ImportError as e:
    raise ImportError("(HINT: you need to install mujoco_py, and also perform the setup instructions here: https://github.com/openai/mujoco-py/.)")

curr_dir = os.path.dirname(os.path.abspath(__file__))

class TestSims(unittest.TestCase):

    def get_sim(self, model_path:str=None, model_xmlstr=None):
        """
        Get sim using model_path or model_xmlstr.
        """
        if model_path:
            if model_path.startswith("/"):
                fullpath = model_path
            else:
                fullpath = os.path.join(os.path.dirname(__file__), model_path)
            if not os.path.exists(fullpath):
                raise IOError("File %s does not exist" % fullpath)
            model = load_model_from_path(fullpath)
        elif model_xmlstr:
            model = load_model_from_xml(model_xmlstr)
        else:
            raise TypeError("Both model_path and model_xmlstr can't be None")

        return MjSim(model)


    def test_adroit_sim(self):
        model_paths = glob.glob(curr_dir+"/../simhive/Adroit/*.xml")
        print(model_paths)
        print("\nSimHive: Tesing Adroit")
        for model_path in model_paths:
            print("\t{}".format(model_path))
            self.get_sim(model_path)


    def test_dmanus_sim(self):
        model_paths = glob.glob(curr_dir+"/../simhive/dmanus_sim/*.xml")
        print("\nSimHive: Tesing D'Manus")
        for model_path in model_paths:
            print("\t{}".format(model_path))
            self.get_sim(model_path)


    def test_fetch_sim(self):
        model_paths = glob.glob(curr_dir+"/../simhive/fetch_sim/*.xml")
        print("\nSimHive: Tesing Fetch")
        for model_path in model_paths:
            print("\t{}".format(model_path))
            self.get_sim(model_path)


    def test_franka_sim(self):
        model_paths = glob.glob(curr_dir+"/../simhive/franka_sim/*.xml")
        print("\nSimHive: Tesing Franka")
        for model_path in model_paths:
            print("\t{}".format(model_path))
            self.get_sim(model_path)


    def test_furniture_sim(self):
        model_paths = glob.glob(curr_dir+"/../simhive/furniture_sim/*.xml")
        print("\nSimHive: Tesing Furniture Sim")
        for model_path in model_paths:
            print("\t{}".format(model_path))
            self.get_sim(model_path)


    def test_myo_sim(self):
        model_paths = glob.glob(curr_dir+"/../simhive/myo_sim/*/*.xml")

        print("\nSimHive: Tesing Myo")
        for model_path in model_paths:
            print("\t{}".format(model_path))
            self.get_sim(model_path)


    def test_object_sim(self):
        model_paths = glob.glob(curr_dir+"/../simhive/object_sim/*.xml")

        print("\nSimHive: Tesing Objects")
        for model_path in model_paths:
            print("\t{}".format(model_path))
            self.get_sim(model_path)


    def test_robel_sim(self):
        model_paths = glob.glob(curr_dir+"/../simhive/robel_sim/d*/*.xml")

        print("\nSimHive: Tesing ROBEL")
        for model_path in model_paths:
            print("\t{}".format(model_path))
            self.get_sim(model_path)


    def test_robotiq_sim(self):
        model_paths = glob.glob(curr_dir+"/../simhive/robotiq_sim/*.xml")

        print("\nSimHive: Tesing RobotiQ")
        for model_path in model_paths:
            print("\t{}".format(model_path))
            self.get_sim(model_path)


    def test_sawyer_sim(self):
        model_paths = glob.glob(curr_dir+"/../simhive/sawyer_sim/*.xml")

        print("\nSimHive: Tesing Sawyer")
        for model_path in model_paths:
            print("\t{}".format(model_path))
            self.get_sim(model_path)


    def test_scene_sim(self):
        model_paths = glob.glob(curr_dir+"/../simhive/scene_sim/*.xml")

        print("\nSimHive: Tesing Scene")
        for model_path in model_paths:
            print("\t{}".format(model_path))
            self.get_sim(model_path)


    def test_trifinger_sim(self):
        model_paths = glob.glob(curr_dir+"/../simhive/trifinger_sim/trifinger.xml")

        print("\nSimHive: Tesing Trifinger")
        for model_path in model_paths:
            print("\t{}".format(model_path))
            self.get_sim(model_path)


    def test_ycb_sim(self):
        model_paths = glob.glob(curr_dir+"/../simhive/YCB_sim/*.xml")

        print("\nSimHive: Tesing YCB")
        for model_path in model_paths:
            print("\t{}".format(model_path))
            self.get_sim(model_path)


if __name__ == '__main__':
    unittest.main()

