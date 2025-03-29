import React from "react";
import GridComponent from "../components/Grid";

const title = "キャラクター紹介";
const data = [
  { id: 1, image: "kirikan.jpg", title: "キリ看ちゃん", description: "キリ看の擬人化として造られたサイボーグ少女。" },
  { id: 2, image: "seisyoyomimiicon.jpg", title: "今だけ聖書よみ美", description: "聖書を読むのにハマっているナイル川出身の女の子。" },
  { id: 3, image: "", title: "Title 3", description: "Description 3" },
  { id: 4, image: "", title: "Title 4", description: "Description 4" },
  { id: 5, image: "", title: "Title 5", description: "Description 5" },
  { id: 6, image: "", title: "Title 6", description: "Description 6" },
];

const Character = () => {
  return (
    <div>
      <GridComponent data={data} title={title} />
    </div>
  );
};

export default Character;
