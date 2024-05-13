import React, { memo } from "react";
import ReactWordcloud from "react-wordcloud";
import "tippy.js/dist/tippy.css";
import "tippy.js/animations/scale.css";

const WordCloud = ({ data }) => {
  return (
    <ReactWordcloud
      words={data}
      options={{ fontSizes: [11, 73] }}
      size={[950, 450]}
    />
  );
};

export default memo(WordCloud);
