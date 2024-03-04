import React from 'react';
import {useState} from 'react';

import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form'

import ButtonGroup from 'react-bootstrap/ButtonGroup'
import Button from 'react-bootstrap/Button'

import Card from 'react-bootstrap/Card'
import CardImg from 'react-bootstrap/CardImg'
import CardBody from 'react-bootstrap/CardBody'

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
        <Row className='justify-content-md-center'>
          <SearchBar searchResult = {searchResult} onChangeSearch = {handleChangeSearch} />
        </Row>

        <hr />

        <Row className='justify-content-md-center'>
          <TierSelection onChangeTier = {handleChangeTier} />
        </Row>

        <hr />

        <Row className='justify-content-md-center'>
          <TypeSelection onChangeType = {handleChangeType} />
        </Row>

        <hr />

        <Row className='justify-content-md-center'>
          <DisplayFilteredTanks filteredTanks = {filteredTanks} onAddTank = {onAddTank} />
        </Row>
      </Container>
    </>
  );
}
  
function SearchBar({searchResult, onChangeSearch}) {
  return (
    <>
      <Col className='col col-lg-2'>
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
      <ButtonGroup className="me-2" aria-label="First group">
        <Button onClick={() => onChangeTier(1)}>1</Button>
        <Button onClick={() => onChangeTier(2)}>2</Button>
        <Button onClick={() => onChangeTier(3)}>3</Button>
        <Button onClick={() => onChangeTier(4)}>4</Button>
        <Button onClick={() => onChangeTier(5)}>5</Button>
        <Button onClick={() => onChangeTier(6)}>6</Button>
        <Button onClick={() => onChangeTier(7)}>7</Button>
        <Button onClick={() => onChangeTier(8)}>8</Button>
        <Button onClick={() => onChangeTier(9)}>9</Button>
        <Button onClick={() => onChangeTier(10)}>10</Button>
      </ButtonGroup>
    </>
  );
}
  
function TypeSelection({onChangeType}) {
  return (
    <>
      <ButtonGroup className="me-2" aria-label="First group">
        <Button onClick={() => onChangeType('lightTank')}>Light</Button>
        <Button onClick={() => onChangeType('mediumTank')}>Medium</Button>
        <Button onClick={() => onChangeType('heavyTank')}>Heavy</Button>
        <Button onClick={() => onChangeType('AT-SPG')}>TD</Button>
      </ButtonGroup>
    </>
  );
}
  
function DisplayFilteredTanks({filteredTanks, onAddTank}) {
  return (
    <>
      {filteredTanks.map((tank) => (
        <Col key={tank.tank_id}>
          <Card style={{ width: '12rem'}} className="text-center">
            <cardBody>
              <CardImg src = {tank.image_preview} alt = "tank image"/>
              <CardBody>{tank.name}</CardBody>
              <Button variant="primary" onClick={(e) => onAddTank(tank)}>Select</Button>
            </cardBody>
          </Card>
        </Col>
      ))}
    </>
  );
}