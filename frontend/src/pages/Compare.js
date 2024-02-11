import React from 'react'
import {useState, useEffect} from 'react'

export default function Compare() {
    const [tanks, setTanks] = useState([]);

    useEffect(() => {
        fetch("http://127.0.0.1:8000/api/")
        .then(res => res.json())
        .then(
            (result) => {
            tanks(result);
           },
            // Note: it's important to handle errors here
            // instead of a catch() block so that we don't swallow
            // exceptions from actual bugs in components.
        )
    }, [])

    return (
        <ul>
        {tanks.map(tank => (
            <li key={tank.id}>
            {tank.name} {tank.tier}
            </li>
        ))}
        </ul>
    );
}
