import React from "react";
import { Block, Button, Columns, Container, Form, Heading, Section, Table } from "react-bulma-components";
import {TestRecipeList} from "../test_data/recipe_list_test";
import {Recipe} from "../types";
import {AiOutlineLink, AiOutlineDelete} from "react-icons/ai"

const RecipeURLInput: React.FC<{}> = (): JSX.Element => {
  return (
    <Section>
      <Heading>Add Recipe</Heading>
      <Form.Control>
        <Form.Field alignContent="center" align="center">
          <Columns alignContent="center">
            <Columns.Column size={11}>
              <Form.Input 
                type={'url'}
                placeholder={'https://natashaskitchen.com/perfect-omelette-recipe/'}
              />
            </Columns.Column>
            <Columns.Column>
              <Button fullwidth={true} color={'success'}>go</Button>
            </Columns.Column>
          </Columns>
        </Form.Field>
      </Form.Control>
    </Section>
  )
}

interface RecipeListProps {
  recipes: Array<Recipe>
}
const RecipeList: React.FC<RecipeListProps> = (props): JSX.Element => {
  return (
    <Section>
      <Heading>This Week's Recipes</Heading>
      <Block alignContent={'center'} alignItems={'center'}>
        <Table size={'fullwidth'} striped={true}>
          <thead>
            <tr>
              <th>Name</th>
              <th>Yield</th>
              <th>Cook Time</th>
              <th>Link</th>
              <th/>
            </tr>
          </thead>
          <tbody>
            {props.recipes.map(r => 
            <tr>
              <td>{r.title}</td>
              <td>{r.yield}</td>
              <td>{r.cook_time} minutes</td>
              <td className="is-centered is-vcentered">
                <a href={r.url.href} target="_blank"><AiOutlineLink className="is-centered"/></a>
              </td>
              <td>
                <Button size={'small'} className='is-vcentered' color=''><AiOutlineDelete/></Button>
              </td>
            </tr>)}
          </tbody>
        </Table>
      </Block>
    </Section>
  )
}

const RecipesPage: React.FC<{}> = (): JSX.Element => {
  return (
    <>
      <Container>
        <RecipeURLInput/>
        <RecipeList recipes={TestRecipeList}/>
      </Container>
    </>
  )
}

export default RecipesPage;
