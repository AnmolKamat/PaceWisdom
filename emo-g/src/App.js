import React, { useState, useEffect } from "react";
import "./css/App.css";


const clicked = (emo) =>{
  navigator.clipboard.writeText(emo)
  alert("copied to clipboard")
  let particles = document.getElementsByTagName("h6")
  for (let i=0;i<particles.length;i++){
    particles[i].innerHTML = emo
  }
    

}

const bg = ()=>{
  let bd = document.getElementById("particle-container")
  for (let i=0;i<100;i++){
  let particle = document.createElement("h6")
  particle.classList.add("particle")
  particle.innerHTML = "😍"
  bd.appendChild(particle)
}
}


const SearchBar = () => {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  bg()
  useEffect(() => {
    const fetchSearchResults = async () => {
      try {
        const response = await fetch(
          `https://emoji-api.com/emojis?access_key=e456bb6e51691b37a21c56f2c864c9751f65d931&search=${query}`
        );
        const data = await response.json();
        setResults(data);
      } catch (error) {
        console.error("Error fetching search results:", error);
      }
    };

    const delayDebounceFn = setTimeout(() => {
      if (query.length > 0) {
        fetchSearchResults();
      } else {
        setResults([]);
      }
    }, 300); // Debounce time in milliseconds

    return () => clearTimeout(delayDebounceFn);
  }, [query]);

  return (
    <div className="main">
      <div className="emo-g">
        <h1 className="Head">Emo-G </h1>
        <div className="group">
          <svg className="icon" aria-hidden="true" viewBox="0 0 24 24">
            <g>
              <path d="M21.53 20.47l-3.66-3.66C19.195 15.24 20 13.214 20 11c0-4.97-4.03-9-9-9s-9 4.03-9 9 4.03 9 9 9c2.215 0 4.24-.804 5.808-2.13l3.66 3.66c.147.146.34.22.53.22s.385-.073.53-.22c.295-.293.295-.767.002-1.06zM3.5 11c0-4.135 3.365-7.5 7.5-7.5s7.5 3.365 7.5 7.5-3.365 7.5-7.5 7.5-7.5-3.365-7.5-7.5z"></path>
            </g>
          </svg>
          <input
            type="search"
            className="input"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Search..."
          />
        </div>
        <ul>
          {results == null ? (
            <p>No result</p>
          ) : (
            results.map((result) => (
              <li onClick={() => clicked(result.character)}>
                <span>{result.character}</span>
                <p>{result.unicodeName}</p>
              </li>
            ))
          )}
        </ul>
      </div>
    </div>
    
  );
};
export default SearchBar;
