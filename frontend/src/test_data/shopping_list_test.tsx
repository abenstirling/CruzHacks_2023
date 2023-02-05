import {ShoppingItem} from "../types";

export const ShoppingListTestData: Array<ShoppingItem> = [
  {
    id: "dsjf09dj029jfjflskdjflsjfl",
    is_bought: false,
    item: {
      name: "Tomatoes",
      quantity: 69,
      unit: "none",
      qualifiers: []
    }
  },
  {
    id: "j09jef92j2lkjflwkj",
    is_bought: true,
    item: {
      name: "Potatoes",
      quantity: 42,
      unit: "none",
      qualifiers: []
    }
  },
  {
    id: "j9uoj8j02e9hfj02fh20fh20fh",
    is_bought: true,
    item: {
      name: "Linguini Pasta",
      quantity: 64,
      unit: "ounces",
      qualifiers: []
    }
  },
  {
    id: "0j0ejfojsdfisodjfsofjosf",
    is_bought: false,
    item: {
      name: "Fire-Roasted Canned Tomatoes",
      quantity: 4.0,
      unit: "cans",
      qualifiers: ["16-ounce cans"]
    }
  }
]
