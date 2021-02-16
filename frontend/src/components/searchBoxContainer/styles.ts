import styled from "styled-components";
import { Container } from "semantic-ui-react";

export const SearchBoxWrapper = styled(Container)`
  display: flex !important;
  flex-direction: row;
  align-items: center;
  justify-content: center;

  h3 {
    margin: 0;
  }

  input {
    height: 2em;
    border: none;
    border-bottom: 1px solid #cfcfcf;
    margin: 0 10px;
  }
`;
