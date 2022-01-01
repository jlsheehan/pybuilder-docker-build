from pybuilder.core import use_plugin, init, Project

use_plugin("python.core")
use_plugin("python.distutils")
use_plugin('pybuilder_docker_build')

name = "simple-package"
version = "0.0.1"

default_task = "publish"


@init
def set_properties(project: Project):
    project.set_property("docker_build_force_rm", True)


@init(environments="cli")
def set_cli_properties(project: Project):
    project.set_property("docker_cli", True)
