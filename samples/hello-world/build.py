from pybuilder.core import use_plugin, init, Project

use_plugin("python.core")
use_plugin('pybuilder_docker_build')

name = "hello-world"
version = "0.0.1"

default_task = "publish"


@init
def set_properties(project: Project):
    project.set_property("docker_cli", True)
    # pass
