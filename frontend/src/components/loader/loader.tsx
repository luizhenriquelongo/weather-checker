import React from "react";
import { Dimmer, Segment, Loader as SemanticLoader } from "semantic-ui-react";

export const Loader: React.FC = () => {
  return (
    <Dimmer active inverted>
      <SemanticLoader size="large" />
    </Dimmer>
  );
};
