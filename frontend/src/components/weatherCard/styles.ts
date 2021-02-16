import styled from "styled-components";
import { Card } from "semantic-ui-react";

export const CardGroup = styled(Card.Group)`
  width: 160px;
  display: flex !important;
  flex-direction: column;
  text-align: center;
  margin: 0.875rem !important;
`;

export const CardHeader = styled(Card.Header)`
  font-size: 2em !important;
  margin-top: 0.8rem !important;

  ::before {
    height: 0 !important;
  }
`;
