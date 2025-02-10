# SimHive
SimHive is the physics simulation library of [RoboHive](https://sites.google.com/view/robohive). It consists of a diverse collection of MuJoCo simulation models designed with care for physical realism.

<details>
  <summary>Usage instructions</summary>

  ### Usage instructions
  To benefit from `SimHive`, we strongly encourage our users to -
  - use *SimHive* via [RoboHive](https://sites.google.com/view/robohive)
  - If direct access is required, use [git submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules) link to SimHive (or its subcomponents), instead of copying it over. Submodules allow you to keep *SimHive* as a fully functional repository as a subdirectory to your git repository. Amongst numerous benefits, the ability to easily pull upstream changes from SimHive tops the chart. Its as easy as -
  ``` bash
  # Add entire SimHive as submodule
  git submodule add https://github.com/vikashplus/simhive.git <path/simhive>

  # Add selected module(s): franka_sim
  git submodule add https://github.com/vikashplus/franka_sim.git <path/simhive/franka_sim>
  ```
  The latter example shows how to selectively add modules. See [gitmodules](.gitmodules) files for individual links.
</details>


<details>
  <summary>Citations</summary>

  ### Citation
  If you find `SimHive` useful in your research,
  - please consider supporting the project by providing a [star ⭐](https://github.com/vikashplus/robohive/stargazers)
  - please consider citing our [arXiv paper](https://arxiv.org/abs/2205.13600)  by using the following BibTeX entry:

  ```BibTeX
    @inproceedings{ RoboHive,
      title     = {RoboHive -- A Unified Framework for Robot Learning},
      author    = {Vikash Kumar, Rutav Shah, Gaoyue Zhou, Vincent Moens, Vittorio Caggiano, Jay Vakil, Abhishek Gupta, Aravind Rajeswaran}
      booktitle = {NeurIPS: Conference on Neural Information Processing Systems},
      year      = {2023},
      url       = {https://sites.google.com/view/robohive},
      eprint    = {https://arxiv.org/abs/2310.06828},
    }
  ```
</details>
<br>


# Simulation Models

## [adroit_sim](https://github.com/vikashplus/adroit_sim)
[![projects](https://raw.githubusercontent.com/vikashplus/Adroit/master/gallery/projects.JPG)](https://vikashplus.github.io/)


## [YCB_sim](https://github.com/vikashplus/YCB_sim)
[![projects](https://raw.githubusercontent.com/vikashplus/YCB_sim/master/ycb_objects.png)](https://vikashplus.github.io/)

## [fetch_sim](https://github.com/vikashplus/fetch_sim)
fetch_pole.xml           |  fetch_maneuver.xml       |teleOp_boxes.xml             | teleOp_objects.xml
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
![Alt text](https://raw.githubusercontent.com/vikashplus/fetch_sim/master/gallery/pole.JPG?raw=false "Fetch Pole") |  ![Alt text](https://raw.githubusercontent.com/vikashplus/fetch_sim/master/gallery/maneuver.JPG?raw=false "fetch maneuver") | ![Alt text](https://raw.githubusercontent.com/vikashplus/fetch_sim/master/gallery/boxes.JPG?raw=false "teleOp Boxes") | ![Alt text](https://raw.githubusercontent.com/vikashplus/fetch_sim/master/gallery/objects.JPG?raw=false "teleOp objects")



## [franka_sim](https://github.com/vikashplus/franka_sim)
Franka panda Mujoco models

<table>
  <tr>
    <th width="25%">franka_panda.xml</th>
    <th width="25%">bi-franka_panda.xml</th>
    <th width="25%"></th>
    <th width="25%"></th>
  </tr>
  <tr>
    <td><img src="https://raw.githubusercontent.com/vikashplus/franka_sim/master/franka.png" ></td>
    <td><img src="https://raw.githubusercontent.com/vikashplus/franka_sim/master/bi_franka.png" ></td>
    <td></td>
    <td></td>
  </tr>
</table>

## [furniture_sim](https://github.com/vikashplus/furniture_sim)
MuJoCo simulation for common furnitures

ventionTable.xml |  simpleTable.xml | studyTable.xml | kettle.xml |
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
![Alt text](https://raw.githubusercontent.com/vikashplus/furniture_sim/master/ventionTable/ventionTable.png?raw=false "bin") | ![Alt text](https://raw.githubusercontent.com/vikashplus/furniture_sim/master/simpleTable/simpleTable.png?raw=false "simple table")  |  ![Alt text](https://raw.githubusercontent.com/vikashplus/furniture_sim/master/studyTable/studyTable.png?raw=false "study table")  | ![Alt text](https://raw.githubusercontent.com/vikashplus/furniture_sim/master/kettle/kettles.png?raw=false "kettle") |

hingecabinet.xml           |  slidecabinet.xml | microwave.xml | bin.xml|
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
![Alt text](https://raw.githubusercontent.com/vikashplus/furniture_sim/master/hingecabinet/hingecabinet.png?raw=false "hingecabinet") | ![Alt text](https://raw.githubusercontent.com/vikashplus/furniture_sim/master/slidecabinet/slidecabinet.png?raw=false "slidecabinet")  |  ![Alt text](https://raw.githubusercontent.com/vikashplus/furniture_sim/master/microwave/microwave.png?raw=false "microwave")  | ![Alt text](https://raw.githubusercontent.com/vikashplus/furniture_sim/master/bin/bin.png?raw=false "bin")|

kitchen.xml |  oven.xml | counters.xml | bin.xml  |
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
![Alt text](https://raw.githubusercontent.com/vikashplus/furniture_sim/master/backwall/kitchen.png?raw=false "kitchen") | ![Alt text](https://raw.githubusercontent.com/vikashplus/furniture_sim/master/oven/oven.png?raw=false "oven") | ![Alt text](https://raw.githubusercontent.com/vikashplus/furniture_sim/master/counters/counters.png?raw=false "counters")  | ![Alt text](https://raw.githubusercontent.com/vikashplus/furniture_sim/master/bin/bin.png?raw=false "bin") |
