# We can also create class or instance method for custom validation
# We 
from pydantic import BaseModel
from pydantic import model_validator, ValidationError

class User(BaseModel):
    name:str
    account_id:int

    # This decorator creates a class function
    @model_validator(mode='after')
    def validate_account_id(self):
        # here mode='after' means validation will be done after the object is created
        # so it's an instance method
        # when mode='before' means validation before the object is created
        # in that case it's a class method, so we use cls instead of self
        if self.account_id <= 0:
            raise ValueError(f"Account id must be positive: {self.account_id}")
        # After the validation we need to return the instance itself
        return self
    
    # Creating another model validator for name
    @model_validator(mode='after')
    def validate_name(self):
        if len(self.name) < 3:
            raise ValueError(f"Name must contain atleast 3 characters: {self.name}")
        return self

try:
    user = User(name='bob', account_id=90)
    print(f"Name: {user.name}")
    print(f"Account name: {user.account_id}")
except ValidationError as ve:
    print(f"Validation error: {ve}")