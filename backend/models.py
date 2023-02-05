from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field
from bson import ObjectId


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class UserModel(BaseModel):
    userName: str = Field(...)
    password: str = Field(...)
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}


class IngredientModel(BaseModel):
    name: str = Field(...)
    quantity: float = Field(...)
    unit: str = Field(...)
    qualifiers: list[str] = Field(...)


class ShoppingListItemModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    ingredient: IngredientModel = Field(...)
    is_bought: bool = Field(...)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}


class NutritionQuantity(BaseModel):
    amount: int = Field(...)
    unit: int = Field(...)


class NutritionModel(BaseModel):
    calories: int = Field(...)
    carbohydrateContent: Optional[NutritionQuantity] = Field(...)
    cholesterolContent: Optional[NutritionQuantity] = Field(...)
    fiberContent: Optional[NutritionQuantity] = Field(...)
    proteinContent: Optional[NutritionQuantity] = Field(...)
    sodiumContent: Optional[NutritionQuantity] = Field(...)
    saturatedFatContent: Optional[NutritionQuantity] = Field(...)
    unsaturatedFatContent: Optional[NutritionQuantity] = Field(...)
    fatContent: Optional[NutritionQuantity] = Field(...)


class RecipeModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str = Field(...)
    url: str = Field(...)
    image: str = Field(...)
    ingredients: list[IngredientModel] = Field(...)
    instructions: list[str] = Field(...)
    cook_time: Optional[int] = Field(...)  # minutes
    author: str = Field(...)
    yields: str = Field(...)
    nutrition: NutritionModel

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}
