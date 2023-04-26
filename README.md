# SimHive
SimHive is the physics simulation library of [RoboHive](https://sites.google.com/view/robohive). It consists of a diverse collection of MuJoCo simulation models designed with care for physical realism.

# Usage instructions
To benefit from `SimHive`, we strongly encourage our users to -
- use *SimHive* via [RoboHive](https://sites.google.com/view/robohive)
- If direct access is required, use [git submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules) link to SimHive (or its subcomponents), instead of copying it over. Submodules allow you to keep *SimHive* as a fully functional repository as a subdirectory to your git repository. Amongst numerous benefits, the ability to easily pull upstream changes from SimHive tops the chart. Its a easy as -
``` bash
# Add entire SimHive as submodule
git submodule add https://github.com/vikashplus/simhive.git <simhive_folder_path>

# Add selected modules (franka_sim) in your project
git submodule add https://github.com/vikashplus/franka_sim.git
```
The latter example shows how to selectively add modules. See [gitmodules](.gitmodules) files for individual links.