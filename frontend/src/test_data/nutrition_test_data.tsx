//export interface NutritionFacts {
//  calories:     number,
//  cholesterol?: Quantity,
//  fiber?:       Quantity,
//  protein?:     Quantity,
//  sat_fat?:     Quantity,
//  sugar?:       Quantity,
//  fat?:         Quantity,
//  unsat_fat?:   Quantity
//}

import {NutritionFacts, Unit} from "../types";

export const NutritionTestData: NutritionFacts =
  {
    calories: 800.0,
    cholesterol: {amount: 40, unit: Unit.Milligram},
    fiber: {amount: 20, unit: Unit.Milligram},
    protein: {amount: 10, unit: Unit.Gram},
    sat_fat: {amount: 20, unit: Unit.Gram},
    sugar: {amount: 205, unit: Unit.Milligram},
    fat: {amount: 20, unit: Unit.Gram},
    unsat_fat: {amount: 2330, unit: Unit.Milligram},
  };
