from model.project import Project
from selenium.webdriver.support.ui import Select

def test_add_project(app,json_projects):
    project = json_projects
    app.session.login("administrator", "root")
    oldCount = app.project.count()
    app.project.create(Project(name ="w1"))
    newCount = app.project.count()
    assert oldCount + 1 == newCount



