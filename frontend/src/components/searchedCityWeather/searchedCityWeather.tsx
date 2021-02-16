import React from "react";
import WeatherCard from "../weatherCard";
import { Container, Dimmer, Loader, Segment } from "semantic-ui-react";
import { ICityWeather } from "../../types/cityWeather";

interface IProps {
  cityData: ICityWeather | null;
}

export const SearchedCityWeather: React.FC<IProps> = ({ cityData }) => {
  return (
    <Container
      style={{ display: "flex", justifyContent: "center", margin: "50px" }}
    >
      {cityData && (
        <WeatherCard
          city={cityData.city}
          weather={cityData.weather}
          temperature={cityData.temperature}
        />
      )}
    </Container>
  );
};
