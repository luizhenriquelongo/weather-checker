import React from "react";
import { Dimmer, Segment, Loader as SemanticLoader } from "semantic-ui-react";

export const Loader: React.FC = () => {
  console.log("loading");
  return (
    <Segment>
      <Dimmer active>
        <SemanticLoader background="#FFF" />
      </Dimmer>
    </Segment>
  );
};
