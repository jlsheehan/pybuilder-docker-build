import os

from pybuilder.core import use_plugin, init, Project

use_plugin("python.core")
use_plugin('pybuilder_docker_build')

name = "hello-world"
version = "0.0.1"

default_task = "publish"


@init
def set_properties(project: Project):
    project.set_property("docker_build_args", {"EXTRA_ARG": "Extra build arg"})
    project.set_property("docker_image_repo", "dockerhubusername/hello-world")
    # Don't put your credentials in code, look them up from environment or
    # use some other way to pass secrets to your code
    project.set_property(
        "docker_registry_auth",
        {
            "username": os.getenv("DOCKER_HUB_USERNAME"),
            "password": os.getenv("DOCKER_HUB_PASSWORD")
        }
    )
