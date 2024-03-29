PyBuilder Docker Build Plugin
=============================

Summary
-------

This project is a plugin for [PyBuilder](https://pybuilder.io) that will perform a
docker build for a Python package.  _PyBuilder Docker Build Plugin_ attempts to use
sane defaults so that in most cases you only need add a `Dockerfile` to your
project base directory and a docker image will be built when you call
the appropriate task.

Usage
-----

To use this plugin in your `build.py` file add the following line to the
plugins section:

```python
use_plugin('pypi:pybuilder_docker_build')
```

This will add the following tasks to your build:

| Task         | Description                               |
|--------------|-------------------------------------------|
| docker_build | Performs docker build                     |
| docker_save  | Saves docker image to dist dir            |
| docker_push  | Pushes docker image upstream to your repo |

The following properties are available:

| Property              | Value        | Default            | Usage                                                               |
|-----------------------|--------------|--------------------|---------------------------------------------------------------------|
| docker_cli            | True / False | False              | Use docker cli to do build                                          |
| docker_path           | str          | docker             | Path to docker executable                                           |
| docker_build_path     | str          | `basedir` property | Path to docker build directory                                      |
| docker_build_file     | str          | Dockerfile         | Dockerfile to use for build, relative path from `docker_build_path` |
| docker_build_force_rm | True / False | False              | Use the force rm feature of docker build                            |
| docker_image_repo     | str          | `project.name`     | The name of the image repository                                    |
| docker_image_tag      | str          | latest             | A tag to apply to the repository                                    |
| docker_build_args     | dict         | None               | A dict of build args                                                |
| docker_registry_auth  | dict         | None               | A dict containing `username` and `password` for login / auth        |
| docker_registry       | str          | None               | A http / https URL of registry for authentication and push          |

By default there are several build args that are supplied to the docker build, additional args can
be added with the `docker_build_args` property.  The default build args are:

| Argument             | Value                                                                  |
|----------------------|------------------------------------------------------------------------|
| PROJECT_NAME         | `project.name`                                                         |
| PROJECT_VERSION      | `project.version`                                                      |
| PROJECT_DIST_VERSION | `project.dist_version`                                                 |
| PROJECT_DIST_DIR     | The relative path from the `docker_build_path` property to `$dir_dist` |

Authentication
--------------

If you need to push images to a registry then you probably need to set credentials.  Don't
do this directly in your build file but rather look them up from environment or use some other
method for passing secrets to code.  The following is an extract from the `hello-world` sample
project in the `samples` directory:

```python
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
```