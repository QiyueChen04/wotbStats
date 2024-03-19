import React from 'react';
import axios from 'axios';
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

  async function handleAddTank(tank_id) {
      try {
          const url = 'http://127.0.0.1:8000/api/tankInfo/'; // Adjust the URL as needed
          const response = await axios.get(url, {
              params: {
                  tank_id: tank_id
              }
          });
          console.log(response.data[0])
          setChosenTanks([...chosenTanks, response.data[0]]);
      } catch (error) {
          console.error('Error fetching data:', error);
      }
  }
  // const fetchTankData = async (tank_name) => {
  //   try {
  //     // Make API call to your Django backend
  //     const response = await axios.get('/api/endpoint', {
  //       params: {
  //         arg1: arg1,
  //         arg2: arg2
  //       }
  //     });

  //     // Set data received from the backend
  //     setData(response.data);
  //   } catch (error) {
  //     console.error('Error fetching data:', error);
  //   }
  // };
  // function handleAddTank(newTank) {
  //   setChosenTanks([...chosenTanks, newTank]);
  // }

  function handleRemoveTank(removeTank) {
    setChosenTanks(
      chosenTanks.filter(tank => tank !== removeTank)
    );
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
        <br/>
        <Row>
          <Filter allTanks = {allTanks} onAddTank={handleAddTank} />
        </Row>
        <Row>
          <DisplayTanks chosenTanks = {chosenTanks} onRemoveTank={handleRemoveTank}/>
        </Row>
      </Container>     
    </>
  );
}
