import styles from './workers.module.css';
import axios from 'axios';
import { useEffect, useState } from 'react';
/* eslint-disable-next-line */

export function Workers() {
  axios.get('http://localhost:8000/workers').then((response) => {
    console.log(response);
  });

  return (
    <div className={styles['container']}>
      <h1>Welcome to Workers!</h1>
    </div>
  );
}

export default Workers;
