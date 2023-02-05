import React from "react";
import {Heading, Section, Table, Form} from "react-bulma-components";
import {ShoppingListTestData} from "../test_data/shopping_list_test";
import { ShoppingItem } from "../types";

interface ShoppingListProps {
  items: Array<ShoppingItem>;
}
const ShoppingList: React.FC<ShoppingListProps> = (props): JSX.Element => {
  return (
    <Section>
      <Heading>
        Shopping List
      </Heading>
      <Table size={'fullwidth'} striped={true}>
        <tr>
          <th>Item</th>
          <th>Quantity</th>
          <th>Notes</th>
          <th>Bought?</th>
        </tr>
        {props.items.map(item => <tr>
          <td>{item.item.name}</td>
          <td>{item.item.quantity}</td>
          <td>{item.item.qualifiers.join(", ")}</td>
          <td><Form.Checkbox checked={item.is_bought}/></td>
        </tr>)}
      </Table>
    </Section>
  )
}

const ShoppingPage: React.FC<{}> = (): JSX.Element => {
  return (
    <>
      <ShoppingList items={ShoppingListTestData}/>
    </>
  )
}

export default ShoppingPage;
