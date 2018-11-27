from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app


    def can_login(self,username,password):
        client=Client("http://localhost:441/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
           client.service.mc_login(username,password)
           return True
        except WebFault:
            return False


    def list_projects (self,username,password):
        client = Client("http://localhost:441/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        projects = client.service.mc_projects_get_user_accessible(username,password)
        list = []
        for project in projects:
            list.append(Project(id=str(project.id), name=project.name))
        return list

