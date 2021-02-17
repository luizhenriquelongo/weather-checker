import React, { useState } from "react";
import { ICityWeather } from "./types/cityWeather";
import { Grid } from "semantic-ui-react";
import WeatherBuddyAPI from "./api/weatherBuddy";
import SearchedCityWeather from "./components/searchedCityWeather";
import CachedCities from "./components/cachedCities";
import Loader from "./components/loader";
import PageHeader from "./components/pageHeader";
import { DefaultGrid, GridRow } from "./styles/grid";
import SearchBoxContainer from "./components/searchBoxContainer";

const App: React.FC = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(false);
  const [cityData, setCityData] = useState<ICityWeather | null>(null);
  const [cityName, setCityName] = useState("");
  const [cachedCities, setCachedCities] = useState<ICityWeather[]>([]);

  const getCityWeather = async (cityName: string) => {
    setIsLoading(true);
    try {
      const response = await WeatherBuddyAPI.getCityWeather(cityName);
      if (response) {
        setError(false);
        setCityData(response);
      }
    } catch (e) {
      setError(true);
    }
    setIsLoading(false);
  };

  const getCachedCities = async () => {
    const response = await WeatherBuddyAPI.getCachedCities();
    if (response !== undefined) setCachedCities(response);
  };

  const handleKeyPressed = async (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter" && cityName !== "") {
      setCityData(null);
      await getCityWeather(cityName);
      getCachedCities();
    }
  };

  return (
    <DefaultGrid
      columns={1}
      centered
      padded
      textAlign="center"
      verticalAlign="middle"
    >
      <Grid.Column computer={10} largeScreen={8} mobile={16}>
        <Grid.Row>
          <PageHeader title="WEATHER BUDDY" />
        </Grid.Row>

        <GridRow>
          <SearchBoxContainer
            handleKeyPressed={handleKeyPressed}
            setCityName={setCityName}
          />
        </GridRow>

        <Grid.Row>
          {isLoading ? (
            <Loader />
          ) : (
            <SearchedCityWeather cityData={cityData} error={error} />
          )}
        </Grid.Row>

        <Grid.Row>
          <CachedCities cities={cachedCities} />
        </Grid.Row>
      </Grid.Column>
    </DefaultGrid>
  );
};

export default App;
