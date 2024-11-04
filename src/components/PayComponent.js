import React, { useState, useEffect } from "react";
import Header from '../components/Header';

const ProductDisplay = () => (
  <div className="product">
    <div>
      <div className="productmain">
        <div className="description">
            <h3>ASMRキリスト教会をサポートしてください！</h3>
            <h5>ASMRキリスト教会は、聖書ASMRの製造、口語訳聖書のアーカイブ保存公開、若者の伝道活動、いのちのASMR電話、その他日本のキリスト教をプロテスタントの観点から維持・発展させる活動を継続しております。もし当教会の理念に賛同いただける方は、献金サポートしていただけますと弊社の活動の重要な資金源になります。</h5>
        </div>
      </div>

      <stripe-buy-button
        buy-button-id="buy_btn_1QHOukJrEFc0aosh3vOvliXi"
        publishable-key="pk_live_51L77y9JrEFc0aoshDbT8faRDJBWQJjQTGvMb6jngK3GGGpMtIYf8omncPkMd8e0be0ZsfG2yEWaxYdMSlGSS9pgX00RNzmWvfw"
      ></stripe-buy-button>
    </div>
  </div>
);

const Message = ({ message }) => (
  <section>
    <p>{message}</p>
  </section>
);

export default function PayComponent() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    // Check to see if this is a redirect back from Checkout
    const query = new URLSearchParams(window.location.search);

    if (query.get("success")) {
      setMessage("Order placed! You will receive an email confirmation.");
    }

    if (query.get("canceled")) {
      setMessage(
        "Order canceled -- continue to shop around and checkout when you're ready."
      );
    }
  }, []);

  return message ? (
    <Message message={message} />
  ) : (
    <ProductDisplay />
  );
}

