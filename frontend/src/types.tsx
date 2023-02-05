export interface Ingredient {
  name:       string,
  quantity:   number,
  unit:       string,
  qualifiers: Array<string>,
}

export interface Recipe {
  id:          string,
  title:       string,
  url:         URL,
  ingredients: Array<Ingredient>,
  steps:       Array<string>,
  cook_time:   number, // minutes
  author:      string,
  yield:       string,
  nutrition:   NutritionFacts,
}

export interface ShoppingItem {
  id: string,
  is_bought: boolean,
  item: Ingredient,
}


export enum Unit {
  Gram = 1,
  Milligram
}
export interface Quantity {
  amount: number,
  unit: Unit,
}
export interface NutritionFacts {
  calories:     number,
  cholesterol?: Quantity,
  fiber?:       Quantity,
  protein?:     Quantity,
  sat_fat?:     Quantity,
  sugar?:       Quantity,
  fat?:         Quantity,
  unsat_fat?:   Quantity
}
