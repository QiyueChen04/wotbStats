import React from 'react'
import {useState, useEffect} from 'react'

export default function Compare() {
  const [allTanks, setAllTanks] = useState([]);
  const [error, setError] = useState(null);
  const [isLoaded, setIsLoaded] = useState(false);

  const [shownTanks, setShownTanks] = useState([]);

    useEffect(() => {
      fetch("http://127.0.0.1:8000/api/allTanks/")
        .then(res => res.json())
        .then(
          (result) => {
            setIsLoaded(true);
            setAllTanks(result);
          },
          (error) => {
            setIsLoaded(true);
            setError(error);
          }
        )
    }, [])

    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      const listAllTanks = allTanks.map((tank) =>
      <li key={tank.tank_id}>
        {tank.name}
      </li>
      );
      return (
        <ul>{listAllTanks}</ul>
      );
    }
}
