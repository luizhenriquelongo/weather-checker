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
      style={{
        width: "150px",
        height: "150px",
        marginTop: ".875rem",
        display: "flex",
        flexDirection: "column",
        textAlign: "center",
        margin: ".875rem auto",
      }}
    >
      <Card>
        <Card.Content>
          <Card.Description>{city}</Card.Description>
          <Card.Header style={{ fontSize: "2em", marginTop: ".5rem" }}>
            {temperature}
          </Card.Header>
          <Card.Description>{weather}</Card.Description>
        </Card.Content>
      </Card>
    </Card.Group>
  );
};
