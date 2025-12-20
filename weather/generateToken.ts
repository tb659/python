import { SignJWT, importPKCS8 } from "jose";

// 使用与原 Python 版本相同的私钥和 header/kid
const privateKey = `-----BEGIN PRIVATE KEY-----
MC4CAQAwBQYDK2VwBCIEIPEbnYSWS+arsaMqRQ3WMNDK/quw0bLTqG9qZxeDC4hj
-----END PRIVATE KEY-----`;

async function generateJWT() {
  const key = await importPKCS8(privateKey, "EdDSA");
  const now = Math.floor(Date.now() / 1000);

  const payload = {
    sub: "258BR4VM99",
    iat: now - 30,
    exp: now + 900
  };

  const jwt = await new SignJWT(payload).setProtectedHeader({ alg: "EdDSA", kid: "TGGVD7RTJY" }).sign(key);

  console.log("JWT: ", jwt);
}

generateJWT().catch(err => {
  console.error("Error generating JWT:", err);
});
