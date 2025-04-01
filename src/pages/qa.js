import React from "react";
import GridComponent from "../components/Grid";

const title = "聖書Q＆A";
const data = [
  { id: 1, image: "asmrchurch_jesus_christ_face_wester_drawins_ultra_realistic_pho_4217d174-324c-4f09-b96f-4002a6940f3c.png", title: "憎しみから自由になる", description: "私たちの人生には、傷つくことや裏切られることがあり、心の中に憎しみや怒りが湧き上がることがあります。しかし、憎しみは私たちの心を重くし、神様が用意された喜びから遠ざけてしまいます。でも、大丈夫！神様は私たちが「憎しみから自由になる」ための方法を備えてくださっています。", url: "blog/31" },
  { id: 2, image: "asmrchurch_jesus_christ_face_wester_drawins_ultra_realistic_pho_96252701-12f3-4151-80e1-01751e370432.png", title: "逆境と人生の困難に向き合う", description: "人生にはさまざまな困難がつきものです。健康の問題、人間関係の葛藤、経済的な苦境、精神的な不安など、私たちは生きていく中で何度も試練に直面します。しかし、カトリックの信仰においては、逆境は単なる不幸ではなく、神との関係を深める機会として捉えられます。", url: "blog/32" },
  { id: 3, image: "asmrchurch_jesus_christ_face_wester_drawins_ultra_realistic_pho_cdfe76a1-0a81-4cf5-aadb-2d5ecefa3e25.png", title: "理想の暮らしをかなえるために", description: "私たちは誰しも「理想の暮らし」を求めます。健康でありたい、愛する家族や友人とともに過ごしたい、経済的に安定したい、そして平和のうちに人生を送りたい。これらの願いは自然なものであり、神が私たちに与えた「より良い人生への探求心」とも言えます。 ", url: "blog/33" },
  { id: 4, image: "asmrchurch_jesus_christ_western_drawings_d9609ad9-1c03-4c04-8eee-a9eb91cc6022.png", title: "使徒信条", description: "キリスト教の信仰を正しく理解し、健全な教えのもとに歩むためには、三位一体 と 使徒信条 という神学的な基礎をしっかりと押さえることがとても大切です。これらは、初代教会以来、キリスト教の正統な信仰として受け継がれ、多くの教会で共有されてきた中心的な教えです。", url: "blog/34" },
  { id: 5, image: "asmrchurch_jesus_christ_ultra_realistic_photo_western_drawings_0c0a72a8-a811-4b6c-89b7-6f7abda17979.png", title: "ダニエルについて聖書はどんなことを教えていますか", description: "ダニエル書は、旧約聖書の中でも特に象徴的で預言的な書物であり、ルター派の伝統においても重要な意味を持っています。マルティン・ルターはダニエル書を「聖なる、素晴らしい書」と呼び、その中に神の主権と福音の約束を見出しました。本稿では、ルター派の視点からダニエル書の主要な教えについて考察します。", url: "blog/36" },
  { id: 6, image: "asmrchurch_jesus_christ_ultra_realistic_photo_western_drawings_27fe1011-15c8-47ed-ad54-b1e3a7dc9261.png", title: "だれが聖書を書いたかは分かりますか", description: "聖書はキリスト教の信仰の中心にある聖なる書物ですが、その著者についての問いは多くの人々が抱くものです。カトリック教会の教えによれば、聖書は神の霊感によって書かれたものであり、その著者は単なる人間ではなく、神ご自身が根本的な著者であると理解されています。", url: "blog/36" },
  { id: 7, image: "asmrchurch_jesus_christ_ultra_realistic_photo_western_drawings_38dc21fa-d0bc-4689-b91b-5c8685a06e33.png", title: "「善きサマリア人」になるとはどういうことですか", description: "「善きサマリア人」のたとえ（ルカ10:25-37）は、イエス・キリストが私たちに隣人愛を教えるために語られた重要な教えです。セブンスデー・アドベンチスト（SDA）の信仰では、この物語は単なる道徳的な教訓にとどまらず、キリストの福音と終末時代に生きる私たちの使命に深く結びついている と理解されます。", url: "blog/38" },
  { id: 8, image: "asmrchurch_ultra_realistic_photo_jesus_christ_western_drawings__32bce1ce-43b9-49b1-8adc-d06d7f38a597.png", title: "大患難とは何ですか", description: "「大患難（Great Tribulation）」とは、キリスト教において特に終末論（エスカトロジー）に関する概念であり、多くの福音派・ディスペンセーション主義の伝統では、終末における極度の苦難と神の裁きを指すものとして理解されてきました（マタイ24:21、黙示録7:14）。", url: "blog/39" },
  { id: 9, image: "asmrchurch_ultra_realistic_photo_jesus_christ_western_drawings__55bddf41-ae6f-4fda-9ea9-c90a8464fca2.png", title: "イエスは全能の神ですか", description: "カトリック教会は、イエス・キリストは「全能の神」である という信仰を明確に持っています。ニカイア・コンスタンティノープル信条（381年）において、イエス・キリストは「父と同一本質の神」 として告白されており、これは今日のカトリック教会でも公式な教義として受け継がれています。", url: "blog/40" },
  { id: 10, image: "asmrchurch_ultra_realistic_photo_jesus_christ_western_drawings__505bd86b-0cb4-4861-b3f1-ea9fe4340f4b.png", title: "神の王国とは何か──カルヴァン派の視点", description: "「神の王国」とは、聖書全体を貫く重要な概念であり、キリスト教神学の中心的なテーマの一つです。カルヴァン派（改革派神学）においても、この概念は極めて重要であり、神の主権、恵み、そして救済の計画と深く結びついています。", url: "blog/41" },
  { id: 11, image: "asmrchurch_ultra_realistic_photo_jesus_christ_western_drawings__3606a04c-0806-4c60-a999-5b562ca1f10e.png", title: "エンジニアってなんか性格悪い人多くね？", description: "「エンジニアには性格が悪い人が多いのでは？」という疑問は、技術職に関わる人々のコミュニケーションの傾向や仕事の特性を考えると、ある程度理解できるかもしれません。", url: "blog/42" },
  { id: 12, image: "asmrchurch_ultra_realistic_photo_jesus_christ_western_drawings__420492a8-4536-47ef-b279-8f90b34dd90c.png", title: "おでんツンツンをキリスト教から解釈する", description: "「おでんツンツン」とは、社会の秩序や公共の利益を軽視し、自らの欲求や衝動のままに振る舞う行為の象徴的な表現として捉えることができます。BreakingDownに出る前に、信仰の試合決定をするべきかもしれませんね。", url: "blog/43" },
  { id: 7, image: "", title: "", description: "", url: "blog/" },
  { id: 7, image: "", title: "", description: "", url: "blog/" },
  { id: 7, image: "", title: "", description: "", url: "blog/" },
  { id: 7, image: "", title: "", description: "", url: "blog/" },
  { id: 7, image: "", title: "", description: "", url: "blog/" },

];

const Qa = () => {
  return (
    <div>
      <GridComponent data={data} title={title} dir="qa" />
    </div>
  );
};

export default Qa;

