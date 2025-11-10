class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors or []
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        if not dependencies:
            return "-"
        return "\n".join(f"- {dep}" for dep in dependencies)
    
    def _stringify_authors(self, authors):
        if not authors:
            return "-"
        return "\n".join(f"- {aut}" for aut in authors)
    

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicence: {self.license}\n"
            f"\nAuthors: \n{self._stringify_authors(self.authors)}\n"
            f"\nDependencies: \n{self._stringify_dependencies(self.dependencies)}\n"
            f"\nDevelopment dependencies: \n{self._stringify_dependencies(self.dev_dependencies)}"
        )
