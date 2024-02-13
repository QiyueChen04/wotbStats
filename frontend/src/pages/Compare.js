import React from 'react';
import {useState, useEffect} from 'react';

import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form'

import Image from 'react-bootstrap/Image'

import ButtonGroup from 'react-bootstrap/ButtonGroup'
import Button from 'react-bootstrap/Button'

import Card from 'react-bootstrap/Card'
import CardHeader from 'react-bootstrap/CardHeader'
import CardImg from 'react-bootstrap/CardImg'
import CardBody from 'react-bootstrap/CardBody'
import CardImgOverlay from 'react-bootstrap/CardImgOverlay'
import cardBody from 'react-bootstrap/CardBody'

import Table from 'react-bootstrap/Table'

function Filter( {allTanks, onAddTank} ) {
  const [searchResult, setSearchResult] = useState('');
  const [tier, setTier] = useState(10);
  const [type, setType] = useState('mediumTank');
  const [filteredTanks, setFilteredTanks] = useState([]);

  function filter() {
    if(searchResult != '') {
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
      </Container>

      <hr />

      <Container>
        <Row className='justify-content-md-center'>
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

function DisplayTanks({shownTanks}) {
  return(
      <Container>
        <Row className='justify-content-md-center'>
        {shownTanks?.map((tank) => 
          <Col key={tank.tank_id}>
            <Card style={{ width: '12rem'}} className="text-center">
              <cardBody>
                <CardImg src = {tank.image_preview} alt = "tank image"/>
                <CardBody>{tank.name}</CardBody>
              </cardBody>
            </Card>
          </Col>
        )}
        </Row>
      </Container>
  );
}

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
          <Filter allTanks={allTanks} onAddTank={handleAddTank} />
        </Row>
      </Container>
      <hr />
      <Container>
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
                  <Image src={tank.image_preview} width={80} height={60}/>

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
      {/* <Container>
        <Table striped="columns" bordered={true}>
          <tbody>
            <Row>
              <Col>
                <tr>
                  <td> Name</td>
                </tr>
                <tr>
                  <td> Name</td>
                </tr>
                <tr>
                  <td> Name</td>
                </tr>
              </Col>
              {chosenTanks.map((tank) => 
                <Col key={tank.tank_id}>
                  <Row>{tank.name}</Row>
                  <Row>{tank.tier}</Row>
                  <Row>{tank.type}</Row>
                </Col>
              )} 
            </Row>
           </tbody>
          
        </Table>
      </Container> */}

        
    </>
  );
}
