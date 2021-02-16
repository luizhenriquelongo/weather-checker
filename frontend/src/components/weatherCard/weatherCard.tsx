import React from "react";
import { Card } from "semantic-ui-react";
import { CardGroup, CardHeader } from "./styles";
import { ICityWeather } from "../../types/cityWeather";

export const WeatherCard: React.FC<ICityWeather> = ({
  city,
  weather,
  temperature,
}) => {
  return (
    <CardGroup>
      <Card>
        <Card.Content>
          <Card.Description>{city}</Card.Description>
          <CardHeader>{temperature}</CardHeader>
          <Card.Description>{weather}</Card.Description>
        </Card.Content>
      </Card>
    </CardGroup>
  );
};
