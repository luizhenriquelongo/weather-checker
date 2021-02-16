import React from "react";
import { ICityWeather } from "../../types/cityWeather";
import WeatherCard from "../weatherCard";
import { Container } from "semantic-ui-react";

interface IProps {
  cities: ICityWeather[];
}

export const CachedCities: React.FC<IProps> = ({ cities }) => {
  return (
    <Container
      style={{
        width: "800px",
        height: "auto",
        display: "flex",
        flexDirection: "row",
        justifyContent: "space-even",
        alignItems: "center",
        background: "#F2F2F2",
      }}
    >
      {cities &&
        cities.map((city) => (
          <WeatherCard
            key={city.city}
            city={city.city}
            weather={city.weather}
            temperature={city.temperature}
          />
        ))}
    </Container>
  );
};
