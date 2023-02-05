import React from "react";
import {Heading, Section, Table, Form} from "react-bulma-components";
import {TestRecipeList} from "../test_data/recipe_list_test";
import { Quantity, Recipe, Unit } from "../types";


// export interface NutritionFacts {
//   calories:     number,
//   cholesterol?: Quantity,
//   fiber?:       Quantity,
//   protein?:     Quantity,
//   sat_fat?:     Quantity,
//   sugar?:       Quantity,
//   fat?:         Quantity,
//   unsat_fat?:   Quantity
// }


interface StringifedNutritionFacts {
  title:       string,
  calories:    string,
  cholesterol: string,
  fiber:       string,
  protein:     string,
  sat_fat:     string,
  sugar:       string,
  fat:         string,
  unsat_fat:   string,
}

const unitToString = (unit: Unit): string => {
  if (unit === Unit.Gram) {
    return "g";
  }
  else {
    return "mg";
  }
}

const quantityToString = (qty?: Quantity): string => {
  if (typeof qty !== 'undefined') {
    return qty.amount.toString() + unitToString(qty.unit);
  }
  return "-";
}

const stringifyNutrition = (r: Recipe): StringifedNutritionFacts => {
  let facts = r.nutrition;
  return {
    title: r.title,
    calories: facts.calories.toString(),
    cholesterol: quantityToString(facts.cholesterol),
    fiber: quantityToString(facts.fiber),
    protein: quantityToString(facts.protein),
    sat_fat: quantityToString(facts.sat_fat),
    sugar: quantityToString(facts.sugar),
    fat: quantityToString(facts.fat),
    unsat_fat: quantityToString(facts.unsat_fat)
  }
}

const sumIfPresent = (qty?: Quantity, qty2?: Quantity): Quantity => {
  if (typeof qty !== 'undefined' && typeof qty2 !== 'undefined') {
    let normalized: number = (qty2.unit === Unit.Milligram) ? qty2.amount / 1000 : qty2.amount;

    return {
      amount: qty.amount + normalized,
      unit: Unit.Gram
    }
  }
  else if (typeof qty2 === 'undefined' && typeof qty !== 'undefined') {
    return qty;
  }


  return {
    amount: 0,
    unit: Unit.Gram
  }
}

interface NutritionTableProps {
  facts: Array<Recipe>
}
const NutritionTable: React.FC<NutritionTableProps> = (p): JSX.Element => {
  let sum_facts = p.facts.map(r => r.nutrition).reduce((acc, n) => {return {
    calories: acc.calories + n.calories,
    cholesterol: sumIfPresent(acc.cholesterol, n.cholesterol),
    fiber: sumIfPresent(acc.fiber, n.fiber),
    protein: sumIfPresent(acc.protein, n.protein),
    sat_fat: sumIfPresent(acc.sat_fat, n.sat_fat),
    sugar: sumIfPresent(acc.sugar, n.sugar),
    fat: sumIfPresent(acc.fat, n.fat),
    unsat_fat: sumIfPresent(acc.unsat_fat, n.unsat_fat)
  }});

  return (
    <Section>
      <Heading>
        Nutrition
      </Heading>
      <Table size={'fullwidth'} striped={true}>
        <tr>
          <th>Recipe</th>
          <th>Calories</th>
          <th>Cholesterol</th>
          <th>Fiber</th>
          <th>Protein</th>
          <th>Fat</th>
          <th>Saturated Fat</th>
          <th>Unsaturated Fat</th>
          <th>Sugar</th>
        </tr>
        {p.facts.map(stringifyNutrition).map(f => <tr>
          <td>{f.title}</td>
          <td>{f.calories}</td>
          <td>{f.cholesterol}</td>
          <td>{f.fiber}</td>
          <td>{f.protein}</td>
          <td>{f.fat}</td>
          <td>{f.sat_fat}</td>
          <td>{f.unsat_fat}</td>
          <td>{f.sugar}</td>
        </tr>)}
        <tr>
          <th>Total</th>
          <td>{sum_facts.calories}</td>
          <td>{quantityToString(sum_facts.cholesterol)}</td>
          <td>{quantityToString(sum_facts.fiber)}</td>
          <td>{quantityToString(sum_facts.protein)}</td>
          <td>{quantityToString(sum_facts.fat)}</td>
          <td>{quantityToString(sum_facts.sat_fat)}</td>
          <td>{quantityToString(sum_facts.unsat_fat)}</td>
          <td>{quantityToString(sum_facts.sugar)}</td>
        </tr>
      </Table>
    </Section>
  )
}

const NutritionPage: React.FC<{}> = (): JSX.Element => {
  return (
    <>
      <NutritionTable facts={TestRecipeList}/>
    </>
  )
}

export default NutritionPage;
