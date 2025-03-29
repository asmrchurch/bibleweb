import React from "react";
import GridComponent from "../components/Grid";

const title = "キャラクター紹介";
const data = [
  { id: 1, image: "kirikan.jpg", title: "キリ看ちゃん", description: "キリ看の擬人化として造られたサイボーグ少女。" },
  { id: 2, image: "seisyoyomimiicon.jpg", title: "今だけ聖書よみ美", description: "聖書を読むのにハマっているナイル川出身の女の子。" },
  { id: 3, image: "", title: "", description: "" },
  { id: 4, image: "", title: "", description: "" },
  { id: 5, image: "", title: "", description: "" },
  { id: 6, image: "", title: "", description: "" },
];

const Character = () => {
  return (
    <div>
      <GridComponent data={data} title={title} dir="chars" />
    </div>
  );
};

export default Character;
