import React from 'react';
import {useState} from 'react';

import '../css/Filter.css';

import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form'

import Card from 'react-bootstrap/Card'
import CardImg from 'react-bootstrap/CardImg'
import CardBody from 'react-bootstrap/CardBody' 

import ButtonGroup from 'react-bootstrap/ButtonGroup'
import Button from 'react-bootstrap/Button'

export function Filter( {allTanks, onAddTank} ) {
  const [searchResult, setSearchResult] = useState('');
  const [tier, setTier] = useState(10);
  const [type, setType] = useState('mediumTank');
  const [filteredTanks, setFilteredTanks] = useState([]);

  function filter() {
    if(searchResult !== '') {
      let filteredResult = allTanks.filter((tank) => tank.name.toLowerCase().match(searchResult));
      setFilteredTanks(filteredResult);
    }
    else {
      let filteredResult = allTanks.filter((tank) => tank.tier === (tier)).filter((tank) => String(tank.type) === type);
      setFilteredTanks(filteredResult);
    }
  }

  function handleChangeSearch(str) {
    setSearchResult(str);
    filter();
  }

  function handleChangeTier(num) { 
    setSearchResult('');
    setTier(num);
    filter();
  }

  function handleChangeType(str) {
    setSearchResult('');
    setType(str);
    filter();
  }

  return (
    <>
      <Container className='container text-center'>
        <Row>
          <Col>
            <Row className='justify-content-md-center'>
              <SearchBar searchResult = {searchResult} onChangeSearch = {handleChangeSearch} />
            </Row>

            <br />

            <Row className='justify-content-md-center'>
              <TierSelection onChangeTier = {handleChangeTier} />
            </Row>

            <br />

            <Row className='justify-content-md-center'>
              <TypeSelection onChangeType = {handleChangeType} />
            </Row>
          </Col>

          <Col>
            <Row>
              <DisplayFilteredTanks filteredTanks={filteredTanks} onAddTank={onAddTank} />
            </Row>
          </Col>

        </Row>
      </Container>
    </>
  );
}
  
function SearchBar({searchResult, onChangeSearch}) {
  return (
    <>
      <Col>
        <Form onSubmit={(e) => {e.preventDefault()}}>
          <input 
            type="text" 
            value={searchResult} 
            placeholder="Search..." 
            onChange={(e) => onChangeSearch(e.target.value)} 
          />
        </Form>
      </Col>
    </>
  );
}
  
function TierSelection({onChangeTier}) {
  return (
    <>
      <ButtonGroup className="me-2">
        <button className='tier-button' onClick={() => onChangeTier(1)}>1</button>
        <button className='tier-button' onClick={() => onChangeTier(2)}>2</button>
        <button className='tier-button' onClick={() => onChangeTier(3)}>3</button>
        <button className='tier-button' onClick={() => onChangeTier(4)}>4</button>
        <button className='tier-button' onClick={() => onChangeTier(5)}>5</button>
        <button className='tier-button' onClick={() => onChangeTier(6)}>6</button>
        <button className='tier-button' onClick={() => onChangeTier(7)}>7</button>
        <button className='tier-button' onClick={() => onChangeTier(8)}>8</button>
        <button className='tier-button' onClick={() => onChangeTier(9)}>9</button>
        <button className='tier-button' onClick={() => onChangeTier(10)}>10</button>
      </ButtonGroup>
    </>
  );
}
  
function TypeSelection({onChangeType}) {
  return (
    <>
      <ButtonGroup className="me-2">
        <button className='type-button' onClick={() => onChangeType('lightTank')}>Light</button>
        <button className='type-button' onClick={() => onChangeType('mediumTank')}>Medium</button>
        <button className='type-button' onClick={() => onChangeType('heavyTank')}>Heavy</button>
        <button className='type-button' onClick={() => onChangeType('AT-SPG')}>TD</button>
      </ButtonGroup>
    </>
  );
}

function DisplayFilteredTanks({filteredTanks, onAddTank}) {
  return (
    <>
      {filteredTanks.map((tank) => (
        <div key={tank.tank_id}>
          <Card style={{ width: '12rem'}} className="text-center">
            <cardBody>
              <CardImg src = {tank.image_preview} alt = "tank image"/>
              <CardBody>{tank.name}</CardBody>
              <Button variant="primary" onClick={(e) => onAddTank(tank)}>Select</Button>
            </cardBody>
          </Card>
        </div>
      ))}
    </>
  );
}