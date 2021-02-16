import React from "react";
import { Header } from "./styles";

interface IProps {
  title: string;
}

export const PageHeader: React.FC<IProps> = ({ title }) => {
  return <Header>{title}</Header>;
};
