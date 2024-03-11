from models import User, Item
from sqlalchemy.orm import Session
import schemas
import bcrypt


# Create User
def create_user(db: Session, user: schemas.CreateUser):
    hashed_password = bcrypt.hashpw(user.hashed_password.encode('utf-8'), bcrypt.gensalt())

    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    return db_user

# Read User
def read_user_list(db: Session):
    users = db.query(User).all()
    return users

# create item
def create_item(db: Session, item: schemas.CreateItem, user_id: int):
    item = Item(title=item.title, description=item.description, owner_id=user_id)
    db.add(item)
    db.commit()
    return item

# ResponseValidationError(
#     fastapi.exceptions.ResponseValidationError: 1 validation errors:
#         {
#             'type': 'model_attributes_type', 
#             'loc': ('response',), 
#             'msg': 'Input should be a valid dictionary or object to extract fields from', 
#             'input': [<models.User object at 0x1056b3320>, <models.User object at 0x1056400b0>], 
#             'url': 'https://errors.pydantic.dev/2.6/v/model_attributes_type'
#         }
# )