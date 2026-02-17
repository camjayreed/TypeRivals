import "./App.css";

function App() {
  return (
    <>
      <div className="navbar">
        {/* Not super sure what to put in the navbar */}
        <h1>TypeRivals</h1>

        <div className="nav-links">
          <a href="">Login</a>
          <a href="">Register</a>
        </div>
      </div>

      <div className="infobox">
        <div className="infobox-txt">
          <p style={{ textDecoration: "underline", textUnderlineOffset: "35%" }}>Welcome to TypeRivals</p>
          <p>TypeRivals is a real time online multiplayer typing PvP game</p>
          <p> the goal is to out type the other player, win the match, and climb the ranks.</p>
        </div>
      </div>
      <a href="https://github.com/camjayreed" className="author">Made By: Cameron Reed</a>
    </>
  );
}

export default App;
