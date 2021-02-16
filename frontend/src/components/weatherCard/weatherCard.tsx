import React from "react";
import { Card } from "semantic-ui-react";
import { ICityWeather } from "../../types/cityWeather";

export const WeatherCard: React.FC<ICityWeather> = ({
  city,
  weather,
  temperature,
}) => {
  return (
    <Card.Group
      style={{ width: "150px", height: "150px", marginTop: ".875rem" }}
    >
      <Card>
        <Card.Content>
          <Card.Description>{city}</Card.Description>
          <Card.Header>{temperature}</Card.Header>
          <Card.Description>{weather}</Card.Description>
        </Card.Content>
      </Card>
    </Card.Group>
  );
};
