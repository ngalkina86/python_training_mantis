from model.project import Project
from selenium.webdriver.support.ui import Select
import time

def test_add_project(app):
  #  project = json_projects
    app.session.login("administrator", "root")
    old_projects = app.soap.list_projects("administrator", "root")
    project =Project(name ="d")
    app.project.create(project)
    new_projects = app.soap.list_projects("administrator", "root")
    old_projects.append(project)
    time.sleep(3)
    assert len(old_projects) + 1 == len(new_projects)
    assert old_projects == new_projects
   



