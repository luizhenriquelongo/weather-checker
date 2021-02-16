import React from "react";
import WeatherCard from "../weatherCard";
import { ICityWeather } from "../../types/cityWeather";
import { Wrapper } from "./styles";

interface IProps {
  cityData: ICityWeather | null;
  error: boolean;
}

export const SearchedCityWeather: React.FC<IProps> = ({ cityData, error }) => {
  if (error)
    return (
      <Wrapper>
        <h1>Sorry. We couldn't find the specified city.</h1>
      </Wrapper>
    );
  return (
    <Wrapper>
      {cityData && (
        <WeatherCard
          city={cityData.city}
          weather={cityData.weather}
          temperature={cityData.temperature}
        />
      )}
    </Wrapper>
  );
};
