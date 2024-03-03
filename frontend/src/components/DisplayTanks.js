import React from 'react';

import Container from 'react-bootstrap/Container';
import Image from 'react-bootstrap/Image'
import Table from 'react-bootstrap/Table'

export function DisplayTanks({chosenTanks, onRemoveTank}) {
  return(
    <Container className='container text-center'>
      <Table striped border hover>
        <thead>
          <tr>
            <td> Tank </td>
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
            <tr>
              <td>
                <Image src={tank.image_preview} width={80} height={60} onClick={() => onRemoveTank(tank)}/>
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
