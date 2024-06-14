import React, { useState } from 'react';
import styles from './register.module.css';
import axios from 'axios';
/* eslint-disable-next-line */
export function Register() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [email, setEmail] = useState('');
  const [location, setLocation] = useState('');

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    if (checkPassword() === 0) {
      alert('Passwords do not match');
      setPassword('');
      setConfirmPassword('');
      return;
    }

    axios
      .post('http://localhost:3001/register', { username, password })
      .then((response) => {
        console.log(response.data);
      })
      .catch((error) => {
        console.log(error);
        setPassword('');
        setConfirmPassword('');
      });
  };
  const checkPassword = () => {
    if (password !== confirmPassword) {
      return 0;
    }
  };

  return (
    <div className={styles['container']}>
      <h1>Welcome to Register!</h1>
      <form onSubmit={handleSubmit} className={styles['register-form']}>
        <label htmlFor="username" className={styles['form-label']}>
          Username:
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            className={styles['form-input']}
            required
          />
        </label>
        <label htmlFor="email" className={styles['form-label']}>
          Email:
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className={styles['form-input']}
            required
          />
        </label>
        <label htmlFor="location" className={styles['form-label']}>
          Location:
          <input
            type="text"
            id="location"
            value={location}
            onChange={(e) => setLocation(e.target.value)}
            className={styles['form-input']}
            required
          />
        </label>
        <label htmlFor="password" className={styles['form-label']}>
          Password:
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className={styles['form-input']}
            required
          />
        </label>
        <label htmlFor="confirm-password" className={styles['form-label']}>
          Confirm Password:
          <input
            type="password"
            id="confirm-password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            className={styles['form-input']}
            required
          />
        </label>

        <button type="submit" className={styles['submit-button']}>
          Register
        </button>
      </form>
    </div>
  );
}

export default Register;
