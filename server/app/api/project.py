from fastapi import APIRouter, Depends, HTTPException

from ..schemas.project import ProjectCreateRequest
from ..providers.project import ProjectProvider
from ..services.project import ProjectImpl
from ..dependencies.auth import get_current_user
from ..models.user import UserModel

router = APIRouter(prefix="/project", tags=["project"])


@router.post("/create_project")
async def create_project(
    request: ProjectCreateRequest,
    current_user: UserModel = Depends(get_current_user),
    project_service: ProjectImpl = Depends(ProjectProvider.get_service),
):
    try:
        project = await project_service.create_project(
            project_name=request.project_name,
            owner_id=current_user.user_id,
        )

        return {
            "project_id": project.project_id,
            "project_name": project.project_name,
            "owner_id": project.owner_id,
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
