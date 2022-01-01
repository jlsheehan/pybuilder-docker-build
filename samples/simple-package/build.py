from pybuilder.core import use_plugin, init, Project

use_plugin("python.core")
use_plugin("python.distutils")
use_plugin('pybuilder_docker_build')

name = "simple-package"
version = "0.0.1"

default_task = "publish"


@init
def set_properties(project: Project):
    # uncomment this to try docker cli instead of
    # python docker api
    # project.set_property("docker_cli", True)
    pass