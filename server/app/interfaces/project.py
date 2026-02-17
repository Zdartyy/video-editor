from abc import ABC, abstractmethod
from ..models.project import ProjectModel


class Project(ABC):
    @abstractmethod
    async def create_project(self, project_name: str, owner_id: int) -> ProjectModel:
        """Creates a new project for given owner"""
        raise NotImplementedError
