import React, { useEffect, useState } from "react";
import { ICityWeather } from "./types/cityWeather";
import { Container } from "semantic-ui-react";
import WeatherBuddyAPI from "./api/weatherBuddy";
import SearchedCityWeather from "./components/searchedCityWeather";
import CachedCities from "./components/cachedCities";
import Loader from "./components/loader";
import PageHeader from "./components/pageHeader";

const App: React.FC = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [requestError, setRequestError] = useState("");
  const [cityData, setCityData] = useState<ICityWeather | null>(null);
  const [cityName, setCityName] = useState("");
  const [cachedCities, setCachedCities] = useState<ICityWeather[]>([]);

  const getCityWeather = async (cityName: string) => {
    setIsLoading(true);
    const response = await WeatherBuddyAPI.getCityWeather(cityName);
    if (response) setCityData(response);
    setIsLoading(false);
  };

  useEffect(() => {
    const getCachedCities = async () => {
      const response = await WeatherBuddyAPI.getCachedCities();
      if (response !== undefined) setCachedCities(response);
    };
    getCachedCities();
  }, [cityData]);

  const handleKeyPressed = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter" && cityName !== "") {
      setCityData(null);
      e.preventDefault();
      getCityWeather(cityName);
    }
  };

  return (
    <Container
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        flexDirection: "column",
      }}
    >
      <PageHeader title="WEATHER BUDDY" />

      <div
        style={{
          display: "flex",
          flexDirection: "row",
          alignItems: "center",
          textAlign: "center",
          alignContent: "center",
          height: "2em",
          margin: "0",
          alignSelf: "center",
        }}
      >
        <h2 style={{ margin: "0" }}>How is the weather in </h2>
        <input
          style={{
            height: "2em",
            border: "none",
            borderBottom: "1px solid #CFCFCF",
            margin: "0 10px",
          }}
          name="cityName"
          type="text"
          onChange={(e) => {
            setCityName(e.target.value);
          }}
          onKeyDown={handleKeyPressed}
        />
        <h2 style={{ margin: "0" }}> now?</h2>
      </div>
      {isLoading ? <Loader /> : <SearchedCityWeather cityData={cityData} />}
      <CachedCities cities={cachedCities} />
    </Container>
  );
};

export default App;
