from model.project import Project
import random

def test_delete_project(app):
    app.session.login("administrator", "root")
    if len(app.soap.list_projects("administrator", "root")) == 0:
        app.project.create(Project(name = "variant"))
    old_projects=app.soap.list_projects("administrator", "root")
    project = random.choice(old_projects)
    app.project.delete_project_by_tag()
    new_projects=app.soap.list_projects("administrator", "root")
    assert len(old_projects)-1 == len(new_projects)
    old_projects.remove(project)
    assert old_projects == new_projects

