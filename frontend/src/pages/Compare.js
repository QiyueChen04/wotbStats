import React from 'react';
import {useState, useEffect} from 'react';

import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form'
import ButtonGroup from 'react-bootstrap/ButtonGroup'
import Button from 'react-bootstrap/Button'

function Filter( {allTanks} ) {
  const [searchResult, setSearchResult] = useState('');
  const [tier, setTier] = useState();
  const [type, setType] = useState('mediumTank');
  const [filteredTanks, setFilteredTanks] = useState([]);

  // function handleChangeTier(num) { 
  //   setSearchResult = '';
  //   setTier(num);
  // }

  return (
    <>
      <Container className='container text-center'>
        <Row className='justify-content-md-center'>
          <SearchBar searchResult = {searchResult} setSearchResult = {setSearchResult} />
        </Row>
        <Row>
          <hr />
        </Row>
        <Row className='justify-content-md-center'>
          <TierSelection setTier = {setTier} />
        </Row>
        <Row>
          <hr />
        </Row>
        <Row className='justify-content-md-center'>
          <TypeSelection setType = {setType} />
        </Row>
      </Container>

      <p>{searchResult}</p>
      <p>{tier}</p>
      <p>{type}</p>

    </>
  );
}

function SearchBar({searchResult, setSearchResult}) {
  return (
    <>
      <Col className='col col-lg-2'>
        <Form onSubmit={(e) => {e.preventDefault()}}>
          <input 
          type="text" 
          value={searchResult} 
          placeholder="Search..." 
          onChange={(e) => setSearchResult(e.target.value)} 
          />
        </Form>
      </Col>
    </>
  );
}

function TierSelection({setTier}) {
  return (
    <>
      <ButtonGroup className="me-2" aria-label="First group">
        <Button onClick={() => setTier(1)}>1</Button>
        <Button onClick={() => setTier(2)}>2</Button>
        <Button onClick={() => setTier(3)}>3</Button>
        <Button onClick={() => setTier(4)}>4</Button>
        <Button onClick={() => setTier(5)}>5</Button>
        <Button onClick={() => setTier(6)}>6</Button>
        <Button onClick={() => setTier(7)}>7</Button>
        <Button onClick={() => setTier(8)}>8</Button>
        <Button onClick={() => setTier(9)}>9</Button>
        <Button onClick={() => setTier(10)}>10</Button>
      </ButtonGroup>
    </>
  );
}

function TypeSelection({setType}) {
  return (
    <>
      <ButtonGroup className="me-2" aria-label="First group">
        <Button onClick={() => setType('lightTank')}>Light</Button>
        <Button onClick={() => setType('mediumTank')}>Medium</Button>
        <Button onClick={() => setType('heavyTank')}>Heavy</Button>
        <Button onClick={() => setType('AT-SPG')}>TD</Button>
      </ButtonGroup>
    </>
  );
}

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
  }

  return (
    <Container fluid>
      <Filter allTanks={allTanks} />
    </Container>
  )
  
  // } else {
  //   const listAllTanks = allTanks.map((tank) =>
  //   <li key={tank.tank_id}>
  //     {tank.name}
  //   </li>
  //   );
  //   return (
  //     <ul>{listAllTanks}</ul>
  //   );
  // }
}
