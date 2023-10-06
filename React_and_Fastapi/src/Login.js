// import { useNavigate } from "react-router";
import { fetchToken} from "./Auth";
// import { setToken } from "./Auth";
import { useState } from "react";
import axios from "axios";

export default function Login() {
  // const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [result, setresult] = useState("");
  const [visible, setvisible] = useState(false);

  const data = {
    username: username,
    password: password,
  };

  // const Text = () => {
  //   if (data.username) {
  //     console.log(data.username)
  //   }
  // }
  const login = () => {
    if ((data.username === "") & (data.password === "")) {
      return;
    } else {
      axios
        .post("http://localhost:5000/user/display", data)
        .then((result)=>{
            setvisible(true);
            setresult(result.data)
            setUsername("")
            setPassword("")

        })
        // .then(function (response) {
        //   console.log(response.data.token, "response.data.token");
        //   if (response.data.token) {
        //     setToken(response.data.token);
        //     navigate("/profile");
        //   }
        // })
        .catch(function (error) {
          console.log(error, "error");
        });
    }
  };

  return (
    <div style={{ minHeight: 800, marginTop: 30 }}>
      <h1>Login page</h1>
      <div style={{ marginTop: 30 }}>
        {fetchToken() ? (
          <p>you are logged in</p>
        ) : (
          <div>
            <form>
              <div>
                <label style={{ marginRight: 10 }}>Input Username</label>
                <input
                  type="text"
                  onChange={(e) => setUsername(e.target.value)}
                  value={username}
                />
              </div>
              <br></br>

              <div>
                <label style={{ marginRight: 10 }}>Input Password</label>
                <input
                  type="text"
                  onChange={(e) => setPassword(e.target.value)}
                  value={password}
                />
              </div>
              <br></br>

              <div>
                <button type="button" onClick={login}>
                  Display Username
                </button>
              </div>

              {visible&&<p>{result}</p>}
            </form>
          </div>
        )}
      </div>
    </div>
  );
}
