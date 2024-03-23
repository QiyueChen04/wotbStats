import React, { useState } from 'react';
import axios from 'axios';

import Table from 'react-bootstrap/Table';
import Image from 'react-bootstrap/Image';
import Container from 'react-bootstrap/Container';

import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';

export function DisplayTanks({chosenTanks, onRemoveTank}) {
  const [guns, setGuns] = useState([]);

  async function addGun(tank_id) {
      try {
          const url = 'http://127.0.0.1:8000/api/getTankGuns/'; 
          const response = await axios.get(url, {
              params: {
                  tank_id: tank_id
              }
          });
          console.log(response.data[0]);
          setGuns([...guns, response.data[0]]);
      } catch (error) {
          console.error('Error fetching data:', error);
      }
  }

  return(
    <Container>
    <Table striped border="true" hover>
        <thead>
          <tr>
            <td> Tank </td>
            <td> Specs </td>
            <td> Caliber</td>
            <td> Reload Time  </td>
            <td> Gun Depression  </td>
            <td> Gun Elevation  </td>
  
            <td> HP </td>
            <td> Front Armor</td>
            <td> Side Armor</td>
            <td> Rear Armor</td>
          </tr>
        </thead>
        <tbody>
          {chosenTanks.map((tank) =>
            <tr key={tank.tank_id}>
              <td>
                <Image src={tank.image_preview} width={80} height={60} fluid onClick={() => onRemoveTank(tank)}/>
                <p> {tank.tank_name} </p>
              </td>

              <td> 
                <Dropdown>
                  <Dropdown.Toggle variant="secondary"> Gun </Dropdown.Toggle>
                  <Dropdown.Menu>
                    <Dropdown.Item onClick={() => addGun(tank.tank_id)}> Action </Dropdown.Item>
                    <Dropdown.Item href="#/action-2">Another action</Dropdown.Item>
                    <Dropdown.Item href="#/action-3">Something else</Dropdown.Item>
                    <Dropdown.Divider />
                    <Dropdown.Item href="#/action-4">Separated link</Dropdown.Item>
                  </Dropdown.Menu>
                </Dropdown>
              </td>
  
              <td>{tank.caliber}</td>
              <td>{tank.reload_time}</td>
              <td>{tank.move_down_arc}</td>
              <td>{tank.move_up_arc}</td>
  
              <td>{tank.hp}</td>
              <td>{tank.front}</td>
              <td>{tank.sides}</td>
              <td>{tank.rear}</td>
            </tr>
          )}
        </tbody>
      </Table>
    </Container>
  );
}
