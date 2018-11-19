from model.project import Project
import random

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self,project):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        wd.find_element_by_link_text("Proceed").click()

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def delete_project_by_tag(self):
        wd = self.app.wd
        self.open_manage_page()
        tables = wd.find_elements_by_tag_name("table")
        oldprojects = tables[2].find_elements_by_tag_name("a")
        oldprojects[random.randrange(5, len(oldprojects))].click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()


    def count(self):
        wd = self.app.wd
        self.open_manage_page()
        tables = wd.find_elements_by_tag_name("table")
        return len(tables[2].find_elements_by_tag_name("a")) - 5

    def open_manage_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php") and len(wd.find_elements_by_xpath("//input[@value='Create New Project']")) > 0):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()




