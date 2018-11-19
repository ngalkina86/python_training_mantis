from model.project import Project

def test_delete_project(app):
    app.session.login("administrator", "root")
    if app.project.count() == 0:
        app.project.create(Project(name = "variant"))
    oldCount = app.project.count()
    app.project.delete_project_by_tag()
    newCount = app.project.count()
    assert oldCount - 1 == newCount
