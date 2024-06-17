import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import styles from './navbar.module.css';

function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  const closeMenu = () => {
    setIsOpen(false);
  };

  // Close the menu when clicking outside of it
  useEffect(() => {
    const handleOutsideClick = (event: any) => {
      if (!event.target.closest(`.${styles['navbar']}`) && isOpen) {
        closeMenu();
      }
    };

    document.addEventListener('mousedown', handleOutsideClick);
    return () => document.removeEventListener('mousedown', handleOutsideClick);
  }, [isOpen]);

  return (
    <div className={styles['navbar']}>
      <h1 className={styles['brand']}>Duxio</h1>

      <div className={styles['menu-icon']} onClick={toggleMenu}>
        <div className={isOpen ? styles['bar1-change'] : styles['bar1']}></div>
        <div className={isOpen ? styles['bar2-change'] : styles['bar2']}></div>
        <div className={isOpen ? styles['bar3-change'] : styles['bar3']}></div>
      </div>
      <ul
        className={`${styles['nav-links']} ${
          isOpen ? styles['nav-active'] : ''
        }`}
      >
        <li className={styles['nav-item']} onClick={closeMenu}>
          <Link to="/">Home</Link>
        </li>
        <li className={styles['nav-item']} onClick={closeMenu}>
          <Link to="/workers">Workers</Link>
        </li>
      </ul>
    </div>
  );
}

export default Navbar;
