import React from 'react';
import logo from "./assets/logo_final.jpg";
import { Navbar, Container } from 'react-bulma-components';
import { Outlet, Link } from 'react-router-dom';
import "bulma/css/bulma.css"


function App() {
  return (
      <Container breakpoint={'mobile'}>
        <Navbar>
          <Navbar.Brand>
            <Navbar.Item to="/" renderAs={Link}>
              <img
                alt="Meal planner app"
                src={ logo }
              />
            </Navbar.Item>
        </Navbar.Brand>
          <Navbar.Item  renderAs={Link} to="/recipes">
            Recipes
          </Navbar.Item>
          <Navbar.Item  renderAs={Link} to="/shopping">
            Shopping
          </Navbar.Item>
          <Navbar.Item  renderAs={Link} to="/nutrition">
            Nutrition
          </Navbar.Item>
          <Navbar.Item  renderAs={Link} to="/cook">
            Cook (?)
          </Navbar.Item>
          <Navbar.Container align="right">
            <Navbar.Item href="#">
              Profile
            </Navbar.Item>
          </Navbar.Container>
          <Navbar.Burger />
        </Navbar>

        <Outlet/>
      </Container>
  );
}

export default App;
