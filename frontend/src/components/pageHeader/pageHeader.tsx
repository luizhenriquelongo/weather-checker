import React from "react";

interface IProps {
  title: string;
}

export const PageHeader: React.FC<IProps> = ({ title }) => {
  return (
    <h1 style={{ alignSelf: "center", borderBottom: "1px solid #CFCFCF" }}>
      {title}
    </h1>
  );
};
