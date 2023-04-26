# SimHive
SimHive is the physics simulation library of [RoboHive](https://sites.google.com/view/robohive). It consists of a diverse collection of MuJoCo simulation models designed with care for physical realism.

# Usage instructions
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


# Citation
If you find `SimHive` useful in your research,
- please consider supporting the project by providing a [star ⭐](https://github.com/vikashplus/robohive/stargazers)
- please consider citing our [arXiv paper](https://arxiv.org/abs/2205.13600)  by using the following BibTeX entry:

```BibTeX
@Misc{RoboHive2020,
  title = {RoboHive -- A Unified Framework for Robot Learning},
  howpublished = {\url{https://sites.google.com/view/robohive}},
  year = {2020}
  url = {https://sites.google.com/view/robohive},
}