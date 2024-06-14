import React from 'react';
import { Link } from 'react-router-dom';
import styles from './navbar.module.css';

/* eslint-disable-next-line */

export function Navbar() {
  return (
    <div className={styles['navbar']}>
      <h1 className={styles['brand']}>Duxio</h1>
      <ul className={styles['nav-links']}>
        <li className={styles['nav-item']}>
          <Link to="/">Home</Link>
        </li>
        <li className={styles['nav-item']}>
          <Link to="/login">login</Link>
        </li>
        <li className={styles['nav-item']}>
          <Link to="/workers">Workers</Link>
        </li>
      </ul>
    </div>
  );
}

export default Navbar;
