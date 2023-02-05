import React from "react";
import { Container, Content } from "react-bulma-components";
import { useRouteError } from "react-router-dom";

const ErrorPage: React.FC<{}> = (): JSX.Element => {
  const error: any = useRouteError();
  console.error(error);

  return (
    <Container breakpoint={'mobile'}>
      <Content className="has-text-centered">
        <h1>Oops!</h1>
        <p>Sorry, an unexpected error has occurred.</p>
        <p>
          <i>{error.statusText || error.message}</i>
        </p>
      </Content>
    </Container>
  )
}

export default ErrorPage;
