import React from 'react';
import {useState} from 'react';

import '../css/Filter.css';

import Form from 'react-bootstrap/Form'

import ButtonGroup from 'react-bootstrap/ButtonGroup'

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
    <div className='filter-row'>
      <div className='filter-elements-container'>
        <SearchBar searchResult = {searchResult} onChangeSearch = {handleChangeSearch} />
        <br/>
        <TierSelection onChangeTier = {handleChangeTier} />
        <br/>
        <TypeSelection onChangeType = {handleChangeType} />
      </div>
      <div className='card-container'>
        <DisplayFilteredTanks filteredTanks={filteredTanks} onAddTank={onAddTank} />
      </div>
    </div>
  );
}

function SearchBar({searchResult, onChangeSearch}) {
  return (
    <>
      <Form onSubmit={(e) => {e.preventDefault()}}>
        <input 
          type="text" 
          value={searchResult} 
          placeholder="Search..." 
          onChange={(e) => onChangeSearch(e.target.value)} 
        />
      </Form>
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
    <div className='card-container'>
      {filteredTanks.map((tank) => (
        <div className='card' onClick={(e) => onAddTank(tank)}>
          <img src = {tank.image_preview} alt="tank image" />
          <div class="card-content">
            <p>{tank.name}</p>
          </div>
        </div>
      ))}
    </div>
  );
}
