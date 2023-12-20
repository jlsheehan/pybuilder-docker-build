#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init, Project, Author

use_plugin("python.core")
use_plugin("python.flake8")
use_plugin("python.distutils")
use_plugin("pypi:pybuilder_pytest")
use_plugin('pypi:pybuilder_pytest_coverage')
use_plugin("pypi:pybuilder_git_version")

authors = [Author("Jeffrey Sheehan", "jeff.sheehan7@gmail.com")]
summary = "A Docker build plugin for PyBuilder"
url = "https://github.com/jlsheehan/pybuilder-docker-build"
license = "MIT License"

name = "pybuilder-docker-build"
default_task = "publish"


@init
def set_properties(project: Project):
    project.depends_on("docker")
    project.build_depends_on("pytest")
    project.build_depends_on("pytest-mock")
    project.set_property("distutils_readme_description", True)
    project.set_property("distutils_description_overwrite", True)
