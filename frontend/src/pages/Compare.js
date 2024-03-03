import React from 'react';
import {useState, useEffect} from 'react';

import { Header } from '../components/Header';
import { Filter } from '../components/Filter';
import { DisplayTanks } from '../components/DisplayTanks';

import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';

export default function Compare() {
  const [allTanks, setAllTanks] = useState([]);
  const [error, setError] = useState(null);
  const [isLoaded, setIsLoaded] = useState(false);

  const [chosenTanks, setChosenTanks] = useState([]);

  function handleAddTank(newTank) {
    setChosenTanks([...chosenTanks, newTank]);
  }

  function handleDeleteTank(newTank) {
    
  }

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
  } 
  else if (!isLoaded) {
    return <div>Loading...</div>;
  }

  return (
    <>
      <Container fluid>
        <Row>
          <Header/>
        </Row>
        <Row>
          <Filter allTanks = {allTanks} onAddTank={handleAddTank} />
        </Row>
        <Row>
          <DisplayTanks chosenTanks = {chosenTanks} />
        </Row>
      </Container>
      <hr />        
    </>
  );
}
