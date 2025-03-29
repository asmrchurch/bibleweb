import React from "react";
import GridComponent from "../components/Grid";

const title = "聖書Q＆A";
const data = [
  { id: 1, image: "asmrchurch_jesus_christ_face_wester_drawins_ultra_realistic_pho_4217d174-324c-4f09-b96f-4002a6940f3c.png", title: "憎しみから自由になる", description: "私たちの人生には、傷つくことや裏切られることがあり、心の中に憎しみや怒りが湧き上がることがあります。しかし、憎しみは私たちの心を重くし、神様が用意された喜びから遠ざけてしまいます。でも、大丈夫！神様は私たちが「憎しみから自由になる」ための方法を備えてくださっています。", url: "blog/31" },
  { id: 2, image: "asmrchurch_jesus_christ_face_wester_drawins_ultra_realistic_pho_96252701-12f3-4151-80e1-01751e370432.png", title: "逆境と人生の困難に向き合う", description: "人生にはさまざまな困難がつきものです。健康の問題、人間関係の葛藤、経済的な苦境、精神的な不安など、私たちは生きていく中で何度も試練に直面します。しかし、カトリックの信仰においては、逆境は単なる不幸ではなく、神との関係を深める機会として捉えられます。", url: "blog/32" },
  { id: 3, image: "asmrchurch_jesus_christ_face_wester_drawins_ultra_realistic_pho_cdfe76a1-0a81-4cf5-aadb-2d5ecefa3e25.png", title: "理想の暮らしをかなえるために", description: "私たちは誰しも「理想の暮らし」を求めます。健康でありたい、愛する家族や友人とともに過ごしたい、経済的に安定したい、そして平和のうちに人生を送りたい。これらの願いは自然なものであり、神が私たちに与えた「より良い人生への探求心」とも言えます。 ", url: "blog/33" },
  { id: 4, image: "asmrchurch_jesus_christ_western_drawings_d9609ad9-1c03-4c04-8eee-a9eb91cc6022.png", title: "使徒信条", description: "キリスト教の信仰を正しく理解し、健全な教えのもとに歩むためには、三位一体 と 使徒信条 という神学的な基礎をしっかりと押さえることがとても大切です。これらは、初代教会以来、キリスト教の正統な信仰として受け継がれ、多くの教会で共有されてきた中心的な教えです。", url: "blog/34" },

];

const Qa = () => {
  return (
    <div>
      <GridComponent data={data} title={title} dir="qa" />
    </div>
  );
};

export default Qa;

