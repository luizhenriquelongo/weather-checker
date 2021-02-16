import axios from "axios";
import { axiosConfig } from "./axios/config";
import { ICityWeather } from "../types/cityWeather";

const api = axios.create({
  ...axiosConfig,
  baseURL: `${axiosConfig.baseURL}/api/v1/`,
});

const WeatherBuddyAPI = {
  getCityWeather: async (cityName: string): Promise<ICityWeather | null> => {
    const response = await api.get(`weather/${cityName}`);
    if (response !== undefined) return response.data;
    return null;
  },
  getCachedCities: async (): Promise<ICityWeather[]> => {
    const response = await api.get("weather");
    if (response !== undefined) return response.data;
    return [];
  },
};

export default WeatherBuddyAPI;
