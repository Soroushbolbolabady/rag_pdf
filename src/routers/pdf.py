import os
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from fastapi import UploadFile
from src.pdf_reader.reader import tokenize_pdf


router = APIRouter()


@router.post("/upload_pdf", tags=["pdf"])
async def upload_pdf(files: list[UploadFile]):
                
    try:
        if os.path.exists("./pdf"):
            pass
        else:
            os.mkdir("./pdf")
        

        for item in files:
            file_path = f"./pdf/{item.filename}"
            with open(file_path, "wb") as f:
                f.write(item.file.read())
                f.close()
        return JSONResponse(content = "Files Successfuly uploaded." , status_code=200)
    except FileExistsError:
        return JSONResponse(content="File/File Problem", status_code=422)
