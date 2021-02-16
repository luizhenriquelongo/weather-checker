import React, { useEffect, useState } from "react";
import { ICityWeather } from "./types/cityWeather";
import { Container } from "semantic-ui-react";
import WeatherBuddyAPI from "./api/weatherBuddy";
import SearchedCityWeather from "./components/searchedCityWeather";
import CachedCities from "./components/cachedCities";
import Loader from "./components/loader";
import { Simulate } from "react-dom/test-utils";

const App: React.FC = () => {
  const [loading, setLoading] = useState(false);
  const [requestError, setRequestError] = useState("");
  const [cityData, setCityData] = useState<ICityWeather | null>(null);
  const [cityName, setCityName] = useState("");
  const [cachedCities, setCachedCities] = useState<ICityWeather[]>([]);

  const getCityWeather = (cityName: string) => {
    const response = WeatherBuddyAPI.getCityWeather(cityName);
    if (response) {
      response
        .then((response) => {
          setCityData(response);
        })
        .catch((error) => setRequestError(error));
    }
  };

  useEffect(() => {
    const getCachedCities = () => {
      const response = WeatherBuddyAPI.getCachedCities();
      if (response !== undefined) {
        response
          .then((response) => {
            setCachedCities(response);
          })
          .catch((error) => setRequestError(error));
      }
    };
    getCachedCities();
  }, [cityData]);

  const handleKeyPressed = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter" && cityName !== "") {
      setLoading(true);
      setCityData(null);
      e.preventDefault();
      getCityWeather(cityName);
      setLoading(false);
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
      <h1 style={{ alignSelf: "center" }}>WEATHER BUDDY</h1>

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
            borderBottom: "1px solid #000",
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
      {loading ? <Loader /> : <SearchedCityWeather cityData={cityData} />}
      <CachedCities cities={cachedCities} />
    </Container>
  );
};

export default App;
