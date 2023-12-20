import logging
import os

from pybuilder.core import Project

from pybuilder_docker_build import util

logger = logging.getLogger(__name__)


def test_full_image_tag(mocker):
    properties = {
        "docker_image_repo": "test-repo",
        "docker_image_tag": "image_tag"
    }
    project = mocker.Mock(Project)
    project.get_property.side_effect = properties.get
    assert util._full_image_tag(project) == "test-repo:image_tag"


def test_empty_build_args(mocker):
    os.path.relpath = mocker.Mock()
    os.path.relpath.return_value = "target/dist/test-project-0.0.1"
    project = mocker.Mock(Project)
    project.name = "test-project"
    project.version = "0.0.1"
    project.dist_version = "0.0.1"
    project.expand_path.return_value = "target/dist/test-project-0.0.1"
    project.has_property.return_value = False
    result = {
        "PROJECT_NAME": "test-project",
        "PROJECT_VERSION": "0.0.1",
        "PROJECT_DIST_VERSION": "0.0.1",
        "PROJECT_DIST_DIR": "target/dist/test-project-0.0.1"
    }
    assert util._build_args(project, logger) == result


def test_build_args(mocker):
    os.path.relpath = mocker.Mock()
    os.path.relpath.return_value = "target/dist/test-project-0.0.1"

    project = mocker.Mock(Project)
    project.name = "test-project"
    project.version = "0.0.1"
    project.dist_version = "0.0.1"
    project.expand_path.return_value = "target/dist/test-project-0.0.1"
    project.has_property.return_value = True
    project.get_property.return_value = {
        "EXTRA": "extra",
        "ARG": "arg"
    }
    result = {
        "PROJECT_NAME": "test-project",
        "PROJECT_VERSION": "0.0.1",
        "PROJECT_DIST_VERSION": "0.0.1",
        "PROJECT_DIST_DIR": "target/dist/test-project-0.0.1",
        "EXTRA": "extra",
        "ARG": "arg"
    }
    assert util._build_args(project, logger) == result

