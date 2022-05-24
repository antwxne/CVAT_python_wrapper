# CVAT wrapper

## Description

Python wrapper to wrap CVAT API call into a class.

## Example

```python
from CVAT import CVAT
from CVAT.data_types import Task

API = CVAT(username="username", password="password", url="http://localhost:8080")

project_id: int = API.create_project("New project")
task: Task = Task("new task", project_id=project_id)
task = API.create_task(task)
```

## Documentation

All the documentation is made with _python google docstring_.

## Contributeurs

- Antoine Desruet [![github-link][github-logo]](https://github.com/antwxne)


<!-- Markdown link & img definition's -->

[Github-logo]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
