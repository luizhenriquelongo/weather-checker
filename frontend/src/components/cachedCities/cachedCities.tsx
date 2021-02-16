import React from "react";
import { ICityWeather } from "../../types/cityWeather";
import WeatherCard from "../weatherCard";
import { CachedSegment } from "./styles";

interface IProps {
  cities: ICityWeather[];
}

export const CachedCities: React.FC<IProps> = ({ cities }) => {
  return cities.length > 0 ? (
    <CachedSegment placeholder>
      {cities &&
        cities.map((city) => (
          <WeatherCard
            key={city.city}
            city={city.city}
            weather={city.weather}
            temperature={city.temperature}
          />
        ))}
    </CachedSegment>
  ) : null;
};
