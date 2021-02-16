import React from "react";
import { SearchBoxWrapper } from "./styles";

interface IProps {
  handleKeyPressed: (e: React.KeyboardEvent<HTMLInputElement>) => Promise<void>;
  setCityName: (name: string) => void;
}

export const SearchBoxContainer: React.FC<IProps> = ({
  handleKeyPressed,
  setCityName,
}) => {
  return (
    <SearchBoxWrapper fluid text>
      <h3>How is the weather in </h3>
      <input
        name="cityName"
        type="text"
        onChange={(e) => {
          setCityName(e.target.value);
        }}
        onKeyDown={handleKeyPressed}
      />
      <h3> now?</h3>
    </SearchBoxWrapper>
  );
};
